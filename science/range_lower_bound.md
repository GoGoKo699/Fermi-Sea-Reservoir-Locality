# Finite-size range lower bound

Fixed overlap with an entire Fermi sea imposes a bounded sum of momentum-occupation errors. It does not impose the same small error on every mode. This account proves a rational-degree lower bound directly from that aggregate constraint, including the exceptional modes and the possible proximity of polynomial roots to sampled momenta.

The [Gaussian stationarity account](gaussian_stationarity.md) converts this scalar degree bound into a bound on reservoir range. The complete operational assumptions are also collected in the [model](model.md). All logarithms are natural.

## Model, fidelity, and finite-size statement

There are $`N=4M+2`$ spinless fermionic modes on a periodic ring, with one mode $`c_x`$ per site and $`x\in\mathbb Z_N`$. The Fourier convention is

```math
c_k=N^{-1/2}\sum_{x=0}^{N-1}e^{-ikx}c_x,
\qquad k\in K_N:=\{2\pi m/N:m\in\mathbb Z_N\}.
```

The target $`|\mathrm{FS}_N\rangle`$ fills exactly the momenta with $`\cos k>0`$. It is the unique ground state of

```math
H_{\rm tar}=-\sum_x(c_x^\dagger c_{x+1}+c_{x+1}^\dagger c_x).
```

The choice $`N=4M+2`$ excludes a sampled momentum at either Fermi point and gives exactly $`N/2`$ occupied target modes.

Consider a time-independent, translation-invariant Lindblad generator

```math
\mathcal L(\rho)=-i[H,\rho]
 +\sum_{\mu,x}\mathcal D[L_{\mu,x}](\rho),
\qquad
\mathcal D[L](\rho)=L\rho L^\dagger-\tfrac12\{L^\dagger L,\rho\},
```

where $`H`$ is quadratic, may contain pairing, and has coupling range $`R_H`$. Each jump is linear,

```math
L_{\mu,x}=\sum_{r=-R_J}^{R_J}
\left(u_{\mu,r}c_{x+r}+v_{\mu,r}c_{x+r}^\dagger\right).
```

There may be arbitrarily many jump families, and their coefficients and number may depend on $`N`$. Site indices are periodic. Ranges refer to an explicit finite-support representation before periodization; aliases on a small ring do not increase the bounds on its Laurent degrees. There are no additional persistent modes per cell. Define the charged range

```math
S:=\max\{R_H,2R_J\},\qquad R:=\max\{R_H,R_J\},
\quad\text{so } S\le 2R.
```

A physical density matrix here means one commuting with total fermion parity. This includes projectors onto odd-parity vectors, such as the present target with $`N/2=2M+1`$ particles. It does not mean restriction to the even-particle Hilbert subspace.

Assume that the generator has a unique physical stationary state $`\sigma`$, and

```math
F:=\langle\mathrm{FS}_N|\sigma|\mathrm{FS}_N\rangle\ge F_0>0.
```

The overlap convention is the squared pure-state fidelity. Global attraction from every physical initial state can be imposed as an operational preparation requirement; the converse below uses only uniqueness of the physical stationary state. No lower bound on a spectral gap or jump strength is assumed.

For $`N\ge1026`$, define

```math
\begin{aligned}
a_N&:=\lceil N^{2/3}\rceil,
& b_N&:=\lfloor N/8\rfloor,
& \delta_N&:=N^{-1/3},\\
x_j&:=\tan\!\left(\frac{(j+1/2)\pi}{N}\right),
& w_N&:=\log\frac{x_{a_N+1}}{x_{a_N}},
& W_N&:=\log\frac{x_{b_N+1}}{x_{a_N}},\\
\Lambda_N&:=2\log\frac{1-\delta_N}{\delta_N}.
\end{aligned}
```

Here $`a_N\le b_N`$, $`w_N,W_N,\Lambda_N>0`$. Write $`[t]_+=\max\{t,0\}`$.

**Theorem 1: full Gaussian converse.** For the above model and overlap criterion,

```math
\boxed{
S\ge
\frac{\Lambda_N
\left[W_N-(-2\log F_0)\,w_N N^{1/3}\right]_+}
{8\pi^2+32\Lambda_N w_N}.
}
```

In particular, for every fixed $`F_0\in(0,1)`$,

