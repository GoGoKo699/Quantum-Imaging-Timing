#!/usr/bin/env python3
"""Deterministic checks of the pair receiver and ideal random-gap formulas.

Run from any directory with ``python verification/verify_receiver.py``.
Successful execution prints one JSON object and writes no artifacts. Assertions
raise on failure. These finite calculations corroborate formulas; the Markdown
proofs establish their uniform and asymptotic scope.
"""

from __future__ import annotations

import itertools
import json
import math
import warnings

import numpy as np
from scipy.integrate import IntegrationWarning, quad
from scipy.optimize import brentq
from scipy.special import exp1, roots_hermitenorm
from scipy.stats import binom


def pair_probabilities(v: float, q: float) -> tuple[float, float, float]:
    """Return p_v(0), p_v(q), and their difference without cancellation."""
    assert v >= 0.0 and q > 0.0
    p0 = -0.5 * math.expm1(-0.5 * math.log1p(v))
    delta = -math.expm1(-2.0 * q / (1.0 + v)) / (4.0 * math.sqrt(1.0 + v))
    return p0, p0 + delta, delta


def pair_h2(v: float, h: float) -> float:
    """Squared Hellinger distance in the convention H^2 = 1 - affinity."""
    p0, ph, delta = pair_probabilities(v, h)
    den_one = (math.sqrt(p0) + math.sqrt(ph)) ** 2
    den_zero = (math.sqrt(1.0 - p0) + math.sqrt(1.0 - ph)) ** 2
    return 0.5 * delta**2 * (1.0 / den_one + 1.0 / den_zero)


def pair_constants(v_max: float, q_max: float) -> tuple[float, float]:
    a = math.exp(-2.0 * q_max) / (2.0 * (1.0 + v_max) ** 1.5)
    b = min(a, 1.0 / (2.0 * math.sqrt(1.0 + v_max) * (math.sqrt(1.0 + v_max) + 1.0)))
    return a * a / 4.0, 1.0 / (8.0 * b) + (v_max + q_max) / 16.0


def poisson_j(h: float, kappa: float) -> float:
    return h * h / kappa * math.log1p(kappa / h)


def exp_mean_integral(function, ratio: float) -> float:
    """Integrate on x=v/kappa, splitting at the h/kappa boundary layer."""
    points = [0.0]
    if ratio < 1.0:
        points.append(ratio)
    points.append(1.0)
    value = 0.0
    for lo, hi in zip(points[:-1], points[1:]):
        piece, _ = quad(function, lo, hi, epsabs=2e-10, epsrel=2e-10, limit=300)
        value += piece
    tail, _ = quad(function, 1.0, np.inf, epsabs=2e-10, epsrel=2e-10, limit=300)
    return value + tail


def check_pair_integral() -> dict:
    nodes, weights = roots_hermitenorm(256)
    weights = weights / math.sqrt(2.0 * math.pi)
    errors = []
    for v in (0.0, 1e-7, 0.01, 0.4, 2.0, 10.0):
        z = math.sqrt(v) * nodes
        for q in (1e-9, 1e-4, 0.02, 0.2, 1.5):
            offset = 2.0 * math.sqrt(q)
            overlap = float(
                weights
                @ (
                    0.5 * np.exp(-z * z / 2.0)
                    + 0.25 * np.exp(-(z + offset) ** 2 / 2.0)
                    + 0.25 * np.exp(-(z - offset) ** 2 / 2.0)
                )
            )
            quadrature_probability = (1.0 - overlap) / 2.0
            _, exact_probability, _ = pair_probabilities(v, q)
            errors.append(abs(exact_probability - quadrature_probability))
    assert max(errors) < 8e-13, max(errors)
    return {"cases": len(errors), "max_absolute_probability_error": max(errors)}


def check_hellinger_bounds() -> dict:
    v_max, q_max = 2.0, 0.25
    c_pair, c_upper = pair_constants(v_max, q_max)
    ratios = []
    for v in np.r_[0.0, np.geomspace(1e-10, v_max, 24)]:
        for h in np.geomspace(1e-10, q_max, 24):
            ratio = pair_h2(float(v), float(h)) / (h * h / (v + h))
            assert c_pair * (1.0 - 1e-12) <= ratio <= c_upper * (1.0 + 1e-12)
            ratios.append(float(ratio))
    # A zero-motion null is Bernoulli(0); this detects a factor-two convention error.
    _, p, _ = pair_probabilities(0.0, 0.1)
    zero_motion = pair_h2(0.0, 0.1)
    assert abs(zero_motion - (1.0 - math.sqrt(1.0 - p))) < 3e-16
    return {
        "cases": len(ratios),
        "convention": "H^2 = 1 - affinity",
        "proved_lower_constant": c_pair,
        "proved_upper_constant": c_upper,
        "observed_ratio_min": min(ratios),
        "observed_ratio_max": max(ratios),
    }


