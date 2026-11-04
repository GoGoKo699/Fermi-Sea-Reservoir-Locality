# Model and sharp spatial threshold

A stationary reservoir prepares a many-body state by making it the attracting steady state of an open-system evolution. For a critical Fermi sea, the target occupation changes discontinuously at the Fermi points. The question is how much spatial reach a reservoir needs when the target is approximated on a finite ring.

The resource studied here is the range of the effective Gaussian Lindblad generator. The accuracy criterion is the overlap with the entire target state. Coefficients may depend on system size, and the stationary feasibility problem puts no restriction on waiting time.

## Target and fidelity

There are $`N=4M+2`$ spinless fermionic modes on a periodic ring, with one mode $`c_x`$ per site. Set the lattice spacing and the hopping coefficient to one. The Fourier convention and target Hamiltonian are

```math
c_k=\frac{1}{\sqrt N}\sum_{x=0}^{N-1}e^{-ikx}c_x,
\qquad
K_N=\left\{\frac{2\pi m}{N}:m=0,\ldots,N-1\right\},
```

```math
H_{\mathrm{tar}}
=-\sum_{x=0}^{N-1}
\left(c_x^\dagger c_{x+1}+c_{x+1}^\dagger c_x\right)
=-2\sum_{k\in K_N}\cos k\,c_k^\dagger c_k.
```

The unique ground state $`|\mathrm{FS}_N\rangle`$ occupies precisely the modes with $`\cos k>0`$. The chosen sizes exclude zero-energy modes at the Fermi points and give exactly $`N/2`$ particles.

For a stationary density matrix $`\sigma`$, define

```math
F(\sigma)=
\langle\mathrm{FS}_N|\sigma|\mathrm{FS}_N\rangle.
```

This is the squared pure-state fidelity. A fixed threshold $`F_0\in(0,1)`$ is held independent of $`N`$ in the spatial theorem. It can be close to one. If the desired trace distance from the target is at most $`\varepsilon`$, the sufficient condition $`F\ge1-\varepsilon^2`$ follows from the standard pure-target fidelity bound.

Physical density matrices commute with total fermion parity. Projectors onto odd-parity vectors are physical; in particular, the target has the odd particle number $`N/2=2M+1`$. No restriction to the even-particle Hilbert subspace is imposed.

## Allowed generators and charged range

The dynamics is time independent and translation invariant:

```math
\frac{d\rho}{dt}=\mathcal L(\rho)
=-i[H,\rho]
+\sum_{\mu,x}\mathcal D[L_{\mu,x}](\rho),
\qquad
\mathcal D[L](\rho)
=L\rho L^\dagger-\frac12\{L^\dagger L,\rho\}.
```

The Hamiltonian $`H`$ is quadratic and may contain pairing. Its coupling range is $`R_H`$. Each translated jump is linear,

```math
L_{\mu,x}
=\sum_{r=-R_J}^{R_J}
\left(u_{\mu,r}c_{x+r}
+v_{\mu,r}c_{x+r}^\dagger\right).
```

Both coefficients and the number of jump families may depend on $`N`$. The charged radius is

```math
R=\max\{R_H,R_J\}.
```

A jump of radius $`R_J`$ acts on at most $`2R_J+1`$ consecutive sites before periodization. On a small ring, repeated positions can be combined; this cannot enlarge the Laurent-degree bounds used in the converse. A support-diameter convention changes only constant factors.

The generator must converge from every physical initial state to a unique physical stationary state. The lower bound in fact needs only uniqueness. There is no assumed uniform spectral gap, coefficient bound, or minimum damping strength. The construction has bounded rates and explicitly finite coefficient precision.

There are no additional persistent modes per cell. Translation invariance is with respect to one lattice site. Time-dependent control, feedback, interacting jumps and enlarged auxiliary systems define different preparation models.

## Main theorem

Let $`R_{\min}(N,F_0)`$ be the smallest common radius among the allowed generators whose stationary state has overlap at least $`F_0`$. For every fixed $`F_0\in(0,1)`$,

```math
\boxed{
R_{\min}(N,F_0)=
\Theta_{F_0}\!\left((\log N)^2\right)
\qquad (N=4M+2\to\infty).
}
```

The statement has two complementary parts.

| Part | Scope and conclusion | Proof |
|---|---|---|
| Converse | Every allowed Gaussian generator, including pairing, needs common radius of order at least the square of the logarithm. Rates and waiting time are unrestricted. | [Finite range lower bound](range_lower_bound.md), with the [Gaussian covariance reduction](gaussian_stationarity.md) |
| Construction | Two translated gain/loss families, together with the fixed nearest-neighbor target Hamiltonian, attain that radius order. | [Explicit reservoir and precision](reservoir_construction.md) |
| Preparation cost | The same finite-precision construction reaches the target accuracy from every physical initial state. Its worst-case preparation time is very large. | [Convergence and resource accounting](preparation_costs.md) |

The [finite-size converse](range_lower_bound.md) gives an explicit elementary bound for every allowed $`N\ge1026`$. Its constants are unoptimized, and its positive part permits a vacuous bound at modest size or very small required overlap.

A sharper constant holds in the subclass of separate creation and annihilation jumps with a number-conserving Hamiltonian. In that subclass, the Hamiltonian commutes with every momentum occupation, so its range is irrelevant to the stationary occupation law. For general pairing Hamiltonians, coherent range must be charged.

## Constructive resource statement

For $`0<\epsilon<1`$ and a rate scale $`\Gamma>0`$, the explicit construction uses

```math
m=s^2=O\!\left(\log^2\frac N\epsilon\right)
```

as its jump radius. It has $`m+1`$ independent nonnegative Fourier coefficients; symmetry and alternating signs determine the two jump families. A sufficient absolute precision is

```math
b=O\!\left(\log^3\frac N\epsilon\right)
```

fractional bits per independent coefficient. The total coefficient description therefore uses $`O(\log^5(N/\epsilon))`$ bits. This is a sufficient representation cost, not a lower bound on precision or an optimized preprocessing cost.

After rounding, the stationary overlap is at least $`1-\epsilon/2`$. With the explicit parameter $`s`$ defined in the [construction](reservoir_construction.md), every physical initial state reaches overlap at least $`1-\epsilon`$ by

```math
t_{\mathrm{suff}}
=\frac4\Gamma
\exp(s^3+s+2)
\log\frac{2N}{\epsilon}.
```

The momentum occupation rates remain at most $`\Gamma`$. For fixed $`\epsilon`$ and the stated choice $`s/\log N\to1`$, this particular reservoir actually has

```math
\log\!\bigl(\Gamma t_{\mathrm{worst}}\bigr)
=(1+o(1))(\log N)^3.
```

Thus its slow preparation is a property of the construction, not merely an artifact of a loose sufficient-time estimate. The spatial converse does not establish an optimal time versus range tradeoff.

## Reading the proof

The argument starts by turning global overlap into a bounded total error in momentum occupations. Stationary Gaussian covariance then makes those occupations rational functions of bounded degree. A discrete root-potential estimate forces a square-logarithmic degree under that total-error constraint. Finally, geometric-root polynomials realize the matching degree with positive gain and loss rates.

The rational covariance formalism and approximation mechanism have substantial prior literature. The [related-work account](../references/RELATED_WORK.md) identifies those ingredients and the distinction between exact local stabilization, Gaussian state approximation and the optimized finite-accuracy range question considered here.

Continue with [Gaussian stationarity](gaussian_stationarity.md), or read the scalar [range lower bound](range_lower_bound.md) first. The [physical interpretation](interpretation.md) explains why global accuracy, spatial reach, precision and time enter differently.

