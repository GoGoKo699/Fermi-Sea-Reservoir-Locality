"""Focused checks of finite-precision filters and arbitrary-state preparation.

Decimal arithmetic is used to avoid near-Fermi cancellation in Fourier sums.
This is a high-precision diagnostic, not an interval-arithmetic certificate.
The mathematical interval prescription is in science/reservoir_construction.md.
"""

from decimal import Decimal as D, ROUND_CEILING, ROUND_FLOOR, localcontext
import json
import math
from pathlib import Path

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import expm_multiply


def decimal_pi():
    def atan_inverse(q):
        x = D(1) / q
        power = x
        value = D(0)
        j = 0
        while True:
            term = power / (2 * j + 1)
            new = value + term if j % 2 == 0 else value - term
            if new == value:
                return value
            value = new
            power *= x * x
            j += 1
    return 16 * atan_inverse(D(5)) - 4 * atan_inverse(D(239))


def decimal_cos(x):
    term = D(1)
    value = term
    j = 1
    while True:
        term *= -x * x / ((2 * j - 1) * (2 * j))
        new = value + term
        if new == value:
            return value
        value = new
        j += 1


def chebyshev_eval(coeff, x):
    m = (len(coeff) - 1) // 2
    value = coeff[m]
    previous, current = D(1), x
    for r in range(1, m + 1):
        value += 2 * coeff[m + r] * current
        previous, current = current, 2 * x * current - previous
    return value


def log_one_minus_exp_minus_exp(z):
    # log(1-exp(-exp(z))), including both cancellation-prone tails.
    if z < -36:
        return z - math.exp(z) / 2
    if z > 7:
        return 0.0
    return math.log(-math.expm1(-math.exp(z)))


def exact_log_worst_time(log_rates, log_stationary_fidelity, epsilon):
    target = math.log1p(-epsilon)
    lower = -min(log_rates) - 50
    upper = -min(log_rates) + math.log(math.log(2 * len(log_rates) / epsilon)) + 1

    def log_fidelity(log_time):
        return log_stationary_fidelity + sum(
            log_one_minus_exp_minus_exp(rate + log_time) for rate in log_rates
        )

    assert log_fidelity(lower) < target < log_fidelity(upper)
    for _ in range(100):
        middle = (lower + upper) / 2
        if log_fidelity(middle) < target:
            lower = middle
        else:
            upper = middle
    return (lower + upper) / 2


