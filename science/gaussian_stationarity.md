# Gaussian stationarity and the range converse

This account reduces general translation-invariant Gaussian reservoir dynamics to the rational occupations required by the [finite-size scalar converse](range_lower_bound.md). The calculation includes pairing in both the quadratic Hamiltonian and the linear jumps.

There is one physical fermionic mode per site on a periodic ring, $`N=4M+2`$. Jumps have radius $`R_J`$, the Hamiltonian has coupling range $`R_H`$, and

```math
S=\max\{R_H,2R_J\},\qquad R=\max\{R_H,R_J\},\qquad S\le2R.
```

The generator has a unique parity-invariant stationary density matrix $`\sigma`$, with overlap $`F=\langle\mathrm{FS}_N|\sigma|\mathrm{FS}_N\rangle\ge F_0>0`$. Requiring convergence from every physical initial state is compatible with the proof; only uniqueness is used in the lower bound. Coefficients and channel counts may depend on size. The [model account](model.md) gives the complete operational setting.

The symbol $`C`$ denotes the Majorana covariance throughout this account. The symbol $`\Gamma`$ is reserved elsewhere for the physical rate scale of the explicit reservoir.

## Exact real-space equation

Use Majoranas

```math
w_{x,1}=c_x+c_x^\dagger,
\qquad w_{x,2}=-i(c_x-c_x^\dagger),
\qquad\{w_\alpha,w_\beta\}=2\delta_{\alpha\beta},
```

where the indices in these real-space formulas include site and Majorana component. In the Bloch kernels below, they label the two components within one site. Define the real antisymmetric covariance

```math
C_{\alpha\beta}
=\frac i2\operatorname{Tr}\rho[w_\alpha,w_\beta]
=i\operatorname{Tr}(\rho w_\alpha w_\beta)-i\delta_{\alpha\beta}.
```

Write

```math
H=\frac i4\sum_{\alpha,\beta}h_{\alpha\beta}w_\alpha w_\beta,
\quad h\in\mathbb R^{2N\times2N},\ h^T=-h,
\quad L_\lambda=\sum_\alpha\ell_{\lambda,\alpha}w_\alpha,
```

and define

```math
\mathsf M_{\alpha\beta}
=\sum_\lambda\ell_{\lambda,\alpha}\overline{\ell_{\lambda,\beta}},
\qquad
\mathsf A=\operatorname{Re}\mathsf M,
\qquad\mathsf B=\operatorname{Im}\mathsf M.
```

Thus $`\mathsf M\ge0`$, $`\mathsf A`$ is real symmetric positive semidefinite, and $`\mathsf B`$ is real antisymmetric. Entrywise real and imaginary parts in the Gram definition are taken **in real space**, before the Fourier transform. The exact covariance equation is

```math
\dot C=XC+C X^T+Y,
\qquad X=h-2\mathsf A,\qquad Y=4\mathsf B.
```

This is Proposition 1 and Eq. (15) of Barthel–Zhang [1], converted from their Majorana normalization and sign convention. It can also be checked directly from the canonical anticommutation relations. For example, one-site loss $`L=\sqrt\kappa c`$ gives $`X=-\kappa I_2/2`$, $`Y_{12}=-\kappa`$, and $`C_{12}=2\langle c^\dagger c\rangle-1`$, correctly relaxing to the vacuum.

## Range accounting and the Bloch equation

Translation-invariant matrices have kernels, for example

```math
C_{x\alpha,y\beta}=\gamma_{\alpha\beta}(x-y),
\qquad
C(k):=\sum_{r\in\mathbb Z_N}e^{-ikr}\gamma(r).
```

Use the same Fourier sign for $`X(k)`$ and $`Y(k)`$. The Hamiltonian kernel is supported within $`R_H`$. A translated jump of radius $`R_J`$ contributes to the Gram kernel $`\mathsf M`$ only at differences of two offsets in $`[-R_J,R_J]`$, hence within $`2R_J`$. Summing any number of jump families does not enlarge this support. Thus every entry of $`X(k)`$ and $`Y(k)`$ is represented by a Laurent polynomial in $`z=e^{ik}`$ with exponents in $`[-S,S]`$.

At a stationary covariance,

```math
X(k)C(k)+C(k)X(-k)^T=-Y(k).
```

This Bloch-Lyapunov representation and rationality principle are established in Zhang–Barthel [2], Eqs. (6)–(8). The finite-degree accounting and the aggregate-error application here are spelled out rather than assumed.