```math
S\ge\left(\frac1{36\pi^2}+o(1)\right)(\log N)^2,
\qquad
R\ge\left(\frac1{72\pi^2}+o(1)\right)(\log N)^2.
```

These constants are deliberately unoptimized. The full Gaussian bound above, which involves only explicit elementary functions and integer rounding, is the finite-$`N`$ statement; no unspecified threshold depending on $`F_0`$ is needed to use it. Its positive part correctly allows a vacuous bound for small sizes or very small prescribed overlap.

**Theorem 2: separate gain/loss converse.** If the jumps instead consist of separate translated creation and annihilation families, each of radius $`R_J`$, and $`H`$ is any translation-invariant number-conserving quadratic Hamiltonian, then

```math
\boxed{
R_J\ge
\frac{\Lambda_N
\left[W_N-(-\log F_0)\,w_N N^{1/3}\right]_+}
{4\pi^2+16\Lambda_N w_N}.
}
```

Thus $`R_J\ge[1/(18\pi^2)+o(1)](\log N)^2`$. The Hamiltonian range need not be charged in this special case because the Hamiltonian commutes with every momentum occupation. The full Gaussian bound does charge it: a jump-only statement with an unrestricted pairing Hamiltonian is not proved here.

## Root-potential estimates

### Lemma 1: continuous root budget

For $`z\in\mathbb C`$, put

```math
h_z(x):=\left|\log\left|\frac{x+z}{x-z}\right|\right|,
\qquad x>0.
```

At a real pole the value is $`+\infty`$; the resulting singularity is integrable. If $`z=0`$ or $`\mathrm{Re}z=0`$, the function is identically zero. Otherwise $`h_z`$ is nonnegative, increases on $`(0,|z|)`$, decreases on $`(|z|,\infty)`$, and

```math
\int_0^\infty h_z(x)\,\frac{dx}{x}\le\frac{\pi^2}{2}.
```

**Proof.** Replacing $`z`$ by $`-z`$ leaves $`h_z`$ unchanged. Set $`z=\alpha+i\beta`$, with $`\alpha>0`$, and $`r=|z|`$. Then

```math
h_z(x)=\frac12\log
\frac{x^2+r^2+2\alpha x}{x^2+r^2-2\alpha x},
\qquad
h_z'(x)=
\frac{2\alpha(r^2-x^2)}{(x^2+r^2)^2-4\alpha^2x^2}.
```

This proves unimodality, with the real-root singularity understood separately. Since $`0<\alpha\le r`$, the first expression is at most $`h_r(x)`$. Scaling reduces its integral to the positive real root at 1. Substitution $`x\mapsto1/x`$ in the integral above 1, followed by the nonnegative power series below 1, gives

```math
\begin{aligned}
\int_0^\infty\log\left|\frac{x+1}{x-1}\right|\frac{dx}{x}
&=2\int_0^1\log\frac{1+x}{1-x}\frac{dx}{x}\\
&=4\sum_{m=0}^\infty\frac1{(2m+1)^2}
=\frac{\pi^2}{2}.
\end{aligned}
```

This proves the continuous root budget. $`\square`$

### Lemma 2: discrete root budget after at most two deletions

Let $`x_{a-1}<x_a<\cdots<x_{b+1}`$ be positive numbers and let

```math
w_j:=\log(x_{j+1}/x_j),\qquad a-1\le j\le b,
```

be nonincreasing in $`j`$. For each root $`z`$, there is a set $`D_z\subseteq\{a,\ldots,b\}`$ with $`|D_z|\le2`$ such that

```math
\sum_{j\in\{a,\ldots,b\}\setminus D_z}w_jh_z(x_j)
\le\frac{\pi^2}{2}.
```

The bound remains true if any additional nodes are removed.

**Proof with boundary prescription.** If $`h_z=0`$, take $`D_z=\varnothing`$. Otherwise put $`r=|z|`$. If $`r<x_{a-1}`$, use the decreasing branch throughout and make no deletion. If $`r\ge x_{b+1}`$, use the increasing branch throughout and make no deletion. In the remaining case choose the unique $`\ell\in\{a-1,\ldots,b\}`$ with $`x_\ell\le r<x_{\ell+1}`$, and delete

```math
D_z=\{\ell,\ell+1\}\cap\{a,\ldots,b\}.
```

For every retained index on the increasing branch,

