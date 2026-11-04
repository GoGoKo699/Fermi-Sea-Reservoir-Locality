"""Reproduce the ideal-filter illustrations, using stable log products."""
import json
import math
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "figures"
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 10,
    "axes.spines.top": False, "axes.spines.right": False,
    "svg.hashsalt": "fermi-sea-reservoir-locality",
})


def filter_data(n, s):
    x = np.abs(np.cos(2*np.pi*np.arange(n)/n))
    plus = np.zeros(n)
    minus = np.zeros(n)
    norm = 0.0
    with np.errstate(divide="ignore"):
        for j in range(s*s):
            root = math.exp(-j/s)
            plus += np.log(x+root)
            minus += np.log(np.abs(x-root))
            norm += math.log1p(root)
    contrast = 2*(minus-plus)
    log_fidelity = -float(np.logaddexp(0, contrast).sum())
    error = np.exp(contrast-np.logaddexp(0, contrast))
    log_rate = np.logaddexp(2*(plus-norm), 2*(minus-norm))-math.log(2)
    return {
        "N": n, "s": s, "radius": s*s,
        "infidelity": -math.expm1(log_fidelity),
        "log_fidelity": log_fidelity,
        "error_sum": float(error.sum()),
        "log_minimum_rate_over_Gamma": float(log_rate.min()),
        "log_rates": log_rate,
    }


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    colors = ["#1d4e89", "#138a8a", "#9a5b16", "#913c74"]
    figure, axes = plt.subplots(1, 2, figsize=(11.2, 4.35))
    stationary = []
    for n, color in zip([1026, 4098, 16386, 65538], colors):
        rows = [filter_data(n, s) for s in range(2, 17)]
        stationary.extend([{k:v for k,v in r.items() if k!="log_rates"}
                           for r in rows])
        axes[0].semilogy([r["radius"] for r in rows],
                         [r["infidelity"] for r in rows],
                         marker="o", markersize=3, linewidth=1.6,
                         color=color, label=f"N = {n:,}")
    axes[0].set_xlabel(r"Jump radius $m=s^2$")
    axes[0].set_ylabel(r"Stationary infidelity $1-F_\infty$")
    axes[0].set_title("(a) Stationary accuracy", loc="left", fontweight="bold")
    axes[0].grid(True, which="major", alpha=.18)
    axes[0].legend(frameon=False, fontsize=9, loc="lower left")

    row = filter_data(1026, 8)
    tau = np.geomspace(.02, 25, 220)
    log_ratio = row["log_rates"] - row["log_minimum_rate_over_Gamma"]
    exact = []
    for value in tau:
        argument = np.exp(np.minimum(log_ratio + math.log(value), 40))
        log_product = np.log(-np.expm1(-argument)).sum()
        exact.append(-math.expm1(row["log_fidelity"] + float(log_product)))
    union = np.minimum(1, row["error_sum"] + row["N"]*np.exp(-tau))
    axes[1].semilogy(tau, exact, color=colors[0], linewidth=2,
                     label="Exact worst-case curve")
    axes[1].semilogy(tau, union, color=colors[2], linestyle="--",
                     linewidth=1.8, label="Union bound using actual rate")
    axes[1].axhline(.1, color="#666666", linewidth=.8, linestyle=":")
    axes[1].set_xlabel(r"Rescaled time $\tau=g_{\min}t$")
    axes[1].set_ylabel(r"Worst-case target infidelity")
    axes[1].set_title("(b) Time to approach the target", loc="left",
                      fontweight="bold")
    axes[1].set_xlim(0, 25)
    axes[1].set_ylim(1e-11, 1.5)
    axes[1].grid(True, which="major", alpha=.18)
    axes[1].legend(frameon=False, fontsize=9, loc="lower left")
    axes[1].text(.98, .83,
                 "N = 1,026; s = 8; radius = 64\n"
                 + r"$\log(\Gamma/g_{\min})=$"
                 + f"{-row['log_minimum_rate_over_Gamma']:.2f}",
                 ha="right", va="top", transform=axes[1].transAxes,
                 fontsize=9, bbox={"facecolor":"white", "edgecolor":"none",
                                  "alpha":.9})
    figure.tight_layout(w_pad=2.6)
    figure.savefig(OUT / "accuracy_and_time.svg", metadata={"Date":None})
    figure.savefig(OUT / "accuracy_and_time.png", dpi=180)
    plt.close(figure)
    payload = {
        "convention": "Ideal geometric-root amplitudes; Gamma=1; natural logarithms.",
        "scope": "Finite numerical illustration, not an optimized time/range frontier.",
        "stationary_curves": stationary,
        "dynamics": {
            "N": row["N"], "s": row["s"], "radius": row["radius"],
            "log_minimum_rate_over_Gamma": row["log_minimum_rate_over_Gamma"],
            "stationary_infidelity": row["infidelity"],
            "rescaled_time": tau.tolist(),
            "exact_worst_case_infidelity": exact,
            "actual_rate_union_bound": union.tolist(),
        },
    }
    (OUT / "figure_data.json").write_text(json.dumps(payload, indent=2)+"\n")
    print(json.dumps({
        "figure":str(OUT/"accuracy_and_time.svg"),
        "stationary_cases":len(stationary),
        "dynamics_log_inverse_rate":-row["log_minimum_rate_over_Gamma"],
        "formula_at_tau_10":float(np.interp(10,tau,exact)),
    }, indent=2))


if __name__ == "__main__":
    main()