Because $`X`$ is real, $`X(-k)^T=X(k)^\dagger`$ on the momentum grid. Also $`h(k)^\dagger=-h(k)`$ and $`\mathsf A(k)\ge0`$, so

```math
X(k)+X(k)^\dagger=-4\mathsf A(k)\le0.
```

## Why physical uniqueness does not by itself justify a full inverse

Uniqueness among parity-invariant density matrices need not make $`X`$ strictly stable. For one mode with $`L=c+c^\dagger=w_1`$ and $`H=0`$, the sole physical stationary density matrix is $`I_2/2`$, but $`X=\operatorname{diag}(-2,0)`$. The odd operator $`w_1`$ is also stationary. Thus an argument that infers invertibility of the entire four-component Bloch system solely from physical uniqueness would be incomplete.

For each fixed $`N`$, repair this by adding balanced onsite noise of arbitrarily small strength $`\eta>0`$:

```math
\mathcal L_\eta
=\mathcal L+\eta\sum_x\bigl(\mathcal D[c_x]+\mathcal D[c_x^\dagger]\bigr).
```

It adds $`\eta I/2`$ to $`\mathsf M`$, so

```math
X_\eta=X-\eta I,
\qquad Y_\eta=Y,
\qquad X_\eta(k)+X_\eta(k)^\dagger\le-2\eta I_2.
```

The ranges are unchanged. Every $`X_\eta(k)`$ is strictly stable, and all eigenvalues of the corresponding Lyapunov operator have strictly negative real part. In particular the Bloch-Lyapunov equation has a unique four-component solution for each allowed $`k`$.

Quadratic Hamiltonians and linear jumps preserve Gaussian states. Starting from the maximally mixed Gaussian state, the strict damping inequality makes its covariance converge. Gaussian states are continuously determined by their covariance, so this evolution yields a physical, translation-invariant Gaussian stationary state $`\sigma_\eta`$. Strict stability in fact gives uniqueness and relaxation as stated in [1], Proposition 6, although the following limiting argument only needs the existence of this Gaussian stationary state.

At fixed finite $`N`$, $`\sigma_\eta\to\sigma`$ in trace norm as $`\eta\downarrow0`$. Indeed, the density matrices form a compact set. Any convergent subsequence has a parity-invariant limit $`\tau`$; from the regularized stationarity equation $`\mathcal L_\eta(\sigma_\eta)=0`$, $`\mathcal L(\tau)=0`$. Original physical uniqueness forces $`\tau=\sigma`$. Every subsequential limit is therefore the same. Consequently

```math
F_\eta:=\langle\mathrm{FS}_N|\sigma_\eta|\mathrm{FS}_N\rangle\longrightarrow F>0.
```

No estimate uniform in $`N`$ is required. We prove a finite-size inequality for each small positive $`\eta`$ and then take this limit. The resulting finite-size bound retains the original overlap threshold $`F_0`$.

## Exact rational degree for the occupations

Column-vectorize the stationary Bloch-Lyapunov equation. The coefficient matrix is

```math
\mathcal K_\eta(k)
=I_2\otimes X_\eta(k)+X_\eta(-k)\otimes I_2,
\qquad
\mathcal K_\eta(k)\operatorname{vec}C_\eta(k)
=-\operatorname{vec}Y(k).
```

It is a $`4\times4`$ matrix with Laurent degree at most $`S`$ in each entry. Here Laurent degree at most $`D`$ means exponents lie in $`[-D,D]`$. Cramer's rule gives

```math
C_{\eta,\alpha\beta}(k)=\frac{U_{\alpha\beta}(z)}{Q(z)},
\qquad z=e^{ik},
```

Both the determinant $`Q=\det\mathcal K_\eta`$ and every Cramer numerator $`U_{\alpha\beta}`$ have Laurent degree at most $`4S`$. Every determinant term contains four entries of degree at most $`S`$, including the replaced source column. Strict stability ensures $`Q(e^{ik})\ne0`$ at every sampled momentum, so $`Q`$ is not the zero polynomial. This claim does not require the rational extension to be nonsingular away from the physical grid.

For clarity, the occupation is not in general obtained from a single off-diagonal covariance entry. Let $`v=(1,i)^T`$. The Majorana and Fourier conventions above give

```math
\begin{aligned}
n_\eta(k)
&=\frac14v^\dagger[I_2-iC_\eta(-k)]v\\
&=\frac12+
\frac{C_{\eta,12}(k)-C_{\eta,21}(k)
+i\operatorname{tr}C_\eta(k)}4,
\end{aligned}
```