```math
w_jh_z(x_j)\le\int_{x_j}^{x_{j+1}}h_z(x)\,\frac{dx}{x}.
```

For every retained index on the decreasing branch, use $`w_j\le w_{j-1}`$ to obtain

```math
w_jh_z(x_j)\le w_{j-1}h_z(x_j)
\le\int_{x_{j-1}}^{x_j}h_z(x)\,\frac{dx}{x}.
```

All assigned integration cells have disjoint interiors: in the interior-peak case, the increasing cells end no later than $`x_\ell`$, whereas the decreasing cells begin no earlier than $`x_{\ell+1}`$. Their sum is bounded by Lemma 1. A pole exactly at a sampled node is always deleted. A pole at an outer integration endpoint has only an integrable logarithmic singularity. Nonnegativity proves the assertion about additional deletions. $`\square`$

The deletions are essential. Without them, a root arbitrarily close to a grid node produces an arbitrarily large discrete term, even though its continuous integral remains bounded.

## Scalar converse from total occupation error

This section is a scalar approximation statement; it makes no Gaussian assumption.

Let $`n(k)\in[0,1]`$ be occupations on $`K_N`$, with wrong-occupation probabilities

```math
e(k)=
\begin{cases}
1-n(k),&\cos k>0,\\
n(k),&\cos k<0,
\end{cases}
\qquad
\sum_{k\in K_N}e(k)\le E.
```

Suppose that, at the grid points used below, the odds are represented by a rational function

```math
\frac{n(\pi/2+q)}{1-n(\pi/2+q)}
=\frac{A(x)}{B(x)},\qquad x=\tan(q/2),
```

with nonzero complex polynomials $`A,B`$. Zeros and infinite odds may occur before the root deletions. Let

```math
d:=\deg A+\deg B
```

count the total finite-root multiplicity, including common roots if the ratio has not been reduced.

**Lemma 3: aggregate error forces a root budget.** With the finite-grid definitions above,

```math
\boxed{
d\ge
\frac{\Lambda_N[W_N-w_NE N^{1/3}]_+}
{\pi^2/2+2\Lambda_N w_N}.
}
```

**Proof.** Write $`a=a_N,b=b_N`$. Both momenta

```math
k_j^-:=\pi/2-q_j,\qquad k_j^+:=\pi/2+q_j,
\qquad q_j=(2j+1)\pi/N,
```

belong to $`K_N`$: $`\pi/2=(2M+1)\pi/N`$, so their numerators are even multiples of $`\pi/N`$. For $`a\le j\le b`$, the minus mode is inside the Fermi sea and the plus mode is outside. All these selected modes are distinct.

The grid $`x_j`$ defined above has decreasing logarithmic weights. Indeed, if $`g(t)=\log\tan t`$, then $`g'(t)=2/\sin(2t)`$ decreases on $`(0,\pi/4)`$. The entire interval from $`t_{a-1}=(a-1/2)\pi/N`$ to $`t_{b+1}=(b+3/2)\pi/N`$ lies in that range for the stipulated $`N`$. In particular $`w_j\le w_a=w_N`$, and

```math
\sum_{j=a}^b w_j=W_N.
```

To verify that the chosen interval exists without an asymptotic qualification, for $`N\ge1024`$ one has $`N^{2/3}\le N/10`$. Thus $`a\le N/10+1\le N/8-1\le b`$, and $`t_{b+1}\le\pi/8+3\pi/(2N)<\pi/4`$.

Delete the union of the sets in Lemma 2 for all roots of $`A`$ and $`B`$. This removes at most $`2d`$ nodes. In particular, neither $`A(\pm x_j)`$ nor $`B(\pm x_j)`$ vanishes at any retained node: a zero at either sign has modulus $`x_j`$ and is included in the relevant root deletion.

Also delete a node whenever either $`e(k_j^-)>\delta_N`$ or $`e(k_j^+)>\delta_N`$. There are at most $`E/\delta_N=EN^{1/3}`$ such nodes, because each contains at least one distinct mode whose error exceeds $`\delta_N`$. Let $`G`$ be the nodes surviving both types of deletion. Their weight satisfies

```math
\sum_{j\in G}w_j
\ge\left[W_N-w_N(2d+EN^{1/3})\right]_+.
```

At every $`j\in G`$, the retained finite, positive odds obey

