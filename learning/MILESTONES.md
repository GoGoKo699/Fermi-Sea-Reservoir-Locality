# Thirty milestones for Fermi-sea reservoir locality

This map follows the scientific question from a single mode exchanging particles with a reservoir to the spatial cost of preparing an entire critical Fermi sea. It organizes the project's understanding targets and their dependencies; the complete statements and proofs remain in the linked scientific pages.

The allocation is **12 background/preliminary milestones and 18 narrative/innovation milestones**. The background connects quantum probabilities, fermionic structure, master equations, Fourier locality and Gaussian states into one operational problem. The narrative develops the lower-bound mechanism and the positive reservoir construction, then integrates coefficient precision, actual preparation time, evidence and scope. The extra narrative space reflects the need to connect an all-generator converse with a physically specified realization.

## Anchor and source roles

The educational anchor is Heinz-Peter Breuer and Francesco Petruccione, *The Theory of Open Quantum Systems*, Oxford University Press, first published in 2002 and first issued in paperback in 2007. The [publisher's book record][BP] and [copyright record][BP-copyright] identify those editions.

- **BP2:** Chapter 2, “Quantum Probability,” for the quantum-state and probability language.
- **BP3:** Chapter 3, “Quantum Master Equations,” pp. 109–218, for Markovian master equations, completely positive dynamical semigroups and relaxation.

These chapter pointers identify the relevant foundations within one anchor. The [anchor bridge](ANCHOR_BRIDGE.md) translates that foundation into the project's conventions and identifies the additional ingredients. Fermionic Gaussian covariance, bounded-degree rational occupations and the discrete approximation argument are supplied by the scientific account and its primary research sources. These additional steps establish the locality theorem, while the book supplies the open-system foundation.

Dependencies below are earlier milestones whose ideas are used directly. Each phase ends by connecting its components into a larger scientific statement.

## Phase I: Background and preliminaries: M01–M12

### M01: A state, a target and a success probability

**Central question.** What does it mean for a possibly mixed quantum state to approximate one specified many-body target?

**Understanding target.** Interpret a density matrix, a target projector and the overlap $`F=\mathrm{Tr}(\rho P_{\mathrm{FS}})`$. Distinguish this squared pure-state fidelity from its square root, and relate it to the probability of obtaining the target outcome.

**Dependencies and story role.** None. This supplies the operational meaning of accuracy before a preparation mechanism is introduced.

**Conceptual connection.** The same target probability will describe stationary approximation, finite-time preparation and the worst initial state; their dynamical conditions will differ.

**Sources.** [BP2]; [target and fidelity](../science/model.md#target-and-fidelity); [target projectors in the dynamical argument](../science/preparation_costs.md#arbitrary-initial-states).

### M02: Fermionic occupation and physical parity

**Central question.** What distinguishes a fermionic mode, and which density matrices are physical in this project?

**Understanding target.** Explain the two possible occupations, the role of creation and annihilation operators, and why fermionic signs matter when modes are combined. Understand that a physical density matrix commutes with total parity, while a projector onto an odd-particle state remains physical.

**Dependencies and story role.** M01. This identifies the local degrees of freedom and the state space on which preparation is required to work.

**Conceptual connection.** Odd linear jump operators can describe particle exchange while their dissipators preserve parity covariance. Physical-state uniqueness must therefore be distinguished from decay of every odd operator.

**Sources.** [Physical parity in the model](../science/model.md#target-and-fidelity); [Majorana conventions](../science/gaussian_stationarity.md#exact-real-space-equation); [the physical-uniqueness caveat](../science/gaussian_stationarity.md#why-physical-uniqueness-does-not-by-itself-justify-a-full-inverse).

### M03: What a Markovian reservoir specifies

**Central question.** How do a Hamiltonian and jump operators together determine open-system evolution?

**Understanding target.** Read the coherent commutator and dissipative terms in the project's Lindblad equation. Identify the assumptions of a time-independent generator, quadratic Hamiltonian and linear jumps, and distinguish this effective description from a microscopic system-bath model.

**Dependencies and story role.** M01, M02. This supplies the dynamical objects whose spatial supports will become the resource.

**Conceptual connection.** The master equation is the anchor's entry point. The project asks a further inverse question: which generators can have a sufficiently accurate stationary state?

**Sources.** [BP3]; [allowed generators](../science/model.md#allowed-generators-and-charged-range); [effective-generator scope](../science/interpretation.md#boundaries-of-the-conclusion).

### M04: One mode: population balance and relaxation

**Central question.** How can the same stationary occupation be reached at different speeds?

**Understanding target.** Explain the gain rate $`a`$, loss rate $`b`$, stationary occupation $`a/(a+b)`$ and occupation-relaxation rate $`g=a+b`$. Recognize that rates are squared jump amplitudes and that rescaling both rates changes time without changing their ratio.

**Dependencies and story role.** M03. A complete one-mode mechanism separates stationary accuracy from dynamical speed.

**Conceptual connection.** The construction will engineer a ratio across momentum space, while normalization and very small amplitude margins determine its waiting-time cost.

**Sources.** [BP3]; [separate gain and loss](../science/gaussian_stationarity.md#separate-gain-and-loss); [the construction's rate equations](../science/reservoir_construction.md#parameters-and-amplitudes).

### M05: Stationarity, uniqueness and attraction

**Central question.** When does a stationary state actually define a preparation procedure?

**Understanding target.** Distinguish being stationary, being the unique physical stationary state and attracting every physical initial state. Explain why a finite positive relaxation rate is different from a rate bounded below uniformly as the system grows.

**Dependencies and story role.** M03, M04. This makes the quantifiers behind “prepares” explicit.

**Conceptual connection.** The operational model requires attraction, while the converse needs only physical uniqueness. A singular covariance drift cannot be excluded merely by invoking that uniqueness.

**Sources.** [BP3]; [operational requirements](../science/model.md#allowed-generators-and-charged-range); [stability and physical uniqueness](../science/gaussian_stationarity.md#why-physical-uniqueness-does-not-by-itself-justify-a-full-inverse).

### M06: The ring and its Fermi sea

**Central question.** How does a nearest-neighbor hopping chain produce a sharp occupation boundary in momentum?

**Understanding target.** Connect the discrete Fourier modes to the dispersion $`-2\cos k`$ and the filled modes with $`\cos k>0`$. Explain why $`N=4M+2`$ avoids sampled zero-energy modes and why the closest modes to a Fermi point remain a distance of order $`1/N`$ away.

**Dependencies and story role.** M02, M03. The local fermionic setting becomes a concrete many-body target.

**Conceptual connection.** The finite momentum spacing sets the smallest scale that the reservoir's occupation filter must resolve.

**Sources.** [Target Hamiltonian and Fourier convention](../science/model.md#target-and-fidelity); [the sampled cosine gap](../science/reservoir_construction.md#stationary-error-bound).

### M07: Spatial support becomes Fourier degree

**Central question.** What algebraic restriction does a finite jump radius impose?

**Understanding target.** Connect a jump supported in $`[-R_J,R_J]`$ to a finite Laurent polynomial, and its rate or Gram matrix to differences of offsets of range at most $`2R_J`$. Keep the common radius $`R=\max(R_H,R_J)`$ distinct from $`S=\max(R_H,2R_J)`$ used in the degree bound.

**Dependencies and story role.** M03, M06. This translates the physical resource into a quantity usable in a proof.

**Conceptual connection.** More translated jump families change coefficients but cannot increase the Laurent degree at fixed support. General pairing Hamiltonians contribute their own charged range.

**Sources.** [Range conventions](../science/model.md#allowed-generators-and-charged-range); [Gram support and the Bloch equation](../science/gaussian_stationarity.md#range-accounting-and-the-bloch-equation).

### M08: Gaussian states and covariance dynamics

**Central question.** Why can this many-body stationary problem be described by two-point correlations?

**Understanding target.** Explain what a fermionic Gaussian state encodes in its Majorana covariance $`C`$, including anomalous pairing correlations. Identify quadratic Hamiltonians and linear jumps as the dynamics preserving this structure, without assuming that every allowed initial state is Gaussian.

**Dependencies and story role.** M02, M03. This introduces the exact structural reduction that makes the problem tractable.

**Conceptual connection.** The covariance is a complete description within the Gaussian class; the preparation-time argument will later use observables that also apply outside that class.

**Sources.** [Exact covariance conventions and evolution](../science/gaussian_stationarity.md#exact-real-space-equation); Barthel–Zhang, [quasifree formalism](https://arxiv.org/pdf/2112.08344), Proposition 1 and Sec. V.1.

### M09: Momentum blocks and many-body probabilities

**Central question.** What product structure survives when pairing is allowed?

**Understanding target.** Explain why translation invariance groups Gaussian correlations into blocks $`\{k,-k\}`$, with separate self-conjugate modes. Distinguish a product over individual occupations in the separate gain/loss subclass from a product over two-mode density matrices in the paired case.

**Dependencies and story role.** M06, M08. This connects a compact covariance description to a whole-state success probability.

**Conceptual connection.** Factorization belongs to the stationary Gaussian state in an appropriate momentum decomposition. It is not an assumption that the full channel factors on arbitrary coherent inputs.

**Sources.** [Pair-block structure and fidelity](../science/gaussian_stationarity.md#pair-block-fidelity-implies-the-needed-aggregate-error-budget); [the separate gain/loss state](../science/gaussian_stationarity.md#separate-gain-and-loss).

### M10: Why stationary filters are rational

**Central question.** Why does a finite polynomial jump amplitude produce an occupation that is a ratio?

**Understanding target.** Read $`n(k)=a(k)/(a(k)+b(k))`$ and its odds $`n(k)/(1-n(k))=a(k)/b(k)`$. Distinguish polynomial degree, rational degree and physical positivity, and identify roots as the ingredients controlling changes in the odds.

**Dependencies and story role.** M04, M07. This gives the algebraic language needed for both the converse and the construction.

**Conceptual connection.** A finite spatial support need not produce a polynomial occupation. The denominator permits much sharper variation, at a possible cost in small physical rates.

**Sources.** [Separate gain/loss rational occupations](../science/gaussian_stationarity.md#separate-gain-and-loss); [the scalar approximation setting](../science/range_lower_bound.md#scalar-converse-from-total-occupation-error).

### M11: Different meanings of approximation

**Central question.** How does whole-state accuracy differ from uniform mode accuracy or local-observable accuracy?

**Understanding target.** Distinguish a product success probability, a sum of wrong-occupation probabilities, a maximum mode error and an error in a local observable. Explain why fixed global overlap permits exceptional modes but does not permit an extensive total occupation error.

**Dependencies and story role.** M01, M09. This identifies the actual accuracy constraint that the lower proof must use.

**Conceptual connection.** Replacing the project's aggregate requirement by a stronger uniform approximation condition would change the problem and could invalidate a claimed converse.

**Sources.** [BP2]; [why whole-state overlap matters](../science/interpretation.md#why-whole-state-overlap-matters); [the scalar total-error hypothesis](../science/range_lower_bound.md#scalar-converse-from-total-occupation-error).

### M12: The stationary spatial-resource problem

**Central question.** What exactly is optimized, and what is deliberately left unrestricted?

**Understanding target.** State the target, fixed overlap threshold, allowed generator class, common radius and initial-state requirement together. Explain why size-dependent coefficients, arbitrary channel count and unrestricted waiting are compatible with a meaningful minimum-range question.

**Dependencies and story role.** M05, M07, M09, M10, M11. This is the background synthesis: the objects and distinctions now form one precise operational task.

**Conceptual connection.** The proposed resource law concerns the attracting stationary approximation. Precision, preparation time and microscopic reservoir engineering are separate questions that must be accounted for without changing that optimization.

**Sources.** [Main theorem and model](../science/model.md#main-theorem); [boundaries of the conclusion](../science/interpretation.md#boundaries-of-the-conclusion); [the source-to-project bridge](ANCHOR_BRIDGE.md#the-missing-steps-from-the-anchor-to-the-theorem).

## Phase II: Narrative and innovation: M13–M30

### M13: Global overlap supplies the error budget

**Central question.** How does the many-body overlap constrain the total number of wrong occupations?

**Understanding target.** Explain the product-to-sum bound $`\sum_k e_k\le-\log F`$ for separate gain/loss, and the factor-two bound for general Gaussian momentum pairs. Identify the projector inequality that bounds each mode's error by failure of its target block.

**Dependencies and story role.** M09, M11, M12. This turns the operational accuracy requirement into the quantitative input of the converse.

**Conceptual connection.** Gaussian block structure provides the needed global control without demanding uniform accuracy of every mode or suppressing pairing coherence.

**Sources.** [Pair-block error budget](../science/gaussian_stationarity.md#pair-block-fidelity-implies-the-needed-aggregate-error-budget); [separate gain/loss product fidelity](../science/gaussian_stationarity.md#separate-gain-and-loss).

### M14: A solvable covariance equation without an extra stability assumption

**Central question.** How can the stationary covariance be inverted when physical uniqueness does not make every drift direction decay?

**Understanding target.** Explain the stationary Bloch-Lyapunov equation, the possible undamped odd sector, and the effect of arbitrarily weak onsite gain plus loss. Understand why compactness and physical uniqueness recover the original state when the added noise vanishes at each fixed size.

**Dependencies and story role.** M05, M08, M12. This closes a logical gap before rational inversion is used.

**Conceptual connection.** Regularization supplies a mathematical inverse while preserving the charged range. The finite-size limit retains the original fidelity threshold and needs no continuity estimate uniform in size.

**Sources.** [Parity-safe regularization](../science/gaussian_stationarity.md#why-physical-uniqueness-does-not-by-itself-justify-a-full-inverse); [BP3] for relaxation foundations; Barthel–Zhang, [Proposition 6](https://arxiv.org/pdf/2112.08344).

### M15: Counting the rational degree of the full Gaussian model

**Central question.** Why do arbitrary linear jump families and pairing still leave a bounded root budget?

**Understanding target.** Connect the two-component Majorana symbol to a four-component linear system, then use determinant degree counting to bound the rational occupation odds. Keep track of Hamiltonian range, Gram range and the total numerator-plus-denominator root count $`d\le16S`$.

**Dependencies and story role.** M07, M10, M14. This makes the converse apply to the whole stated Gaussian class.

**Conceptual connection.** The system size increases the number of sampled momenta, but the fixed one-mode unit cell keeps the local matrix dimension fixed. Additional persistent bands would change this reduction.

**Sources.** [Exact rational-degree calculation](../science/gaussian_stationarity.md#exact-rational-degree-for-the-occupations); Zhang–Barthel, [Bloch rationality, Eqs. (6)–(8)](https://arxiv.org/pdf/2204.05346).

### M16: Resolving a Fermi crossing on the actual grid

**Central question.** How can the required occupation jump be measured without replacing the finite ring by a continuum?

**Understanding target.** Pair sampled momenta on opposite sides of a Fermi point and interpret the tangent coordinate $`x=\tan(q/2)`$. Explain why accurate pairs require a large contrast of log odds, and why logarithmic grid weights compare many scales near the crossing.

**Dependencies and story role.** M06, M10, M13, M15. This puts the physical accuracy demand and the algebraic root representation on the same discrete domain.

**Conceptual connection.** The Möbius substitution preserves bounded degree while converting the two sides of the crossing into evaluations at opposite real arguments.

**Sources.** [The selected grid and log-odds contrast](../science/range_lower_bound.md#scalar-converse-from-total-occupation-error); [the polynomial conversion](../science/gaussian_stationarity.md#exact-rational-degree-for-the-occupations).

### M17: What one polynomial root can contribute

**Central question.** Why can a single root supply only a bounded amount of logarithmic contrast across scales?

**Understanding target.** Interpret the root-potential function, its peak at the root modulus and its integral against logarithmic measure. Explain why the bound $`\pi^2/2`$ is independent of the root's location and remains valid for complex roots.

**Dependencies and story role.** M10, M16. This is the continuous estimate underlying the root budget.

**Conceptual connection.** Root factorization turns a complicated rational filter into a sum of elementary contributions. An integrable singularity is acceptable for the continuous estimate, but it does not yet justify a discrete sampled bound.

**Sources.** [Lemma 1: continuous root budget](../science/range_lower_bound.md#lemma-1-continuous-root-budget); [the logarithmic-scale interpretation](../science/interpretation.md#where-the-two-logarithms-enter).

### M18: Repairing the discrete singularity

**Central question.** What prevents a root extremely close to one sampled momentum from defeating the continuous estimate?

**Understanding target.** Explain the deletion of at most two nodes bracketing each root modulus and the use of adjacent integration cells. Understand why decreasing logarithmic weights make the bound work on both sides of the peak, including exact sample roots and boundary cases.

**Dependencies and story role.** M16, M17. This supplies the discrete safeguard required by the actual finite-ring problem.

**Conceptual connection.** Deleting exceptional samples is useful only if their lost weight is counted. The next step combines this algebraic exception set with the physically inaccurate modes.

**Sources.** [Lemma 2 and its boundary prescription](../science/range_lower_bound.md#lemma-2-discrete-root-budget-after-at-most-two-deletions); [root diagnostics and their limits](../verification/README.md#limits-of-the-checks).

### M19: Combining two exception sets into a finite-size converse

**Central question.** After removing roots and inaccurate modes, why is enough of the Fermi crossing left to force a large degree?

**Understanding target.** Combine the aggregate error budget, the root-adjacent deletions and the retained logarithmic weight. Explain the explicit positive-part bound and the two factors of $`\log N`$: required odds contrast and range of logarithmic scales.

**Dependencies and story role.** M13, M15, M16, M18. This assembles the scalar converse with no uniform-error assumption or uncounted deletion.

**Conceptual connection.** The finite inequality absorbs the degree-dependent deletion cost algebraically. The asymptotic square-logarithmic law follows from that inequality, rather than replacing its discrete proof.

**Sources.** [Lemma 3: total-error converse](../science/range_lower_bound.md#scalar-converse-from-total-occupation-error); [asymptotic form](../science/range_lower_bound.md#asymptotic-form).

### M20: From a root budget to a universal spatial requirement

**Central question.** What physical generators are excluded by the rational-degree lower bound?

**Understanding target.** Translate the scalar result into the common-radius lower bound for all allowed Gaussian generators. Explain the stronger separate gain/loss constant and why its irrelevant number-conserving Hamiltonian is different from a general pairing Hamiltonian whose range must be charged.

**Dependencies and story role.** M12, M15, M19. This completes the converse branch of the project.

**Conceptual connection.** The lower bound permits arbitrary finite coefficients and arbitrarily long waiting. Its force is a spatial obstruction under fixed whole-state accuracy, independent of those freedoms.

**Sources.** [Finite-size physical statements](../science/range_lower_bound.md#model-fidelity-and-finite-size-statement); [application of the Gaussian reduction](../science/gaussian_stationarity.md#application-to-the-range-converse).

### M21: Building a legitimate positive reservoir

**Central question.** How does a rational filter become actual finite-support Lindblad jumps?

**Understanding target.** Explain the geometric-root polynomial evaluated at opposite cosines, the assignment of its two amplitudes to gain and loss, and the support radius of the resulting translated jumps. Identify why their squared rates are nonnegative and cannot vanish simultaneously.

**Dependencies and story role.** M04, M07, M10. This begins the constructive branch with a generator that satisfies the physical model.

**Conceptual connection.** An approximation formula alone is insufficient: a matching upper bound must realize the filter with positive rates and the advertised spatial support.

**Sources.** [Parameters and amplitudes](../science/reservoir_construction.md#parameters-and-amplitudes); [real-space coefficient realization](../science/reservoir_construction.md#normalized-fourier-coefficients); [classical approximation attribution](../references/RELATED_WORK.md).

### M22: Why geometric roots give global accuracy

**Central question.** How does one root distribution control all sampled occupied and empty modes?

**Understanding target.** Explain the multiplicative-neighborhood root count and its bounded factor ratio. Connect the nearest sampled cosine, the choice of the root-spacing parameter and the total stationary error to the radius $`O(\log^2(N/\epsilon))`$.

**Dependencies and story role.** M06, M13, M21. This proves that the construction reaches the spatial order required by the converse.

**Conceptual connection.** Uniformly small errors are a sufficient strategy for this particular upper bound. The universal lower bound did not assume that every successful reservoir follows that strategy.

**Sources.** [Stationary error bound](../science/reservoir_construction.md#stationary-error-bound); [global overlap convention](../science/model.md#target-and-fidelity).

### M23: Bounded rates and a nonzero amplitude margin

**Central question.** Why does a formally positive, normalized filter still require care near the Fermi points?

**Understanding target.** Explain the upper rate normalization and the lower amplitude margin obtained from the polynomial at zero. Distinguish bounded coefficients and bounded total occupation rates from a useful lower bound on relaxation speed.

**Dependencies and story role.** M04, M21, M22. This identifies the small scale that controls both rounding robustness and long waiting.

**Conceptual connection.** The same denominator that permits a sharp occupation ratio can arise from two very small amplitudes. Stationary accuracy alone therefore does not settle implementation precision or dynamics.

**Sources.** [Rate normalization](../science/reservoir_construction.md#parameters-and-amplitudes); [nonzero amplitude margin](../science/reservoir_construction.md#a-nonzero-amplitude-margin); [precision and waiting](../science/interpretation.md#precision-and-waiting-time).

### M24: Finite coefficients with a controlled rounding error

**Central question.** Can the spatially optimal construction be specified with finitely many bits while retaining its guarantees?

**Understanding target.** Explain positivity and symmetry of the normalized Fourier coefficients, downward dyadic rounding and the use of the amplitude margin to control occupation ratios. Identify the sufficient cubic-logarithmic precision per coefficient, fifth-power logarithmic description size and finite interval procedure at rounding boundaries.

**Dependencies and story role.** M07, M21, M22, M23. This replaces an exact-real coefficient description by a finite realization.

**Conceptual connection.** The rounding statement controls both stationary fidelity and nonzero damping. Its bit budget is a sufficient construction cost, not a precision lower bound over all reservoirs.

**Sources.** [Normalized coefficients](../science/reservoir_construction.md#normalized-fourier-coefficients); [dyadic rounding theorem](../science/reservoir_construction.md#dyadic-rounding-theorem); [finite boundary procedure](../science/reservoir_construction.md#a-finite-procedure-at-rounding-boundaries).

### M25: Reaching the target from arbitrary physical inputs

**Central question.** Why do the preparation guarantees also cover non-Gaussian initial states and occupation coherences?

**Understanding target.** Use the closed occupation equations and the operator union bound to connect the stationary error budget with a finite-time overlap guarantee. Explain how the implemented minimum occupation rate enters the sufficient waiting time.

**Dependencies and story role.** M03, M05, M13, M24. This upgrades stationary feasibility to an actual preparation guarantee for the stated initial-state class.

**Conceptual connection.** The proof uses observables whose equations close for every input. It does not assume Gaussianity of the initial state or identify occupation relaxation with the full Liouvillian gap.

**Sources.** [BP3]; [arbitrary-initial-state guarantee](../science/preparation_costs.md#arbitrary-initial-states); [implemented rate margin](../science/reservoir_construction.md#dyadic-rounding-theorem).

### M26: The exact worst initial state

**Central question.** Which physical input gives the smallest target population at a fixed time?

**Understanding target.** Explain why the occupation-diagonal algebra evolves as independent two-state chains and why the complementary Fock state minimizes every target-bit probability. Recover the exact worst-case product curve without assuming a tensor-product quantum channel on arbitrary coherences.

**Dependencies and story role.** M04, M09, M25. This sharpens a sufficient-time estimate into an exact operational curve for the construction.

**Conceptual connection.** A many-body worst-case statement can follow from a classical subalgebra even though the surrounding dynamics and admissible inputs are quantum.

**Sources.** [Exact worst-case fidelity curve](../science/preparation_costs.md#exact-worst-case-fidelity-curve); [direct non-Gaussian state-evolution check](../verification/README.md#what-the-state-evolution-check-establishes).

### M27: The construction's actual time scale

**Central question.** Is the long preparation time a real property of this reservoir or only an artifact of a loose estimate?

**Understanding target.** Locate the ideal minimum rate at the sampled modes nearest the Fermi points and interpret the finite logarithmic sum controlling it. Explain why the stated parameter choice gives a cubic-logarithmic exponent in inverse rate and worst-case time, and why the relative rounding bound preserves this conclusion.

**Dependencies and story role.** M23, M24, M26. This gives the construction a quantitative dynamical cost.

**Conceptual connection.** The exact worst-case curve connects the achieved rate to actual preparation time. This construction-specific result does not optimize time over every spatially admissible reservoir.

**Sources.** [Actual minimum-rate calculation](../science/preparation_costs.md#actual-minimum-rate-of-the-ideal-filter); [worst-case time bounds](../science/preparation_costs.md#exact-worst-case-fidelity-curve); [pointwise rounding control](../science/reservoir_construction.md#dyadic-rounding-theorem).

### M28: What the finite calculations establish

**Central question.** How should analytical proofs and finite numerical evidence be read together?

**Understanding target.** Identify what the root, covariance, coefficient-rounding and state-evolution diagnostics test. Distinguish numerical residuals from an all-size proof, high-precision arithmetic from interval certification, and sampled filter performance from optimization over reservoirs.

**Dependencies and story role.** M14, M18, M24, M26, M27. This integrates the evidence supporting conventions and realizations without overstating its reach.

**Conceptual connection.** The delicate mathematical features suggest targeted checks, but the universal resource law remains an analytical result. Large formal radii on small periodic rings must also be interpreted through periodization.

**Sources.** [Verification scope and limits](../verification/README.md#limits-of-the-checks); [precision diagnostics](../verification/README.md#what-the-precision-check-establishes); [finite quantitative examples](../science/preparation_costs.md#quantitative-finite-examples).

### M29: The contribution within its research context

**Central question.** Which ingredients are established, and what additional physical statement is assembled here?

**Understanding target.** Distinguish exact local-stabilization obstructions, Gaussian-MPS approximation, classical rational approximation and the all-reservoir fixed-overlap range problem. Attribute covariance rationality and geometric-root methods correctly while identifying the discrete aggregate-error converse and positive physical realization.

**Dependencies and story role.** M15, M19, M20, M21, M22. This places the two proof branches within the surrounding science.

**Conceptual connection.** A shared rational mechanism does not make every approximation model or error criterion identical. The significance of the theorem depends on its quantifiers, physical class and complete resource accounting.

**Sources.** [Related work and primary references](../references/RELATED_WORK.md); [converse attribution](../science/range_lower_bound.md#attribution); [relation to exact locality](../science/interpretation.md#relation-to-exact-locality-results).

### M30: The complete spatial theorem and its physical meaning

**Central question.** What can be concluded about preparing a critical Fermi sea once all parts of the argument are combined?

**Understanding target.** Explain why the matched bounds establish $`R_{\min}(N,F_0)=\Theta_{F_0}((\log N)^2)`$ at fixed whole-state overlap. State separately the supplied construction's coefficient, precision and time costs, and identify which changes of model or optimization objective remain outside the result.

**Dependencies and story role.** M20, M22, M24, M27, M28, M29. This is the narrative synthesis: a precise resource question, a universal obstruction, a matching realization and its practical limits form one connected scientific account.

**Conceptual connection.** Spatial feasibility, finite specification and approach to the target are related resources with distinct quantifiers. Persistent ancillas, enlarged cells, nonlinear jumps, time-dependent control and microscopic bath locality require separate analysis.

**Sources.** [Main theorem](../science/model.md#main-theorem); [resource summary](../science/preparation_costs.md#resource-summary); [physical meaning and scope](../science/interpretation.md); [anchor-to-project bridge](ANCHOR_BRIDGE.md#the-missing-steps-from-the-anchor-to-the-theorem).

[BP]: https://academic.oup.com/book/27757
[BP-copyright]: https://academic.oup.com/book/27757/chapter-abstract/197977120
[BP2]: https://academic.oup.com/book/27757/chapter-abstract/197977987
[BP3]: https://academic.oup.com/book/27757/chapter-abstract/197978616
