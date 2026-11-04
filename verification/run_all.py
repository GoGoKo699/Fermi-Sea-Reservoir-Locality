"""Run the finite scientific checks and fail on any checked inequality.

These diagnostics test delicate finite conventions and realizations. They do
not prove the universal or asymptotic range theorem.
"""
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent


def run(name):
    result = subprocess.run([sys.executable, str(ROOT / name)],
                            capture_output=True, text=True)
    if result.returncode:
        sys.stderr.write(result.stdout + result.stderr)
        raise SystemExit(result.returncode)


def main():
    run("check_filter_and_roots.py")
    run("check_covariance_conventions.py")
    run("construction_resource_checks.py")
    filters = json.loads((ROOT / "filter_and_root_results.json").read_text())
    cov = json.loads((ROOT / "covariance_conventions_results.json").read_text())
    resources = json.loads((ROOT / "construction_resource_checks.json").read_text())
    occupations = filters["newman_occupations"]
    assert filters["root_kernel"]["all_bounds_hold"]
    assert all(c["sum_error_bound_holds_if_applicable"]
               and c["rate_lower_bound_holds"]
               and c["maximum_rate_bound_holds"] for c in occupations)
    assert max(cov["covariance_derivative_errors"]) < 1e-11
    assert max(c["max_occupation_error"]
               for c in cov["fourier_occupation_checks"]) < 1e-11
    assert all(c["all_asserted_bounds_hold"] for c in resources["coefficient_cases"])
    dynamics = resources["fermionic_arbitrary_state"]
    assert dynamics["all_formula_errors_below_1e_11"]
    assert dynamics["non_Gaussian_Wick_residual_above_1e_4"]
    summary = {
        "status": "pass",
        "scope": "Finite diagnostics, not an asymptotic proof or interval certificate.",
        "filter_cases": len(occupations),
        "root_cases": (filters["root_kernel"]["random_case_count"]
                       + len(filters["root_kernel"]["named_edge_cases"])),
        "largest_deleted_root_sum":
            filters["root_kernel"]["maximum_weighted_sum"],
        "root_integral_bound": 3.141592653589793**2 / 2,
        "covariance_derivative_cases": len(cov["covariance_derivative_errors"]),
        "maximum_covariance_residual": max(cov["covariance_derivative_errors"]),
        "fourier_occupation_cases": len(cov["fourier_occupation_checks"]),
        "maximum_occupation_residual":
            max(c["max_occupation_error"] for c in cov["fourier_occupation_checks"]),
        "coefficient_precision_cases": len(resources["coefficient_cases"]),
        "non_Gaussian_dynamics": dynamics,
    }
    (ROOT / "verification_summary.json").write_text(
        json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()

