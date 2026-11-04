# Physical interpretation

## What the range law says

The target has a sharp boundary between occupied and empty momentum modes. On a finite ring, a reservoir need not reproduce that boundary as an exact function of continuous momentum. It must nevertheless prepare the whole finite many-body state with the required overlap.

For fixed global overlap, a stationary Gaussian reservoir needs a range proportional to $`(\log N)^2`$, up to constants. The converse allows coefficients that depend on $`N`$, arbitrarily many translated jump families, arbitrarily small damping rates and arbitrarily long waiting. Those freedoms cannot remove the spatial requirement.

The construction shows that this range order is sufficient. It uses only two translated jump families and a fixed nearest-neighbor Hamiltonian. This identifies a spatial feasibility threshold within the [specified Gaussian model](model.md).

## Why whole-state overlap matters

For separate gain and loss, the stationary state is a product over momentum modes. If $`e_k`$ is the wrong-occupation probability in mode $`k`$, then

```math
F_\infty=\prod_k(1-e_k),
\qquad
F_\infty\ge F_0
\ \Longrightarrow\
\sum_k e_k\le-\log F_0.
```

A fixed nonzero overlap therefore allows only a bounded total occupation error as the system grows. This condition is stronger than keeping the error of each local observable small. It does not require every individual mode to have error of order $`1/N`$: a few modes may be much worse.

Pairing changes the product structure. A translation-invariant Gaussian state factors into blocks of at most two momentum modes. The corresponding implication is

```math
\sum_k e_k\le-2\log F.
```

The lower proof uses precisely this aggregate control. It removes the limited set of inaccurate modes and still obtains a sufficiently large contribution from the remaining momenta.

## Where the two logarithms enter

Near a Fermi point, the tangent variable $`x=\tan(q/2)`$ turns the occupation odds into a rational function. Bounded generator range limits the number of its polynomial roots.

Across the retained momentum scales, accurate modes require a logarithmic odds contrast of order $`\log N`$. The logarithmic measure of those scales is itself of order $`\log N`$. Their weighted contribution is therefore of order $`(\log N)^2`$.

A single polynomial root contributes only a bounded amount to that weighted contrast after its adjacent sample points are removed. The [discrete root lemma](range_lower_bound.md) is needed because an arbitrarily close root can otherwise create an unbounded sample value. The available root budget consequently forces the spatial range.

This mechanism uses established rational-approximation ideas. Its role here is to connect a global physical accuracy requirement to an optimum over all allowed stationary reservoirs.

## Precision and waiting time

The [constructive coefficients](reservoir_construction.md) are normalized and bounded. Their small near-Fermi amplitudes arise through cancellation, so an absolute precision statement is still necessary. Downward dyadic rounding with the proven bit budget preserves positive damping and the desired stationary fidelity.

Long waiting is a separate cost. For the same construction, the slowest occupation rate is exponentially small in $`(\log N)^3`$. Its exact worst-case target fidelity can be written as

```math
\inf_{\rho_0}F_{\rho_0}(t)
=F_\infty\prod_k\left(1-e^{-g_k t}\right).
```

The complementary Fock state attains this minimum. The formula explains the construction's actual slow preparation without assuming a Gaussian initial state or identifying occupation rates with the full Liouvillian spectral gap.

The [resource account](preparation_costs.md) separates the actual worst-case curve, a sufficient time based on the actual minimum rate, and the looser elementary guarantee. Improving preparation time at the optimal range remains a distinct optimization problem.

## Relation to exact locality results

Exact stabilization asks whether a local generator has the target itself as a stationary state. The present question fixes a finite overlap threshold and permits a mixed stationary approximation with coefficients redesigned for each size. This changes the approximation problem.

Recent locality papers already study exact Fermi-sea obstructions, reservoir tails and truncated constructions, including true global-fidelity calculations. Gaussian matrix-product-state work also provides closely related rational approximations and geometric-root constructions. The [source comparison](../references/RELATED_WORK.md) makes those connections explicit. The central conclusion here is the sharp optimized hard-range threshold under fixed whole-state accuracy.

## Boundaries of the conclusion

The result concerns effective Gaussian Lindblad range. It does not identify that range with the locality of an underlying microscopic system-bath Hamiltonian. Engineering a spatially extended jump can require additional physical resources. Locality is defined in the fermionic algebra; Jordan–Wigner spin strings mean that the same operators need not be local in a spin representation.

The one-mode unit cell, translation invariance and time-independent linear jumps are assumptions of the theorem. A persistent auxiliary system, feedback, an enlarged unit cell, nonlinear jumps or time-dependent controls may change the feasible generators and their rational-degree bounds. The current converse does not settle those models.

The theorem constrains the attracting stationary state. It does not prohibit a different finite-time control protocol from passing close to the target. Within its stated model, the matching bounds establish the spatial cost, while the explicit precision and dynamical estimates show what the supplied realization pays to attain it.