def coefficient_case(n, epsilon_string="0.1"):
    epsilon = float(epsilon_string)
    kappa = -math.log(math.tanh(0.5))
    s = math.ceil(max(2, math.log(n / 2) + 1,
                      1 + math.log(4 * n / epsilon) / (2 * kappa)))
    m = s * s
    count = 2 * m + 1
    b_estimate = math.ceil((s**3 + s + 2) / (2 * math.log(2))
                           + math.log2(4 * math.sqrt(2) * count * n / epsilon))
    digits = math.ceil(b_estimate * math.log10(2)) + 65
    with localcontext() as ctx:
        ctx.prec = digits
        eps = D(epsilon_string)
        u = (-(D(s**3 + s + 2) / 2)).exp()
        b = int(((D(s**3 + s + 2) / 2 +
                   (4 * D(2).sqrt() * count * n / eps).ln()) / D(2).ln())
                .to_integral_value(rounding=ROUND_CEILING))
        grid = D(2) ** b
        roots = [(-D(j) / s).exp() for j in range(m)]
        coeff = [D(1)]
        for root in roots:
            middle_probability = root / (1 + root)
            side_probability = 1 / (2 * (1 + root))
            updated = [D(0)] * (len(coeff) + 2)
            for j, value in enumerate(coeff):
                updated[j] += side_probability * value
                updated[j + 1] += middle_probability * value
                updated[j + 2] += side_probability * value
            # Enforce the exact mathematical reflection symmetry.
            for j in range(len(updated) // 2):
                averaged = (updated[j] + updated[-j - 1]) / 2
                updated[j] = updated[-j - 1] = averaged
            coeff = updated
        rounded = [(value * grid).to_integral_value(rounding=ROUND_FLOOR) / grid
                   for value in coeff]
        l1_error = sum(a - b for a, b in zip(coeff, rounded))
        p_one = D(1)
        for root in roots:
            p_one *= 1 + root
        pi = decimal_pi()
        errors = []
        log_rates = []
        ideal_log_rates = []
        maximum_occupation_change = D(0)
        minimum_rate_ratio = D("Infinity")
        maximum_rate_ratio = D(0)
        maximum_amplitude_error = D(0)
        for k in range(n):
            angle = 2 * pi * min(k, n - k) / n
            x = decimal_cos(angle)
            positive = D(1)
            negative = D(1)
            for root in roots:
                positive *= x + root
                negative *= -x + root
            positive /= p_one
            negative /= p_one
            rounded_positive = chebyshev_eval(rounded, x)
            rounded_negative = chebyshev_eval(rounded, -x)
            ideal_denominator = positive**2 + negative**2
            rounded_denominator = rounded_positive**2 + rounded_negative**2
            ideal_occupation = positive**2 / ideal_denominator
            rounded_occupation = rounded_positive**2 / rounded_denominator
            maximum_occupation_change = max(maximum_occupation_change,
                                             abs(rounded_occupation - ideal_occupation))
            ratio = rounded_denominator / ideal_denominator
            minimum_rate_ratio = min(minimum_rate_ratio, ratio)
            maximum_rate_ratio = max(maximum_rate_ratio, ratio)
            maximum_amplitude_error = max(maximum_amplitude_error,
                abs(positive - rounded_positive), abs(negative - rounded_negative))
            errors.append(1 - rounded_occupation if x > 0 else rounded_occupation)
            log_rates.append(float((rounded_denominator / 2).ln()))
            ideal_log_rates.append(float((ideal_denominator / 2).ln()))
        log_fidelity = sum((1 - error).ln() for error in errors)
        nu = eps / (4 * n)
        log_exact_time = exact_log_worst_time(log_rates, float(log_fidelity), epsilon)
        return {
            "N": n, "epsilon": epsilon_string, "s": s, "radius": m,
            "fractional_bits_b": b, "decimal_working_digits": digits,
            "normalized_coefficient_sum": str(sum(coeff)),
            "rounded_coefficient_sum": str(sum(rounded)),
            "coefficient_l1_error": str(l1_error),
            "amplitude_error_bound": str(count / grid),
            "observed_maximum_amplitude_error": str(maximum_amplitude_error),
            "maximum_occupation_change": str(maximum_occupation_change),
            "occupation_change_bound": str(eps / (4 * n)),
            "minimum_observed_rate_ratio": str(minimum_rate_ratio),
            "maximum_observed_rate_ratio": str(maximum_rate_ratio),
            "rate_ratio_lower_bound": str((1 - nu)**2),
            "rate_ratio_upper_bound": str((1 + nu)**2),
            "rounded_error_sum": str(sum(errors)),
            "rounded_log_fidelity": str(log_fidelity),
            "ideal_minimum_log_rate_Gamma_1": min(ideal_log_rates),
            "rounded_minimum_log_rate_Gamma_1": min(log_rates),
            "rounded_maximum_log_rate_Gamma_1": max(log_rates),
            "exact_worst_case_log_Gamma_t": log_exact_time,
            "actual_rate_union_bound_log_Gamma_t": -min(log_rates) + math.log(math.log(2*n/epsilon)),
            "proof_rate_bound_log_Gamma_t": math.log(4) + s**3+s+2 + math.log(math.log(2*n/epsilon)),
            "all_asserted_bounds_hold": bool(
                sum(rounded) <= 1 and sum(errors) <= eps/2
                and maximum_occupation_change <= eps/(4*n)
                and minimum_rate_ratio >= (1-nu)**2
                and maximum_rate_ratio <= (1+nu)**2
                and maximum_amplitude_error <= count/grid
            ),
        }


def annihilator(n, k):
    dimension = 1 << n
    rows, cols, values = [], [], []
    for basis in range(dimension):
        if basis & (1 << k):
            rows.append(basis ^ (1 << k))
            cols.append(basis)
            values.append(-1 if (basis & ((1 << k) - 1)).bit_count() % 2 else 1)
    return sparse.csr_matrix((values, (rows, cols)), shape=(dimension, dimension), dtype=complex)


def arbitrary_state_case():
    n = 6
    dimension = 1 << n
    target_bits = np.cos(2*np.pi*np.arange(n)/n) > 0
    target = sum((1 << k) for k in range(n) if target_bits[k])
    complement = (dimension - 1) ^ target
    rates = np.array([0.7, 1.0, 1.2, 1.7, 2.2, 0.9])
    stationary_errors = np.array([0.07, 0.12, 0.11, 0.09, 0.10, 0.08])
    occupations = np.where(target_bits, 1-stationary_errors, stationary_errors)
    gains, losses = rates*occupations, rates*(1-occupations)
    bits = ((np.arange(dimension)[:,None] >> np.arange(n)) & 1)
    energies = bits @ np.array([1.3, -0.7, 0.2, 0.8, -0.4, 1.1])
    hamiltonian = sparse.diags(energies, format="csr")
    identity = sparse.eye(dimension, format="csr")
    generator = -1j * (sparse.kron(identity, hamiltonian)
                        - sparse.kron(hamiltonian.T, identity))
    annihilators = [annihilator(n,k) for k in range(n)]
    for k, op in enumerate(annihilators):
        for jump in (math.sqrt(losses[k])*op, math.sqrt(gains[k])*op.conj().T):
            square = jump.conj().T @ jump
            generator += (sparse.kron(jump.conj(), jump)
                          - 0.5*sparse.kron(identity, square)
                          - 0.5*sparse.kron(square.T, identity))
    generator = generator.tocsr()
    rng = np.random.default_rng(20261104)
    state = rng.normal(size=dimension) + 1j*rng.normal(size=dimension)
    state[np.sum(bits, axis=1) % 2 == 0] = 0  # Definite odd parity: physical.
    state /= np.linalg.norm(state)
    rho = np.outer(state, state.conj())
    rho_complement = np.zeros((dimension,dimension), complex)
    rho_complement[complement,complement] = 1
    time = 3.7
    evolved = expm_multiply(time*generator,
        np.column_stack([rho.reshape(-1,order="F"),rho_complement.reshape(-1,order="F")]))
    final_random = evolved[:,0].reshape((dimension,dimension),order="F")
    final_complement = evolved[:,1].reshape((dimension,dimension),order="F")
    initial_populations = np.abs(state)**2
    initial_occupations = initial_populations @ bits
    predicted_occupations = occupations + (initial_occupations-occupations)*np.exp(-rates*time)
    evolved_occupations = np.real(np.diag(final_random)) @ bits
    correct = 1-stationary_errors + stationary_errors*np.exp(-rates*time)
    wrong = (1-stationary_errors)*(1-np.exp(-rates*time))
    target_effect_diagonal = np.prod(np.where(bits == target_bits, correct, wrong),axis=1)
    predicted_random_fidelity = initial_populations @ target_effect_diagonal
    predicted_minimum_fidelity = np.prod(wrong)
    def expectation(op):
        return np.vdot(state, op @ state)
    c01 = expectation(annihilators[0].conj().T @ annihilators[1])
    f01 = expectation(annihilators[0] @ annihilators[1])
    pair_population = initial_populations @ (bits[:,0]*bits[:,1])
    wick_residual = pair_population - initial_occupations[0]*initial_occupations[1] + abs(c01)**2 - abs(f01)**2
    errors = [
        float(np.max(np.abs(evolved_occupations-predicted_occupations))),
        float(abs(final_random[target,target]-predicted_random_fidelity)),
        float(abs(final_complement[target,target]-predicted_minimum_fidelity)),
    ]
    return {
        "N": n, "time": time, "Lindblad_convention": "D[L]=L rho Ldagger - anticommutator/2",
        "initial_state": "Seeded random pure state of odd fermion parity",
        "initial_Wick_residual_modes_0_1": float(wick_residual),
        "random_state_target_fidelity_evolved": float(final_random[target,target].real),
        "random_state_target_fidelity_diagonal_formula": float(predicted_random_fidelity),
        "complement_target_fidelity_evolved": float(final_complement[target,target].real),
        "exact_worst_case_formula": float(predicted_minimum_fidelity),
        "maximum_occupation_equation_error": errors[0],
        "random_fidelity_formula_error": errors[1],
        "worst_case_fidelity_formula_error": errors[2],
        "all_formula_errors_below_1e_11": max(errors)<1e-11,
        "non_Gaussian_Wick_residual_above_1e_4": bool(abs(wick_residual)>1e-4),
    }


def main():
    result = {
        "purpose": "Focused finite-precision cancellation and arbitrary-initial-state checks; not a proof by sampling.",
        "coefficient_diagnostic_uses_interval_certification": False,
        "coefficient_cases": [coefficient_case(n) for n in (66,258,1026)],
        "fermionic_arbitrary_state": arbitrary_state_case(),
    }
    destination = Path(__file__).with_name("construction_resource_checks.json")
    destination.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({
        "destination":str(destination),
        "coefficient_cases":[{k:r[k] for k in (
            "N","s","radius","fractional_bits_b","all_asserted_bounds_hold",
            "rounded_error_sum","maximum_occupation_change",
            "exact_worst_case_log_Gamma_t","actual_rate_union_bound_log_Gamma_t",
            "proof_rate_bound_log_Gamma_t")} for r in result["coefficient_cases"]],
        "fermionic_arbitrary_state":result["fermionic_arbitrary_state"],
    },indent=2))


if __name__=="__main__":
    main()
