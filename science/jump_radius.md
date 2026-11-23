# Jump radius with unrestricted pairing Hamiltonians

Consider the periodic one-mode-per-site ring and the quadratic, one-site-translation-invariant Lindblad model in the [model account](model.md). The linear jumps have radius $`R_J`$. The Hamiltonian may contain pairing, with unrestricted coupling range and strength. If the unique physical stationary state has squared overlap at least $`F_0>0`$ with the Fermi sea, then, for $`N=4M+2\ge1026`$,

```math
\boxed{R_J\ge
\frac{\Lambda_N\left[W_N-(-2\log F_0)w_N N^{1/3}\right]_+}
{4\pi^2+16\Lambda_N w_N}.}
```

The [finite-grid quantities](range_lower_bound.md#model-fidelity-and-finite-size-statement) use the sampled momenta on both sides of a Fermi crossing. At fixed $`F_0\in(0,1)`$ the bound is $`R_J\ge (1/(18\pi^2)+o(1))(\log N)^2`$. The [existing gain/loss filters](reservoir_construction.md) attain this order. No rate bound or convergence speed enters the stationary statement.

## The paired covariance and dissipative rates

For a distinct momentum pair $`\{k,-k\}`$, set $`d=(c_k,c_{-k}^\dagger)^T`$. These are canonical annihilators after a particle–hole change of variables on the second mode. Write $`u_\mu(k)=\sum_r u_{\mu,r}e^{ikr}`$ and $`v_\mu(k)=\sum_r v_{\mu,r}e^{ikr}`$. Fourier mixing of the translated jump labels gives the two channels in this pair,

```math
u_\mu(k)d_1+v_\mu(k)d_2,
\qquad
v_\mu(-k)d_1^\dagger+u_\mu(-k)d_2^\dagger.
```

Let $`B`$ and $`G`$ be the loss and gain Gram matrices in this frame and $`D=B+G`$. The translation-invariant quadratic Hamiltonian has the form $`d^\dagger h d`$ on this pair, up to a constant. The canonical anticommutation relations, or the [Gaussian covariance equation](gaussian_stationarity.md#exact-real-space-equation), give the block evolution for $`M_{ij}=\langle d_j^\dagger d_i\rangle`$:

```math
\dot M=-i[h,M]-\tfrac12\{D,M\}+G,
\qquad 0\preceq M\preceq I.
```

A stationary translation-invariant Gaussian covariance can be obtained by averaging over time the covariances along the orbit from the maximally mixed Gaussian state. The physical covariance set is closed and bounded. For each accumulation point of the time averages, the affine covariance equation has zero right-hand side because the covariance endpoint difference divided by elapsed time tends to zero. The Gaussian state with this covariance is fixed by Gaussian evolution. Under physical uniqueness it is the designated stationary state. Translation invariance makes it a [product over momentum pairs and self-conjugate modes](gaussian_stationarity.md#pair-block-fidelity-implies-the-needed-aggregate-error-budget).

## Stationary accuracy transfers to a scalar rate ratio

Diagonalize the stationary $`M`$ with eigenvalues $`m_i`$. The commutator has zero diagonal in that basis, so $`G_{ii}=m_iD_{ii}`$. Positivity of the gain matrix gives $`|G_{ij}|\le\sqrt{G_{ii}G_{jj}}`$. For every vector $`z`$,

```math
z^\dagger Gz
\le\left(\sum_i |z_i|\sqrt{m_i D_{ii}}\right)^2
\le (z^\dagger Mz)\operatorname{Tr}D.
```

Since $`B=D-G`$ has diagonal entries $`(1-m_i)D_{ii}`$, the same argument gives $`B\preceq(\operatorname{Tr}D)(I-M)`$. In the original $`d`$ frame define the scalar rates

```math
\begin{aligned}
a(k)&=G_{11}+B_{22}=\sum_\mu\left(|v_\mu(k)|^2+|v_\mu(-k)|^2\right),\\
b(k)&=B_{11}+G_{22}=\sum_\mu\left(|u_\mu(k)|^2+|u_\mu(-k)|^2\right),\\
g(k)&=a(k)+b(k)=\operatorname{Tr}D.
\end{aligned}
```

Both rates are nonnegative trigonometric polynomials of degree at most $`2R_J`$. If $`g(k)=0`$ on a distinct pair, every jump on that pair vanishes. The pair's physical parity then commutes with the Hamiltonian and every jump, and is conserved. Time averaging the state evolution from each of the two pair-parity sectors yields distinct physical stationary states. Thus physical uniqueness implies $`g(k)>0`$ on every distinct pair.

On an occupied target pair, the covariance target in the $`d`$ frame is $`\operatorname{diag}(1,0)`$. The matrix inequalities give $`b(k)/g(k)\le (1-M_{11})+M_{22}`$. On an empty target pair, they give $`a(k)/g(k)\le M_{11}+(1-M_{22})`$. In both cases the wrong occupation of the scalar score $`a(k)/g(k)`$ is bounded by the sum of the two physical occupation errors. The target pair projector is dominated by either correct-occupation projector. If its squared overlap is $`F_{\{k,-k\}}`$, the summed error is therefore at most $`2(1-F_{\{k,-k\}})`$. Product fidelity bounds the summed scalar error on any collection of distinct pairs by $`-2\log F_0`$. The scalar score measures dissipative selectivity. The actual occupations can also depend on the Hamiltonian.

## Applying the discrete root bound

The momenta in the [scalar converse](range_lower_bound.md#scalar-converse-from-total-occupation-error) are all distinct and lie in $`(0,\pi)`$, so each represents a different physical pair. Assign the scalar score on those momenta and the exact target score elsewhere. For a positive parameter $`\eta`$, use the score $`(a+\eta)/(a+b+2\eta)`$ on the selected momenta. Its odds are $`(a+\eta)/(b+\eta)`$, with nonzero numerator and denominator. The total error tends to an error at most $`-2\log F_0`$ as $`\eta\downarrow0`$ at fixed $`N`$.

The [tangent substitution](gaussian_stationarity.md#exact-rational-degree-for-the-occupations) clears a common denominator and represents each of $`a+\eta`$ and $`b+\eta`$ by a polynomial of degree at most $`4R_J`$. Lemma 3 then bounds $`8R_J`$ from below. Letting $`\eta\downarrow0`$ gives the displayed finite-size bound. The coherent Hamiltonian enters the diagonal stationarity argument only through the vanishing diagonal commutator, independently of its range or strength.

The radius bound also applies under finite-time success from every physical input, since a Gaussian stationary state can still be obtained by covariance averaging and success forces it to have overlap at least $`F_0`$. A pair with zero rate would conserve odd pair parity and prevent success from an odd-pair input. The [paired time converse](https://github.com/GoGoKo699/Fermi-Sea-Preparation-Time/blob/main/science/paired_reservoirs.md) quantifies the stronger restriction from finite-time preparation with bounded rates.