def product_probabilities(bits: np.ndarray, probabilities: np.ndarray) -> np.ndarray:
    return np.prod(np.where(bits, probabilities, 1.0 - probabilities), axis=1)


def check_matching_and_finite_tests() -> dict:
    schedules = [
        ("regular", np.full(14, 0.06), 0.15),
        ("alternating", np.array([0.9, 0.002, 0.7, 0.004, 0.6, 0.006, 0.5, 0.008, 0.8, 0.01, 0.7, 0.012]), 0.09),
        ("irregular", np.array([0.11, 0.003, 0.05, 0.7, 0.001, 0.3, 0.02, 0.4, 0.005, 0.2]), 0.07),
    ]
    reports = []
    for name, gaps, h in schedules:
        weights = h * h / (gaps + h)
        matching_weights = [float(weights[0::2].sum()), float(weights[1::2].sum())]
        parity = int(np.argmax(matching_weights))
        chosen = gaps[parity::2]
        assert matching_weights[parity] >= float(weights.sum()) / 2.0 - 1e-15
        p0 = np.array([pair_probabilities(float(v), h)[0] for v in chosen])
        ph = np.array([pair_probabilities(float(v), h)[1] for v in chosen])
        bits = np.array(list(itertools.product((0, 1), repeat=len(chosen))), dtype=bool)
        llr = bits @ np.log(ph / p0) + (~bits) @ np.log((1.0 - ph) / (1.0 - p0))
        reject = llr >= 0.0
        assert np.all(np.log(ph * (1.0 - p0) / (p0 * (1.0 - ph))) > 0.0)
        p_null = product_probabilities(bits, p0)
        p_alt = product_probabilities(bits, ph)
        alpha = float(p_null[reject].sum())
        beta = float(p_alt[~reject].sum())
        affinity = float(np.prod(np.sqrt(p0 * ph) + np.sqrt((1.0 - p0) * (1.0 - ph))))
        assert abs(alpha + beta - float(np.minimum(p_null, p_alt).sum())) < 1e-13
        assert alpha + beta <= affinity + 1e-13
        later_betas = []
        for q in (h, 2.0 * h, 0.7, 3.0, 100.0):
            pq = np.array([pair_probabilities(float(v), q)[1] for v in chosen])
            current_beta = float(product_probabilities(bits, pq)[~reject].sum())
            assert current_beta <= beta + 1e-13
            later_betas.append(current_beta)
        assert all(b <= a + 1e-13 for a, b in zip(later_betas[:-1], later_betas[1:]))
        reports.append({
            "schedule": name,
            "selected_pairs": len(chosen),
            "retained_information_fraction": matching_weights[parity] / float(weights.sum()),
            "type_I_error": alpha,
            "type_II_error_at_h": beta,
            "product_affinity_bound_on_each_error": affinity,
            "type_II_errors_at_increasing_q": later_betas,
        })

    # An exact binomial calculation with enough identical pairs to be informative.
    pair_count, v, h = 500, 0.001, 0.05
    p0, ph, _ = pair_probabilities(v, h)
    bit_weight = math.log(ph * (1.0 - p0) / (p0 * (1.0 - ph)))
    offset = pair_count * math.log((1.0 - ph) / (1.0 - p0))
    threshold = math.ceil(-offset / bit_weight)
    alpha = float(binom.sf(threshold - 1, pair_count, p0))
    beta = float(binom.cdf(threshold - 1, pair_count, ph))
    affinity = math.exp(pair_count * math.log1p(-pair_h2(v, h)))
    assert alpha + beta <= affinity + 1e-13
    assert max(alpha, beta) < 0.01
    return {
        "enumerated_tests": reports,
        "informative_binomial_test": {
            "pairs": pair_count,
            "gap_variance": v,
            "design_h": h,
            "reject_at_or_above_antisymmetric_count": threshold,
            "type_I_error": alpha,
            "type_II_error": beta,
            "product_affinity_bound_on_each_error": affinity,
        },
    }


