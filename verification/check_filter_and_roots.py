"""Finite numerical checks for the Fermi-reservoir locality theorem.

These are diagnostics, not a substitute for the all-N proof. Rates are computed
as log products, including exact numerical zeros, to avoid underflow.
"""

import json
import math
from pathlib import Path

import numpy as np


def finite_number(value):
    value = float(value)
    return value if math.isfinite(value) else str(value)


def newman_case(n, s, epsilon=0.1):
    x = np.cos(2 * np.pi * np.arange(n) / n)
    log_plus = np.zeros(n)
    log_minus = np.zeros(n)
    log_p_one = 0.0
    with np.errstate(divide="ignore"):
        for j in range(s * s):
            root = math.exp(-j / s)
            log_plus += np.log(np.abs(x + root))
            log_minus += np.log(np.abs(root - x))
            log_p_one += math.log1p(root)
    gain = 2 * (log_plus - log_p_one) - math.log(2)
    loss = 2 * (log_minus - log_p_one) - math.log(2)
    log_rate = np.logaddexp(gain, loss)
    log_error = np.where(x > 0, loss, gain) - log_rate
    error = np.exp(log_error)
    with np.errstate(divide="ignore", invalid="raise"):
        log_fidelity = np.log1p(-error).sum()
    range_condition = math.exp(-(s * s - 1) / s) <= np.min(np.abs(x))
    log_error_sum_bound = math.log(n) + 2 * (s - 1) * math.log(math.tanh(0.5))
    log_rate_lower_bound = -math.log(2) - s**3 - s - 2
    return {
        "N": n,
        "s": s,
        "jump_radius_m": s * s,
        "sum_errors": finite_number(error.sum()),
        "log_fidelity": finite_number(log_fidelity),
        "minimum_log_rate_Gamma_1": finite_number(log_rate.min()),
        "maximum_log_rate_Gamma_1": finite_number(log_rate.max()),
        "minimum_abs_cosine": finite_number(np.min(np.abs(x))),
        "geometric_root_range_condition": bool(range_condition),
        "log_sum_error_bound_if_range_condition": log_error_sum_bound,
        "sum_error_bound_holds_if_applicable": bool(
            not range_condition or math.log(error.sum()) <= log_error_sum_bound + 1e-9
        ),
        "minimum_log_rate_lower_bound": log_rate_lower_bound,
        "rate_lower_bound_holds": bool(log_rate.min() >= log_rate_lower_bound - 1e-9),
        "maximum_rate_bound_holds": bool(log_rate.max() <= 1e-9),
    }


def kernel_cases(n=65538):
    # Include one additional endpoint for the weights and use precisely the
    # one-crossing tangent grid from the proposed proof.
    lo = math.ceil(n ** (2 / 3))
    hi = math.floor(n / 8)
    all_x = np.tan((np.arange(lo, hi + 2) + 0.5) * np.pi / n)
    x = all_x[:-1]
    weights = np.diff(np.log(all_x))
    assert np.all(np.diff(weights) <= 1e-14)
    middle = len(x) // 2
    test_roots = [
        ("real_at_node", complex(x[middle])),
        ("real_nextafter_node", complex(np.nextafter(x[middle], math.inf))),
        ("imaginary_distance_1e-300_from_node", complex(x[middle], 1e-300)),
        ("imaginary_distance_1e-14_from_node", complex(x[middle], 1e-14)),
        ("positive_real_between_nodes", complex(math.sqrt(x[middle] * x[middle + 1]))),
        ("complex_angle_small", x[middle] * np.exp(1e-6j)),
        ("complex_angle_quarter_pi", x[middle] * np.exp(0.25j * math.pi)),
        ("pure_imaginary", complex(0, x[middle])),
        ("negative_real", complex(-x[middle])),
        ("peak_below_grid", complex(x[0] / 100)),
        ("peak_above_grid", complex(x[-1] * 100)),
        ("zero", 0j),
    ]
    rng = np.random.default_rng(20261104)
    for i in range(200):
        radius = math.exp(rng.uniform(math.log(x[0]) - 3, math.log(x[-1]) + 3))
        angle = rng.uniform(-math.pi, math.pi)
        test_roots.append((f"random_{i}", radius * np.exp(1j * angle)))
    results = []
    for name, z in test_roots:
        # Remove nearest bracketing nodes. Peaks exactly at a node are removed,
        # as are zero values even in the presence of machine-level rounding.
        insertion = np.searchsorted(x, abs(z), side="left")
        deleted = {int(j) for j in (insertion - 1, insertion) if 0 <= j < len(x)}
        mask = np.ones(len(x), dtype=bool)
        for j in deleted:
            mask[j] = False
        with np.errstate(divide="ignore", invalid="ignore"):
            h = np.abs(np.log(np.abs(x + z)) - np.log(np.abs(x - z)))
        weighted_sum = float(np.sum(weights[mask] * h[mask]))
        results.append({
            "name": name,
            "root_real": float(z.real),
            "root_imag": float(z.imag),
            "deleted_indices": sorted(j + lo for j in deleted),
            "weighted_sum_after_deletion": finite_number(weighted_sum),
            "pi_squared_over_two": math.pi**2 / 2,
            "bound_holds": math.isfinite(weighted_sum) and weighted_sum <= math.pi**2 / 2 + 1e-10,
            "unremoved_max_kernel": finite_number(np.max(h)),
        })
    return {
        "N": n,
        "j_range": [lo, hi],
        "total_weight": float(weights.sum()),
        "maximum_weight": float(weights.max()),
        "weights_nonincreasing": bool(np.all(np.diff(weights) <= 1e-14)),
        "all_bounds_hold": all(r["bound_holds"] for r in results),
        "maximum_weighted_sum": max(r["weighted_sum_after_deletion"] for r in results),
        "named_edge_cases": results[:12],
        "random_case_count": len(results) - 12,
        "random_cases": results[12:],
    }


def main():
    occupations = []
    for n in (1026, 4098, 16386, 65538):
        ss = sorted({math.ceil(0.5 * math.log(n)), math.ceil(math.log(n)),
                     math.ceil(1.5 * math.log(n)), math.ceil(2 * math.log(2 * n / 0.1) + 4)})
        occupations.extend(newman_case(n, s) for s in ss)
    data = {
        "purpose": "Numerical convention and spike diagnostics only; no universal theorem established by sampling.",
        "fidelity_convention": "F = target pure-state overlap, product(1-error_k); natural logarithms.",
        "rates": "Gamma=1; log rates retained to avoid underflow.",
        "newman_occupations": occupations,
        "root_kernel": kernel_cases(),
    }
    destination = Path(__file__).with_name("filter_and_root_results.json")
    destination.write_text(json.dumps(data, indent=2) + "\n")
    print(json.dumps({
        "destination": str(destination),
        "newman_occupations": occupations,
        "root_kernel_summary": {k: v for k, v in data["root_kernel"].items() if k not in ("named_edge_cases", "random_cases")},
        "root_kernel_named_edges": data["root_kernel"]["named_edge_cases"],
    }, indent=2))


if __name__ == "__main__":
    main()
