"""Finite independent checks of the joint timing, jitter and calibration model.

Quadrature checks spatial-mode probabilities; exact factorial moments check
the heterogeneous receiver variance. Matrix and scalar examples exercise the
converse and crossover formulas. These finite checks do not prove uniformity.
"""
import json
import math
from decimal import Decimal, localcontext

import numpy as np
from numpy.polynomial.hermite import hermgauss
from scipy.optimize import brentq
from scipy.stats import poisson


def require(ok, label):
    if not ok:
        raise AssertionError(label)


def even_moment(q, r, k):
    ans = np.zeros_like(r)
    for j in range(k + 1):
        gaussian = math.prod(range(1, 2*j, 2))*r**j if j else np.ones_like(r)
        power = 2*(k-j)
        source = 1. if power == 0 else .5*(2*q)**(power/2)
        ans += math.comb(2*k, 2*j)*gaussian*source
    return ans


def moments(q, w, d):
    f = [np.ones_like(d)] + [even_moment(q, w+d, k)/2**k for k in range(1, 5)]
    var_q = f[2]+f[1]-f[1]**2
    cov_q_f2 = f[3]+2*f[2]-f[1]*f[2]
    var_f2 = f[4]+4*f[3]+2*f[2]-f[2]**2
    a, beta = 4/3, -4*d
    return (2*f[1]-d, a*f[2]+beta*f[1]+d*d,
            4*var_q, a*a*var_f2+beta*beta*var_q+2*a*beta*cov_q_f2,
            2*a*cov_q_f2+2*beta*var_q)


def receiver_checks():
    nodes, weights = hermgauss(96)
    weights /= math.sqrt(math.pi)
    indices = np.arange(180)
    residuals = []
    for q in (0., 1e-6, .001, .02, .2):
      for w in (0., 1e-6, .001, .05, .3):
       for delta in (0., 1e-5, .01, .1):
        r, d = w+delta/2, delta/2
        p = np.zeros(len(indices))
        for shift, mass in ((0., .5), (math.sqrt(2*q), .25), (-math.sqrt(2*q), .25)):
            a = math.sqrt(2*r)*nodes+shift
            p += mass*(weights[:, None]*poisson.pmf(indices[None, :], a[:, None]**2/2)).sum(axis=0)
        y = 2*indices-d
        z = (4/3)*indices*(indices-1)-4*d*indices+d*d
        ey, ez, vy, vz, cyz = moments(q, w, np.asarray(d))
        swap = (1-(1+2*r)**-.5*(1+math.exp(-2*q/(1+2*r)))/2)/2
        err = max(abs(p.sum()-1), abs(p@y-ey), abs(p@z-ez),
                  abs(p@(y-ey)**2-vy), abs(p@(z-ez)**2-vz),
                  abs(p@((y-ey)*(z-ez))-cyz), abs(p[1::2].sum()-swap))
        require(err < 2e-10, 'HG quadrature/moment/SWAP disagreement')
        residuals.append(float(err))
    return {'cases': len(residuals), 'maximum_absolute_error': max(residuals),
            'HG_modes_retained': len(indices), 'quadrature_nodes': len(nodes)}


def covariance_checks():
    rng = np.random.default_rng(20261102)
    eigenvalues, ratios = [], []
    for n in (2, 3, 8, 32, 96):
      for trial in range(12):
        u = np.r_[1., 10**rng.uniform(-8, 0, n-1)]
        if trial == 0: u[1:] = 1.
        if trial == 1: u[1:] = 1e-8
        nxt = np.r_[u[1:], np.inf]
        c = 1/(2*(1/u+1/nxt))
        C = np.minimum.outer(np.cumsum(u), np.cumsum(u))
        value = float(np.linalg.eigvalsh(C-np.diag(c))[0])
        require(value >= -1e-12, 'diagonal covariance extraction')
        eigenvalues.append(value)
        for b in (0., 1e-7, .001, .1):
          for power in (1, 2):
            ratio = float(np.sum((b+c)**-power)/np.sum((b+u[1:])**-power))
            require(.25 <= ratio <= 2*4**power+2, 'extracted/gap sum comparison')
            ratios.append(ratio)
    return {'matrix_cases': len(eigenvalues), 'smallest_difference_eigenvalue': min(eigenvalues),
            'weighted_sum_cases': len(ratios), 'weighted_sum_ratio_range': [min(ratios), max(ratios)]}


