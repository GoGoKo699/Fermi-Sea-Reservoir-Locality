# From open-system dynamics to a spatial locality theorem

Consider a ring of fermionic sites whose reservoir continuously adds and removes particles. The task is to make its attracting stationary state approximate the entire half-filled Fermi sea. The question is how far the Hamiltonian couplings and reservoir jumps must reach, even when arbitrarily long waiting is allowed.

This bridge connects the selected educational anchor to that question. The [30-milestone map](MILESTONES.md) organizes the project's understanding targets and dependencies. The [model and main theorem](../science/model.md) remain the authoritative statement of the result.

## Selected educational anchor

**Heinz-Peter Breuer and Francesco Petruccione, *The Theory of Open Quantum Systems*, Oxford University Press.** The book was first published in **2002**; its first paperback publication was **2007**. The [official Oxford record](https://academic.oup.com/book/27757) and [publisher's copyright page](https://academic.oup.com/book/27757/chapter-abstract/197977120) distinguish those dates. The hardcover ISBN is **978-0-19-852063-4**; the first paperback ISBN is **978-0-19-921390-0**. The linked Oxford edition has [DOI 10.1093/acprof:oso/9780199213900.001.0001](https://doi.org/10.1093/acprof:oso/9780199213900.001.0001).

The book supplies the framework for density matrices, completely positive evolution and quantum master equations. The reading route below uses the publisher's chapter titles and topics. Primary research papers supply the specialized fermionic and approximation-theoretic ingredients identified later on this page.

## A focused route through the book

Read the project's model alongside the relevant parts of the book; the complete book is not a prerequisite for following the scientific account.

| Reading purpose | Anchor location | Connection to this project |
|---|---|---|
| Interpret states and measurement probabilities | **Chapter 2, “Quantum Probability”** ([publisher chapter](https://academic.oup.com/book/27757/chapter-abstract/197977987)): density matrices, composite systems, quantum operations and effects | Understand the stationary density matrix and the probability of the target-state projector. |
| Understand the dynamical model | **Chapter 3, “Quantum Master Equations,” pp. 109–218** ([publisher chapter](https://academic.oup.com/book/27757/chapter-abstract/197978616)): completely positive dynamical semigroups and quantum Markov processes | Read the Hamiltonian and jump terms in the [allowed generator](../science/model.md#allowed-generators-and-charged-range), and distinguish a stationary state from convergence toward it. |
| Interpret relaxation and model assumptions | Chapter 3's treatment of relaxation and microscopic master-equation derivations | Separate stationary accuracy from preparation time. The project starts from an effective Lindblad generator; its range theorem does not derive the locality of a microscopic system–bath Hamiltonian. |

These are chapter-level reading pointers. The steps connecting them to the reservoir-range theorem are supplied explicitly by the scientific pages below.

## Notation and assumptions in this project

The repository uses the Lindblad convention

```math
\frac{d\rho}{dt}=\mathcal L(\rho)
=-i[H,\rho]+\sum_{\mu,x}\mathcal D[L_{\mu,x}](\rho),
\qquad
\mathcal D[L](\rho)
=L\rho L^\dagger-\frac12\{L^\dagger L,\rho\}.
```

The Hamiltonian term describes coherent evolution; the dissipators describe the reservoir's channels. Rate factors are absorbed into the jump amplitudes: a term with coefficient $`\gamma\mathcal D[A]`$ is written using $`L=\sqrt\gamma A`$.

| General open-system concept | Repository convention and specialization |
|---|---|
| System state | $`\rho(t)`$ describes the full fermionic ring after the environment has been eliminated. Its stationary state is $`\sigma`$, satisfying $`\mathcal L(\sigma)=0`$. |
| Degrees of freedom | There is one fermionic mode $`c_x`$ per site. Creation and annihilation operators obey canonical anticommutation relations, developed in the [covariance account](../science/gaussian_stationarity.md). |
| Coherent and dissipative terms | $`H`$ is quadratic and may contain pairing terms. Each jump is linear and may mix creation and annihilation operators. The explicit construction uses separate gain and loss. |
| Spatial resource | $`R_H`$ is the Hamiltonian coupling range, $`R_J`$ the jump radius, and $`R=\max\{R_H,R_J\}`$ the charged common radius. Translation invariance is by one site. |
| Gaussian covariance and rate scale | $`C`$ denotes the Majorana covariance. The separate symbol $`\Gamma`$ denotes the physical occupation-rate scale in the construction. |
| Physical states | Density matrices commute with total fermion parity. A projector onto an odd-parity vector is physical; this includes the target with $`N/2=2M+1`$ particles. |

The target Hamiltonian specifies which state is wanted. The generator's Hamiltonian is part of the allowed preparation mechanism; it need not equal the target Hamiltonian in the converse. The construction chooses the nearest-neighbor target Hamiltonian itself.

## The missing steps from the anchor to the theorem

### Fermionic covariance and stationary rational functions

The specialized reduction starts with Majorana operators, which are Hermitian combinations of creation and annihilation operators. For quadratic Hamiltonians and linear jumps, their two-point covariance obeys a closed equation,

```math
\dot C=XC+CX^T+Y.
```

Here $`X`$ contains coherent motion and damping, and $`Y`$ supplies the reservoir's covariance source. This quasi-free formalism is an imported research ingredient, with normalization and signs fixed in [Gaussian stationarity](../science/gaussian_stationarity.md#exact-real-space-equation).

Translation invariance turns that equation into a small matrix problem at each momentum. Finite spatial range bounds the Laurent degree of its coefficients. Solving the stationary equation therefore makes the occupations rational functions with a controlled degree. The project's proof includes an onsite-noise regularization before taking a fixed-size limit: uniqueness among physical states alone does not justify inverting the unrestricted covariance system. That qualification is essential to the full pairing-inclusive converse.

### Whole-state fidelity gives an aggregate error budget

The accuracy criterion is

```math
F=\langle\mathrm{FS}_N|\sigma|\mathrm{FS}_N\rangle.
```

It is the probability of the target projector, or squared pure-state fidelity. Define $`e(k)`$ as the probability of the wrong occupation in mode $`k`$. For the separate gain/loss stationary state, the mode probabilities multiply, giving $`F=\prod_k(1-e(k))`$. In the general translation-invariant Gaussian setting, pairing can correlate opposite momenta, so the state factors into blocks of at most two modes instead. The [pair-block argument](../science/gaussian_stationarity.md#pair-block-fidelity-implies-the-needed-aggregate-error-budget) gives

```math
\sum_k e(k)\le-2\log F.
```

Thus fixed nonzero global overlap permits only a bounded total error as the ring grows. It still permits a few inaccurate modes. This project-specific use of global fidelity is the link between the physical preparation task and the approximation problem.

### The finite-grid rational obstruction

Near a Fermi point, a tangent change of variable converts the occupation odds into a ratio of ordinary polynomials. The [range lower bound](../science/range_lower_bound.md) then compares two quantities: the contrast required by accurate occupied and empty modes, and the contrast that a fixed number of polynomial roots can supply across momentum scales.

The proof retains the aggregate error criterion. It removes the set of inaccurate modes controlled by the aggregate error budget and the sample points adjacent to root peaks; those deletions prevent an arbitrarily near-grid root from producing an uncontrolled discrete spike. The number of removed modes can grow with system size, while their discarded logarithmic weight remains controlled. The remaining weighted contrast requires order $`(\log N)^2`$ roots. Together with the covariance degree bound, this yields the spatial converse. This finite-grid argument and its application to the optimized reservoir class are project-specific derivations built on established rational-approximation ideas.

## Construction, accuracy and waiting time

A single fermionic mode already exposes an important distinction. With gain rate $`a`$ and loss rate $`b`$, its mean occupation $`q(t)`$ obeys

```math
\dot q=a-(a+b)q,
\qquad
q_\infty=\frac{a}{a+b},
\qquad
g=a+b.
```

The rate ratio sets the stationary occupation; their sum sets occupation relaxation. Multiplying both rates by two preserves the stationary state and halves the relaxation time. This elementary connection to the anchor's master-equation framework helps explain why spatial feasibility and waiting time are separate resources.

The project's [matching construction](../science/reservoir_construction.md) chooses geometric-root polynomials in $`\cos k`$ as the gain/loss amplitudes. Their squares give nonnegative gain and loss rates, with a strictly positive total occupation rate. Their Fourier support gives actual finite-radius jumps. Combined with the converse, the project-specific result is

```math
R_{\min}(N,F_0)=\Theta_{F_0}\!\left((\log N)^2\right),
\qquad N=4M+2\to\infty,
```

for each fixed $`F_0\in(0,1)`$, under the assumptions in the model.

The supplied realization also accounts for its coefficients and dynamics. For final infidelity $`\epsilon`$, a sufficient jump radius is $`O(\log^2(N/\epsilon))`$ and a sufficient absolute precision per independent normalized coefficient is $`O(\log^3(N/\epsilon))`$ fractional bits. Downward rounding preserves positive damping and the stationary accuracy. These are constructive upper bounds; the spatial theorem holds at fixed overlap and does not claim an optimal precision frontier.

The [preparation proof](../science/preparation_costs.md#arbitrary-initial-states) covers every physical initial state, including non-Gaussian states. Commuting wrong-occupation projectors give an operator union bound, so the scalar relaxation equations control whole-state fidelity without assuming that the initial state factors. At fixed accuracy, this particular construction has worst-case preparation time $`\Gamma^{-1}\exp[\Theta((\log N)^3)]`$. Its slow dynamics and the exact worst-case fidelity curve are established separately from the all-reservoir spatial lower bound.

## Scientific routes and primary sources

The book remains the single educational anchor. The following primary papers identify specialized ingredients and close precedents; the [related-work account](../references/RELATED_WORK.md) supplies the full comparison and bibliography.

| Specialized ingredient | Primary research source | Canonical project route |
|---|---|---|
| Quasi-free covariance dynamics and stability | Barthel and Zhang, *J. Stat. Mech.* (2022) 113101 ([DOI](https://doi.org/10.1088/1742-5468/ac8e5c); [published-version preprint](https://arxiv.org/abs/2112.08344v5)) | [Covariance conventions and regularization](../science/gaussian_stationarity.md) |
| Translation-invariant stationary covariance as a rational function | Zhang and Barthel, *Phys. Rev. Lett.* **129**, 120401 (2022), Eqs. (6)–(8) ([DOI](https://doi.org/10.1103/PhysRevLett.129.120401); [primary text](https://arxiv.org/pdf/2204.05346)) | [Range and rational-degree accounting](../science/gaussian_stationarity.md#range-accounting-and-the-bloch-equation) |
| Geometric-root approximation and sharp discrete uniform sign approximation | Newman (1964) and Sherstov (2013), with original citations in [Related Work](../references/RELATED_WORK.md#references); [Sherstov's author manuscript](https://web.cs.ucla.edu/~sherstov/pdf/hshs.pdf) | [Discrete root budget](../science/range_lower_bound.md#root-potential-estimates) and [positive reservoir construction](../science/reservoir_construction.md) |
| Closely related rational occupations and Gaussian-state approximation | Franco-Rubio and Cirac, *Phys. Rev. B* **106**, 235136 (2022) ([published source](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.106.235136)) | [Attribution and distinctions](../references/RELATED_WORK.md) |

Use the [milestone map](MILESTONES.md) for the connected learning route, the [physical interpretation](../science/interpretation.md) for the result's meaning and boundaries, and the [verification guide](../verification/README.md) for reproducible checks and their limits. The exact assumptions, constants and proofs remain in the linked scientific pages.