def check_poisson_integrals() -> dict:
    resolvent_ratios = []
    formula_errors = []
    for ratio in np.geomspace(1e-7, 100.0, 15):
        normalizer = math.log1p(1.0 / ratio)
        integral = exp_mean_integral(
            lambda x: math.exp(-x) / ((x + ratio) * normalizer), float(ratio)
        )
        exact = math.exp(float(ratio)) * float(exp1(ratio)) / normalizer
        formula_errors.append(abs(integral - exact))
        assert math.exp(-1.0) - 1e-10 <= integral <= 1.0 + 1e-10
        resolvent_ratios.append(integral)
    assert max(formula_errors) < 2e-9

    kappa_max, q_max = 2.0, 0.25
    c_pair, _ = pair_constants(kappa_max, q_max)
    lower = c_pair / math.e
    pair_ratios = []
    for kappa in (1e-5, 0.02, 0.3, 2.0):
        for h in (1e-7, 1e-4, 0.02, 0.2):
            j = poisson_j(h, kappa)
            ratio = exp_mean_integral(
                lambda x: math.exp(-x) * pair_h2(kappa * x, h) / j,
                h / kappa,
            )
            assert ratio >= lower * (1.0 - 1e-8)
            pair_ratios.append(ratio)
    return {
        "resolvent_integral_cases": len(resolvent_ratios),
        "max_exp_integral_formula_error": max(formula_errors),
        "resolvent_over_log_proxy_range": [min(resolvent_ratios), max(resolvent_ratios)],
        "joint_gap_outcome_cases": len(pair_ratios),
        "proved_joint_hellinger_over_J_lower_bound": lower,
        "observed_joint_hellinger_over_J_range": [min(pair_ratios), max(pair_ratios)],
    }


def check_crossover_and_duration() -> dict:
    inversion_ratios = []
    for n in (10, 1000, 1_000_000):
        for kappa in (1e-10, 1e-6, 0.001, 0.1, 2.0):
            proxy = 1.0 / n + math.sqrt(kappa / (n * math.log(2.0 + n * kappa)))
            at_proxy = n * poisson_j(proxy, kappa)
            assert 0.25 <= at_proxy <= 5.0
            root = brentq(lambda h: n * poisson_j(h, kappa) - 1.0, proxy / 6.0, 5.0 * proxy, xtol=1e-16, rtol=2e-14)
            assert proxy / 5.0 <= root <= 4.0 * proxy
            inversion_ratios.append(root / proxy)

    duration_errors = []
    marker_errors = []
    examples = []
    kappa, b, floor = 0.05, 1.0, 0.001
    for count in (40, 100, 1000, 10_000):
        pairs, n = count // 2, count - 1
        duration = n * kappa
        record = {"N": count}
        for label, short in (("doublet", b / count), ("floored", max(b / count, floor))):
            long = (duration - pairs * short) / (pairs - 1)
            duration_errors.append(abs(pairs * short + (pairs - 1) * long - duration))
            assert kappa - 1e-14 <= long <= 3.0 * kappa + 1e-14
            def information(h):
                return pairs * h * h / (short + h) + (pairs - 1) * h * h / (long + h)
            root = brentq(lambda h: information(h) - 1.0, 1e-15, 1.0, xtol=1e-15, rtol=2e-14)
            marker_errors.append(abs(information(root) - 1.0))
            record[f"h_{label}"] = root
        regular = (1.0 + math.sqrt(1.0 + 4.0 * n * kappa)) / (2.0 * n)
        record["h_regular"] = regular
        assert record["h_doublet"] <= regular + 1e-13
        assert record["h_doublet"] <= record["h_floored"] + 1e-13
        examples.append(record)
    assert max(duration_errors) < 1e-12
    assert max(marker_errors) < 1e-10
    return {
        "poisson_inversion_cases": len(inversion_ratios),
        "exact_root_over_uniform_proxy_range": [min(inversion_ratios), max(inversion_ratios)],
        "equal_duration_cases": 2 * len(examples),
        "max_dimensionless_duration_error": max(duration_errors),
        "max_information_marker_residual": max(marker_errors),
        "equal_duration_examples": examples,
    }


def main() -> None:
    warnings.simplefilter("error", IntegrationWarning)
    report = {
        "status": "passed",
        "scope": "Deterministic finite checks; no simulation or artifact writes; proofs establish uniform claims.",
        "pair_gaussian_integral": check_pair_integral(),
        "hellinger_bounds": check_hellinger_bounds(),
        "finite_tests": check_matching_and_finite_tests(),
        "poisson_integrals": check_poisson_integrals(),
        "timing_crossover": check_crossover_and_duration(),
    }
    print(json.dumps(report, indent=2, sort_keys=True, allow_nan=False))


if __name__ == "__main__":
    main()