def weighted_variance(q, w, b, d):
    ey, ez, vy, vz, cyz = moments(q, w, d)
    raw = (b+d)**-2
    S = raw.sum()
    lam = raw/S
    D = 1-lam@lam
    mu = w+q
    ci = 2*mu*lam*(1-lam)/D
    linear = np.sum(lam*lam*vz+ci*ci*vy-2*lam*ci*cyz)
    av = lam*lam*vy
    degenerate = 2*(av.sum()**2-av@av)/(D*D)
    tau = S**-.25
    require(np.max(np.abs(ey-mu)) < 1e-12, 'heterogeneous second moment')
    require(np.max(np.abs(ez-(mu*mu-q*q/3))) < 1e-12, 'heterogeneous fourth moment')
    return float(linear+degenerate), float(tau), float(D)


def shape_checks():
    rng = np.random.default_rng(713)
    rows = []
    for b, n in ((.01, 50000), (.03, 20000), (.1, 5000)):
      for kind in ('close', 'heterogeneous', 'mixed'):
        d = np.full(n, 1/(2*n))
        if kind == 'heterogeneous': d = 10**rng.uniform(-8, -.3, n)
        if kind == 'mixed': d[::5] = .3
        for q in (0., .5*b, b, .1, .25):
            variance, tau, normalizer = weighted_variance(q, .5*b, b, d)
            if tau > b: continue
            ratio = variance/(tau**4+q*q*tau*tau)
            require(0 <= ratio < 200, 'global shape variance envelope')
            rows.append({'b': b, 'q': q, 'n': n, 'gaps': kind,
                         'normalized_variance': ratio, 'cross_product_normalizer': normalizer})
    # Directly enumerate small independent HG records to check the complete
    # weighted statistic, including covariance and its cross-product divisor.
    enum_errors = []
    nodes, quad_weights = hermgauss(80)
    quad_weights /= math.sqrt(math.pi)
    mode_indices = np.arange(16)
    for d in (np.asarray([0., .02]), np.asarray([0., .001, .02])):
        q, w, b = .02, .01, .03
        distributions = []
        for gap in d:
            p = np.zeros(len(mode_indices))
            for shift, mass in ((0., .5), (math.sqrt(2*q), .25), (-math.sqrt(2*q), .25)):
                a = math.sqrt(2*(w+gap))*nodes+shift
                p += mass*(quad_weights[:, None]*poisson.pmf(mode_indices[None, :], a[:, None]**2/2)).sum(axis=0)
            distributions.append(p)
        grids = np.meshgrid(*([mode_indices]*len(d)), indexing='ij')
        mass = np.ones_like(grids[0], dtype=float)
        raw = (b+d)**-2
        lam = raw/raw.sum()
        ybar, zbar, diagonal = np.zeros_like(mass), np.zeros_like(mass), np.zeros_like(mass)
        for i, grid in enumerate(grids):
            mass *= distributions[i][grid]
            y = 2*grid-d[i]
            z = (4/3)*grid*(grid-1)-4*d[i]*grid+d[i]**2
            ybar += lam[i]*y
            zbar += lam[i]*z
            diagonal += lam[i]**2*y*y
        T = zbar-(ybar*ybar-diagonal)/(1-lam@lam)
        mean = float(np.sum(mass*T))
        variance = float(np.sum(mass*(T+q*q/3)**2))
        predicted, _, _ = weighted_variance(q, w, b, d)
        error = max(abs(mass.sum()-1), abs(mean+q*q/3), abs(variance-predicted))
        require(error < 1e-11, 'complete weighted HG enumeration')
        enum_errors.append(error)
    return {'active_cases': len(rows), 'maximum_q_over_b': max(z['q']/z['b'] for z in rows),
            'maximum_normalized_variance': max(z['normalized_variance'] for z in rows),
            'minimum_cross_product_normalizer': min(z['cross_product_normalizer'] for z in rows),
            'complete_record_enumeration_cases': len(enum_errors),
            'maximum_enumeration_error': max(enum_errors),
            'cases': rows}


