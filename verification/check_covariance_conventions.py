"""Exact finite-Fock-space checks of the conventions in science/gaussian_stationarity.md.

These checks diagnose factors and Fourier signs; they do not replace the proof.
"""

import json
from pathlib import Path

import numpy as np
from scipy.linalg import expm


def annihilators(n):
    identity = np.eye(2, dtype=complex)
    parity = np.diag([1, -1]).astype(complex)
    lowering = np.array([[0, 1], [0, 0]], dtype=complex)
    result = []
    for j in range(n):
        operator = np.array([[1]], dtype=complex)
        for site in range(n):
            factor = parity if site < j else lowering if site == j else identity
            operator = np.kron(operator, factor)
        result.append(operator)
    return np.array(result)


def majoranas(c):
    return np.stack([part for mode in c for part in
                     (mode + mode.conj().T, -1j * (mode - mode.conj().T))])


def covariance(w, rho):
    second = np.einsum("aij,bjk,ki->ab", w, w, rho, optimize=True)
    return 1j * (second - np.eye(len(w)) * np.trace(rho))


def hamiltonian(w, h):
    return 0.25j * np.einsum("ab,aij,bjk->ik", h, w, w, optimize=True)


def derivative_check(seed):
    rng = np.random.default_rng(seed)
    n = 3
    c = annihilators(n)
    w = majoranas(c)
    raw_h = rng.normal(size=(2*n, 2*n))
    h = (raw_h - raw_h.T) / 3
    ell = rng.normal(size=(5, 2*n)) + 1j*rng.normal(size=(5, 2*n))
    ell /= 5
    m = ell.T @ ell.conj()
    x = h - 2*m.real
    y = 4*m.imag
    raw = rng.normal(size=(2**n, 2**n)) + 1j*rng.normal(size=(2**n, 2**n))
    rho = raw @ raw.conj().T
    parity = np.diag([(-1)**i.bit_count() for i in range(2**n)])
    rho = (rho + parity @ rho @ parity) / 2
    rho /= np.trace(rho)
    hh = hamiltonian(w, h)
    derivative = -1j * (hh @ rho - rho @ hh)
    for coeff in ell:
        jump = np.einsum("a,aij->ij", coeff, w)
        norm = jump.conj().T @ jump
        derivative += jump @ rho @ jump.conj().T - (norm @ rho + rho @ norm)/2
    gamma = covariance(w, rho)
    direct = covariance(w, derivative)
    predicted = x @ gamma + gamma @ x.T + y
    return float(np.max(np.abs(direct-predicted)))


def occupation_check(seed):
    rng = np.random.default_rng(seed)
    n = 6
    c = annihilators(n)
    w = majoranas(c)
    onsite = rng.normal(size=(2, 2))
    onsite = onsite-onsite.T
    neighbor = rng.normal(size=(2, 2))
    h = np.zeros((2*n, 2*n))
    for site in range(n):
        here = slice(2*site, 2*site+2)
        nxt = slice(2*((site+1) % n), 2*((site+1) % n)+2)
        h[here, here] += onsite
        h[here, nxt] += neighbor
        h[nxt, here] -= neighbor.T
    hh = hamiltonian(w, h)
    rho = expm(-0.4*hh)
    rho /= np.trace(rho)
    gamma = covariance(w, rho)
    kernel = np.stack([gamma[2*r:2*r+2, :2] for r in range(n)])
    errors = []
    trace_term_sizes = []
    for k in 2*np.pi*np.arange(n)/n:
        symbol = np.einsum("r,rab->ab", np.exp(-1j*k*np.arange(n)), kernel)
        occupation = 0.5+(symbol[0, 1]-symbol[1, 0]+1j*np.trace(symbol))/4
        mode = np.einsum("r,rij->ij", np.exp(-1j*k*np.arange(n))/np.sqrt(n), c)
        direct = np.trace(rho @ mode.conj().T @ mode)
        errors.append(abs(direct-occupation))
        trace_term_sizes.append(abs(1j*np.trace(symbol)/4))
    return {"max_occupation_error": float(max(errors)),
            "largest_trace_term": float(max(trace_term_sizes))}


if __name__ == "__main__":
    results = {"covariance_derivative_errors": [derivative_check(s) for s in range(4)],
               "fourier_occupation_checks": [occupation_check(s) for s in range(4)]}
    assert max(results["covariance_derivative_errors"]) < 1e-11
    assert max(r["max_occupation_error"] for r in results["fourier_occupation_checks"]) < 1e-11
    path = Path(__file__).with_name("covariance_conventions_results.json")
    path.write_text(json.dumps(results, indent=2)+"\n")
    print(json.dumps(results, indent=2))