```math
\begin{aligned}
g_j
&:=\log\frac{n(k_j^-)}{1-n(k_j^-)}
-\log\frac{n(k_j^+)}{1-n(k_j^+)}\\
&\ge2\log\frac{1-\delta_N}{\delta_N}=\Lambda_N.
\end{aligned}
```

Factor $`A`$ and $`B`$. Their leading coefficients cancel in each ratio at $`-x`$ and $`x`$. Since the sampled odds are positive,

```math
g_j
=\log\left|\frac{A(-x_j)}{A(x_j)}\right|
-\log\left|\frac{B(-x_j)}{B(x_j)}\right|
\le\sum_{z\in\mathcal Z(A)\sqcup\mathcal Z(B)}h_z(x_j),
```

with multiplicities. This step needs neither real polynomial coefficients nor positivity away from the sampled grid. Lemma 2, still valid after the extra deletions, gives

```math
\Lambda_N
\left[W_N-w_N(2d+EN^{1/3})\right]_+
\le\sum_{j\in G}w_jg_j
\le\frac{\pi^2}{2}d.
```

Dropping the positive part on the left, collecting the terms proportional to $`d`$, and then using $`d\ge0`$, proves the stated root-degree bound. $`\square`$

### Asymptotic form

At fixed $`E`$,

```math
\begin{aligned}
W_N&=\tfrac13\log N+
\log\frac{\tan(\pi/8)}{\pi}+o(1),\\
w_N&=(1+o(1))N^{-2/3},\\
\Lambda_N&=\tfrac23\log N+o(1).
\end{aligned}
```

Consequently $`w_NEN^{1/3}=o(1)`$, $`\Lambda_Nw_N=o(1)`$, and Lemma 3 gives

```math
d\ge\left(\frac4{9\pi^2}+o(1)\right)(\log N)^2.
```

Unlike a proof that first assumes uniform error $`O(1/N)`$, this argument permits an arbitrary set of bad modes consistent with the actual total-error budget.

## From the scalar lemma to reservoir range

The [Gaussian reduction](gaussian_stationarity.md#application-to-the-range-converse) supplies

```math
d\le16S,\qquad E=-2\log F_0
```

for the full Gaussian model, after an onsite-noise regularization and a limit at each fixed size. Dividing Lemma 3 by 16 gives Theorem 1. In the [separate gain/loss subclass](gaussian_stationarity.md#separate-gain-and-loss), the stronger bounds are

```math
d\le8R_J,\qquad E=-\log F_0,
```

which give Theorem 2.

The finite-size proof keeps the deleted weight explicitly and absorbs the root-deletion term algebraically. It does not assume that the degree is small relative to the grid. Complex and repeated roots, common factors, exact sample roots, roots outside the sampled interval, and arbitrary bad modes consistent with the total-error budget are all covered.

Together with the [positive-rate construction](reservoir_construction.md), the converse gives the sharp spatial order. It does not imply a fast preparation protocol; the [preparation-cost account](preparation_costs.md) treats time separately.

## Attribution

The logarithm-squared degree scale is part of classical rational approximation. Sherstov's sharp discrete uniform approximation results already imply that scale for uniformly inverse-polynomial sign error on an integer grid. The argument above explicitly treats a tangent grid under a total occupation-error constraint, using root deletions to control discrete singularities.

Franco-Rubio and Cirac study the same Fermi sea through Gaussian matrix product states with rational occupations. Their rigorous result gives a superlogarithmic virtual-mode requirement, while the logarithm-squared behavior appears in their heuristic and constructive analysis. The [related-work account](../references/RELATED_WORK.md) explains the relation to that result and to exact local-stabilization obstructions.

- A. A. Sherstov, *The Intersection of Two Halfspaces Has High Threshold Degree*, SIAM J. Comput. **42**, 2329–2374 (2013). [DOI:10.1137/100785260](https://doi.org/10.1137/100785260); [author-hosted primary manuscript](https://web.cs.ucla.edu/~sherstov/pdf/hshs.pdf).
- A. Franco-Rubio and J. I. Cirac, *Gaussian matrix product states cannot efficiently describe critical systems*, Phys. Rev. B **106**, 235136 (2022). [DOI:10.1103/PhysRevB.106.235136](https://doi.org/10.1103/PhysRevB.106.235136); [arXiv:2204.02478](https://arxiv.org/abs/2204.02478). See the rigorous lower bound, Sec. V, Eq. (18), and Appendix D.