def collision_checks():
    nodes, weights = hermgauss(96)
    weights /= math.sqrt(math.pi)
    errors, scaled = [], []
    for b in (.02, .1, .3):
      for c in (.001, .02, .2):
        q, u, v = .2*b, .5, c+b/2
        v1 = v-q
        require(v1 >= 0, 'admissible compensated variance')
        ell = math.sqrt(v*(u+v))
        z = q/ell
        exact = (math.exp(z/(1+z))+math.exp(-z/(1-z)))/(2*math.sqrt(1-z*z))
        integral = 0.
        for sign_x in (-1, 1):
          for sign_y in (-1, 1):
            x = math.sqrt(2*v1)*nodes+sign_x*math.sqrt(q)
            y = math.sqrt(2*v1)*nodes+sign_y*math.sqrt(q)
            kernel = math.sqrt(1+v/u)*np.exp(-(x[:, None]**2+y[None, :]**2)/(2*u)
                       +math.sqrt((u+v)/v)/u*x[:, None]*y[None, :])
            integral += .25*float(weights@kernel@weights)
        errors.append(abs(integral-exact))
        require(errors[-1] < 2e-10, 'heterogeneous collision kernel quadrature')
        # High precision preserves the small compensated quartic divergence.
        with localcontext() as ctx:
            ctx.prec = 65
            zd = Decimal(str(q))/(Decimal(str(v))*(Decimal('.5')+Decimal(str(v)))).sqrt()
            one = Decimal(1)
            F = ((zd/(one+zd)).exp()+(-zd/(one-zd)).exp())/(2*(one-zd*zd).sqrt())
            ratio = float((F-one)/zd**4)
        require(0 <= ratio <= 200, 'quartic compensated collision bound')
        scaled.append(ratio)
    return {'cases': len(errors), 'maximum_kernel_quadrature_error': max(errors),
            'chi_squared_over_z_fourth_range': [min(scaled), max(scaled)]}


def timing_root(n, b, internal, external):
    def info(q):
        return n*q*q/(b+internal+q)+(n-1)*q*q/(b+external+q)
    return brentq(lambda q: info(q)-1, 1e-16, 10., xtol=1e-15)


def schedule_checks():
    ratios, floors = [], []
    for N in (1000, 10000, 100000):
      n = N//2
      for b in (0., 1e-6, .001, .1):
       r0 = timing_root(n, b, 1/N, 1.)
       S2 = n/(b+1/N)**2+(n-1)/(b+1.)**2
       for M in (0, 10, N, math.inf):
        K = N if math.isinf(M) else (N*M/(N+M) if M else 0.)
        static = 1/N+min(b, math.sqrt(b/max(math.sqrt(N), K)))
        nuisance = 0. if not b else min(b, math.sqrt(b/M) if M else math.inf, S2**-.25)
        joint = r0+nuisance
        ratio = joint/static
        require(.2 < ratio < 8, 'close-doublet reduction')
        ratios.append(ratio)
       if b:
        floors.append({'N': N, 'b': b, 'perfect_calibration_floor': r0,
                       'zero_jitter_floor': timing_root(n, 0., 1/N, 1.)})
        raw_nuisance = min(b, S2**-.25)
        Mcross = max(1/b, b*math.sqrt(S2))
        require(math.isclose(math.sqrt(b/Mcross), raw_nuisance, rel_tol=1e-12), 'calibration crossover')
    return {'close_doublet_cases': len(ratios), 'joint_to_static_order_ratio': [min(ratios), max(ratios)],
            'physical_jitter_examples': floors}


def main():
    print(json.dumps({'status': 'passed', 'purpose': 'finite identities and regression checks; not a uniform theorem proof',
                      'relative_modes': receiver_checks(), 'covariance_extraction': covariance_checks(),
                      'weighted_shape': shape_checks(), 'collision_substitution': collision_checks(),
                      'schedule_endpoints': schedule_checks()}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
