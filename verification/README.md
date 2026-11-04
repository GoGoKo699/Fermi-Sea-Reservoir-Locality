# Verification and reproduction

The universal range theorem is analytical. These finite calculations check the fragile parts of its realization and conventions: deleting samples next to polynomial roots, constructing positive filters, translating Majorana covariance into occupations, rounding tiny amplitudes, and evolving non-Gaussian initial states.

## Run the checks

Use Python 3.12 and the package versions in [requirements.txt](requirements.txt). The recorded run used Python 3.12.14.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r verification/requirements.txt
python verification/run_all.py
```

Run the commands from the repository root. The scripts resolve their output paths relative to their own files. The main runner returns a nonzero exit code on failure and writes [verification_summary.json](verification_summary.json) with a passing status only after every diagnostic satisfies its assertions.

| Script | What it checks | Recorded result |
|---|---|---|
| [check_filter_and_roots.py](check_filter_and_roots.py) | Sixteen ideal-filter cases; 212 root-potential cases, including roots on a sample, near a sample and outside the interval | All applicable filter and root bounds pass; largest retained root sum about 3.064, below $`\pi^2/2`$ |
| [check_covariance_conventions.py](check_covariance_conventions.py) | Direct finite-dimensional Lindblad derivatives for four three-mode states; Fourier occupation reconstruction for four paired six-mode Gaussian states | Maximum derivative residual below $`5.3\times10^{-16}`$; occupation residual below $`4.7\times10^{-16}`$ |
| [construction_resource_checks.py](construction_resource_checks.py) | Decimal coefficient construction and downward rounding at three sizes; direct six-mode fermionic Lindblad evolution from a non-Gaussian physical state and the complementary Fock state | All checked coefficient bounds pass; maximum dynamical residual below $`1.2\times10^{-15}`$ |
| [run_all.py](run_all.py) | Executes the preceding scripts and checks their numerical assertions together | Pass; detailed values in the summary JSON |

The individual records are [filter_and_root_results.json](filter_and_root_results.json), [covariance_conventions_results.json](covariance_conventions_results.json) and [construction_resource_checks.json](construction_resource_checks.json).

### What the state-evolution check establishes

The initial random pure state lies in an odd fermion-parity sector and is therefore a physical density matrix. Its occupation Wick residual is approximately $`-0.06825`$, so the tested state is not Gaussian. A direct Jordan–Wigner matrix representation evolves the full density matrix under the stated fermionic Lindbladian.

The result agrees with the independent occupation equations and with the exact target-population formula. A separate evolution of the complementary Fock state attains the predicted worst-case target fidelity. This tests the claim for arbitrary physical initial states without assuming that the full quantum channel factors into one-mode channels on coherences.

### What the precision check establishes

The three coefficient examples have $`N=66,258,1026`$ and use $`273,275,400`$ fractional bits, respectively. They test the normalized coefficient sums, amplitude perturbation, fidelity margins, rate perturbation and preparation-time bounds in the [construction](../science/reservoir_construction.md) and [resource account](../science/preparation_costs.md).

These calculations use high-precision decimal arithmetic. They are not interval certificates. The finite algorithm with certified coefficient enclosures is specified analytically in the construction page. For $`N=66`$, the formal radius exceeds half the ring length and periodization aliases coefficients; that case is a small-size diagnostic, not a claim of optimal finite-size range.

## Figures

Reproduce the tracked vector figure and its data with

```bash
python verification/make_figures.py
```

The script produces:

- [figures/accuracy_and_time.svg](figures/accuracy_and_time.svg), the tracked two-panel illustration;
- [figures/figure_data.json](figures/figure_data.json), the numerical values used in both panels;
- a local PNG preview, ignored by Git.

The first panel plots ideal stationary infidelity against radius $`m=s^2`$ at $`N=1026,4098,16386,65538`$. These samples vary the filter parameter directly rather than enforcing one fixed requested error. The second panel uses $`N=1026`$ and $`s=8`$. It compares the exact worst-case infidelity with the union bound, both evaluated using the actual ideal occupation rates.

Products are evaluated through logarithms, and tiny infidelities use stable exponential functions. This avoids subtracting a nearly unit floating-point fidelity from one and avoids evaluating cancellation-prone Fourier sums at ordinary precision. The figure uses ideal amplitudes; the separate rounding checks concern finite-precision realizations.

## Limits of the checks

The root samples do not prove the root integral or the discrete deletion lemma. Small matrix calculations do not establish the all-size Gaussian reduction. Decimal tests do not certify every rounded coefficient. The plots do not optimize over reservoirs. Those claims, where made, rely on the corresponding analytical arguments.

Floating-point residuals and last digits can vary with numerical libraries. The runner's $`10^{-11}`$ convention and dynamical tolerances leave substantial margin relative to the recorded residuals. No Liouvillian-gap equality is inferred from the occupation-rate checks.

Return to the [scientific model](../science/model.md) or the [repository overview](../README.md).