using $`C(-k)=-C(k)^T`$. The trace term matters if $`n(k)\ne n(-k)`$. With the Fourier sign used here, its sign is **plus**. Thus

```math
n_\eta(k)=\frac{P(z)}{Q(z)},
\qquad
\frac{n_\eta(k)}{1-n_\eta(k)}
=\frac{P(z)}{Q(z)-P(z)},
```

and $`P,Q-P`$ both have Laurent degree at most $`D=4S`$.

Set $`k=\pi/2+q`$ and $`x=\tan(q/2)`$, so

```math
z=i\frac{1+ix}{1-ix}.
```

For any Laurent polynomial $`T(z)=\sum_{r=-D}^D t_rz^r`$,

```math
(1+x^2)^D T\!\left(i\frac{1+ix}{1-ix}\right)
=\sum_{r=-D}^D t_ri^r(1+ix)^{D+r}(1-ix)^{D-r}
```

is an ordinary polynomial of degree at most $`2D`$. Apply this to $`P`$ and $`Q-P`$. Their common denominator cancels in the odds, yielding the two polynomials $`A,B`$ in the [scalar converse](range_lower_bound.md#scalar-converse-from-total-occupation-error), each of degree at most $`8S`$. Hence

```math
d=\deg A+\deg B\le16S.
```

For sufficiently small $`\eta`$, $`F_\eta>0`$. Neither $`A`$ nor $`B`$ can be identically zero: that would force all sampled occupations to be respectively 0 or 1, incompatible with positive overlap with the half-filled target. Repeated roots, common polynomial factors, and artificial factors at $`x=\pm i`$ are harmless; the root count is an upper bound before any cancellation. Actual roots at a selected positive or negative grid point are handled by the [discrete root budget lemma](range_lower_bound.md#lemma-2-discrete-root-budget-after-at-most-two-deletions).

## Pair-block fidelity implies the needed aggregate error budget

For a translation-invariant Gaussian state, normal momentum correlations vanish unless $`k=k'`$, and anomalous correlations vanish unless $`k=-k'`$. Its covariance is therefore block diagonal over the unordered pairs $`\{k,-k\}`$, together with the self-conjugate modes $`0,\pi`$. After choosing a fixed fermionic mode ordering, the even Gaussian density matrix factors over these blocks:

```math
\sigma_\eta=\bigotimes_B\sigma_{\eta,B}.
```

One way to justify this factorization, including singular Gaussian states, is to compare Wick moments: block-diagonal covariance gives all even moments of the product of its Gaussian marginals, while all odd block moments vanish. These moments determine the density matrix. Equivalently, full-rank Gaussian exponentials split into commuting quadratic block terms and the general case follows by a limit.

The target factors in the same blocks. Since $`\cos(-k)=\cos k`$, a two-mode block target is either $`|00\rangle`$ or $`|11\rangle`$. Let $`\Pi_B`$ be its rank-one target projector and $`F_{\eta,B}=\operatorname{Tr}(\sigma_{\eta,B}\Pi_B)`$. Then

```math
F_\eta=\prod_BF_{\eta,B}.
```

If $`P_k`$ is the projector onto the correct occupation of mode $`k\in B`$, then $`\Pi_B\le P_k`$. Therefore its wrong-occupation probability obeys

```math
e_\eta(k)=\operatorname{Tr}[\sigma_{\eta,B}(I-P_k)]
\le1-F_{\eta,B}.
```

Every block contains at most two modes. For $`F_\eta>0`$,

```math
\boxed{
\sum_ke_\eta(k)
\le2\sum_B(1-F_{\eta,B})
\le-2\sum_B\log F_{\eta,B}
=-2\log F_\eta.
}
```

This argument allows pairing coherence within a block. The stronger equality $`F=\prod_k(1-e(k))`$ is not generally valid with pairing and is not used in the general Gaussian converse.

## Application to the range converse

Apply [Lemma 3 of the scalar converse](range_lower_bound.md#scalar-converse-from-total-occupation-error) to $`\sigma_\eta`$, with the pair-block error budget $`E_\eta=-2\log F_\eta`$ and the root count $`d\le16S`$. Dividing its degree lower bound by 16 gives

```math
S\ge
\frac{\Lambda_N[W_N-w_N(-2\log F_\eta)N^{1/3}]_+}
{8\pi^2+32\Lambda_Nw_N}.
```

At fixed $`N`$, the right side is continuous in $`F_\eta>0`$. Taking $`\eta\downarrow0`$ and using $`F\ge F_0`$ therefore proves the [full Gaussian finite-size converse](range_lower_bound.md#model-fidelity-and-finite-size-statement). The asymptotics of the finite-grid quantities and $`S\le2R`$ give the stated common-radius lower bound. No exchange of the large-size and vanishing-noise limits is needed.

## Separate gain and loss

Write the separate jump families as

```math
L^-_{\mu,x}=\sum_r u_{\mu,r}c_{x+r},
\qquad L^+_{\nu,x}=\sum_r v_{\nu,r}c^\dagger_{x+r},
```

with offsets in $`[-R_J,R_J]`$. With the fixed Fourier convention, define

```math
u_\mu(k)=\sum_r u_{\mu,r}e^{ikr},
\qquad v_\nu(k)=\sum_r v_{\nu,r}e^{-ikr}.
```

Unitary Fourier mixing of the translated jump labels then gives rates

```math
a(k)=\sum_\nu|v_\nu(k)|^2,
\qquad b(k)=\sum_\mu|u_\mu(k)|^2.
```

Each is a nonnegative trigonometric polynomial of degree at most $`2R_J`$, irrespective of channel count. A number-conserving, translation-invariant quadratic $`H`$ is diagonal in $`n_k=c_k^\dagger c_k`$. Thus stationary occupations are

```math
n(k)=\frac{a(k)}{a(k)+b(k)}.
```

Physical uniqueness implies $`a(k)+b(k)>0`$ for every sampled momentum. Otherwise the conserved, undamped occupation of that mode yields distinct physical stationary states. With positive sums, the stationary density is the product of the one-mode gain/loss stationary densities, so

```math
F=\prod_k(1-e(k)),\qquad\sum_ke(k)\le-\log F\le-\log F_0.
```

The odds are $`a/b`$. The Möbius conversion above with $`D=2R_J`$ makes numerator and denominator polynomials of degree at most $`4R_J`$, hence $`d\le8R_J`$. If either rate polynomial vanished identically, positive target overlap would be impossible. The [scalar converse](range_lower_bound.md#scalar-converse-from-total-occupation-error) with $`E=-\log F_0`$, divided by 8, gives the separate gain/loss finite-size bound.

## Scope and literature

The full Gaussian reduction charges Hamiltonian range as well as jump range. An unrestricted long-range pairing Hamiltonian is outside a jump-radius-only conclusion. By contrast, a translation-invariant number-conserving Hamiltonian cannot change the stationary momentum populations in the separate gain/loss subclass.

Physical-sector uniqueness is the only uniqueness assumption used in the limiting argument. The onsite regularization supplies an invertible Bloch equation without assuming that physical uniqueness makes every odd operator decay. No bound uniform in system size is needed on that regularization limit.

This is a stationary spatial converse. It allows arbitrarily weak rates and does not supply a preparation-time bound. The matching upper construction and its time cost are given in [reservoir construction](reservoir_construction.md) and [preparation costs](preparation_costs.md).

The covariance evolution, Gaussianity, and Bloch-Lyapunov rationality are established ingredients. Their role here is to give an explicit degree bound for the total-error argument, with one fixed physical mode per cell and all coherent range charged. See also the [related-work account](../references/RELATED_WORK.md).

1. T. Barthel and Y. Zhang, *Solving quasi-free and quadratic Lindblad master equations for open fermionic and bosonic systems*, J. Stat. Mech. (2022) 113101. [arXiv:2112.08344v5](https://arxiv.org/pdf/2112.08344). Proposition 1 / Eq. (15) gives covariance evolution; Proposition 5 gives Gaussian stationary states; Proposition 6 gives strict-stability relaxation; Sec. V.1 discusses Gaussianity. Their Majoranas obey $`\{w_i,w_j\}=\delta_{ij}`$; the normalization and the sign of the second Majorana have been converted explicitly above.
2. Y. Zhang and T. Barthel, *Criticality and Phase Classification for Quadratic Open Quantum Many-Body Systems*, Phys. Rev. Lett. **129**, 120401 (2022). [DOI:10.1103/PhysRevLett.129.120401](https://doi.org/10.1103/PhysRevLett.129.120401); [arXiv:2204.05346v2](https://arxiv.org/pdf/2204.05346). Equations (6)–(8) establish the Bloch-Lyapunov rationality used here.
