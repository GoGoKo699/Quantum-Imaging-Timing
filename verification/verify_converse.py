"""Finite checks of the collective converse and the direct-imaging formulas.

These checks examine constants, fidelity conventions, and algebra. The uniform
theorems are established in science/, not by these finite examples.
"""

import json
import math

import numpy as np
from scipy.special import gammaln, roots_hermitenorm


def coherent_position(x, cutoff):
    """Fock coefficients of a vacuum translated in x by x; Var(x)=1/2."""
    alpha = x / np.sqrt(2)
    if alpha == 0:
        result = np.zeros(cutoff)
        result[0] = 1
        return result
    k = np.arange(cutoff)
    return (
        np.exp(-alpha * alpha / 2 + k * np.log(abs(alpha)) - gammaln(k + 1) / 2)
        * np.sign(alpha) ** k
    )


def gaussian_mixture(c, cutoff=64, quadrature_order=160):
    nodes, weights = roots_hermitenorm(quadrature_order)
    weights /= np.sqrt(2 * np.pi)
    vectors = np.array([coherent_position(np.sqrt(c) * x, cutoff) for x in nodes])
    return (vectors.T * weights) @ vectors


def root_fidelity(a, b):
    vals, vecs = np.linalg.eigh(a)
    square_root = (vecs * np.sqrt(np.maximum(vals, 0))) @ vecs.T
    vals = np.linalg.eigvalsh(square_root @ b @ square_root)
    return np.sqrt(np.maximum(vals, 0)).sum()


def main():
    rng = np.random.default_rng(20261029)
    precision_ratios = []
    for n in (1, 2, 3, 8, 30):
        for _ in range(30):
            v = 10.0 ** rng.uniform(-8, 3, n)
            difference = np.eye(n)
            if n > 1:
                difference[np.arange(1, n), np.arange(n - 1)] = -1
            precision = difference.T @ np.diag(1 / v) @ difference
            eigenvalues = np.linalg.eigvalsh(precision)
            # Positive definiteness can be within roundoff at these condition
            # numbers; a substantial negative value is an error, not clipped.
            assert eigenvalues.min() >= -1e-12 * np.linalg.norm(precision, 2)
            eigenvalues = np.maximum(eigenvalues, 0)
            for q in (1e-7, 1e-4, 0.01, 1.0):
                lhs = np.sum(eigenvalues / (1 + q * eigenvalues))
                rhs = 2 * np.sum(1 / (v + q))
                ratio = float(lhs / rhs)
                assert ratio <= 1 + 1e-7, (n, q, ratio)
                precision_ratios.append(ratio)

    cutoff = 16
    a = np.diag(np.sqrt(np.arange(1, cutoff)), 1)
    momentum = (a - a.T) / (1j * np.sqrt(2))
    derivative = np.zeros((cutoff, cutoff), complex)
    derivative[0, 0] = 1
    for _ in range(4):
        derivative = -1j * (momentum @ derivative - derivative @ momentum)
    commutator_norm = float(np.abs(np.linalg.eigvalsh(derivative)).sum())
    triangle_bound = math.sqrt(105) / 2 + 2 * math.sqrt(15) + 4.5
    assert commutator_norm < triangle_bound < 18

    binary_checks = []
    for q in (1e-5, 1e-4, 0.001, 0.01, 0.1):
        plus = coherent_position(np.sqrt(q), cutoff)
        minus = coherent_position(-np.sqrt(q), cutoff)
        binary = (np.outer(plus, plus) + np.outer(minus, minus)) / 2
        gaussian = gaussian_mixture(q, cutoff=cutoff, quadrature_order=100)
        distance = float(np.abs(np.linalg.eigvalsh(binary - gaussian)).sum() / 2)
        assert distance <= 1.5 * q * q + 1e-14
        binary_checks.append({"q": q, "half_trace_over_q_squared": distance / q**2})

    fidelity_checks = []
    for c, q in ((0, 0.03), (0.01, 0.002), (0.1, 0.03), (0.4, 0.1), (0.8, 0.03)):
        first, second = gaussian_mixture(c), gaussian_mixture(c + q)
        retained_trace_error = float(max(abs(np.trace(first) - 1), abs(np.trace(second) - 1)))
        numerical = float(root_fidelity(first, second))
        delta = np.arcsinh(np.sqrt(c + q)) - np.arcsinh(np.sqrt(c))
        analytic = float(1 / np.sqrt(np.cosh(delta)))
        error = abs(numerical - analytic)
        assert retained_trace_error < 1e-10
        assert error < 2e-8
        assert 1 - analytic <= q**2 / (4 * (c + q)) + 1e-14
        fidelity_checks.append({"c": c, "q": q, "absolute_root_fidelity_error": error})

    # Independent Gaussian quadrature verifies the classical likelihood and
    # fourth moment used in the all-processing direct-imaging comparison.
    nodes, weights = roots_hermitenorm(100)
    weights /= np.sqrt(2 * np.pi)
    direct_checks = []
    for q in (0.001, 0.03, 0.2):
        x = nodes / np.sqrt(2)
        ratio = np.exp(-q) * np.cosh(2 * np.sqrt(q) * x)
        chi_squared = float(np.dot(weights, (ratio - 1) ** 2))
        expected_chi_squared = float(2 * np.sinh(q) ** 2)
        assert abs(chi_squared - expected_chi_squared) < 1e-12
        for v in (0.001, 0.1, 1.0):
            noise_variance = 1 + v
            second_moment, fourth_moment = 0.0, 0.0
            for shift, probability in ((0, 0.5), (-2 * np.sqrt(q), 0.25), (2 * np.sqrt(q), 0.25)):
                y = np.sqrt(noise_variance) * nodes + shift
                second_moment += probability * np.dot(weights, y**2)
                fourth_moment += probability * np.dot(weights, y**4)
            variance = float(fourth_moment - second_moment**2)
            expected_variance = 2 * noise_variance**2 + 8 * noise_variance * q + 4 * q**2
            assert abs(second_moment - (noise_variance + 2 * q)) < 1e-12
            assert abs(variance - expected_variance) < 1e-10
            direct_checks.append({"q": q, "v": v, "fourth_moment_variance_error": abs(variance - expected_variance)})

    print(json.dumps({
        "precision_cases": len(precision_ratios),
        "precision_bound_max_ratio": max(precision_ratios),
        "fourth_commutator_trace_norm": commutator_norm,
        "fourth_commutator_triangle_bound": triangle_bound,
        "binary_to_gaussian": binary_checks,
        "gaussian_fidelity": fidelity_checks,
        "direct_imaging": direct_checks,
        "status": "passed",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
