# A finite-range reservoir with finite coefficient precision

The upper bound uses two translated jump families. Their Fourier amplitudes are normalized polynomials in $`\cos k`$. Geometrically spaced roots make the unwanted occupation small on both sides of the Fermi surface. Normalization keeps the rates bounded, and a quantitative rounding rule makes the coefficient precision explicit.

The polynomial mechanism is inherited from classical rational approximation and closely related Gaussian-state constructions. See the [attribution and comparison](../references/RELATED_WORK.md). The purpose here is to realize the filter as a positive Lindblad generator and account for its physical parameters.

## Parameters and amplitudes

Fix $`N=4M+2`$, a requested final infidelity $`0<\epsilon<1`$, and a rate scale $`\Gamma>0`$. Put

```math
q_0=\tanh(1/2),\qquad
\kappa=-\log q_0,
```

and choose

```math
s=\left\lceil
\max\left\{
2,\ \log(N/2)+1,\
1+\frac{\log(4N/\epsilon)}{2\kappa}
\right\}
\right\rceil,
\qquad m=s^2.
```

Define

```math
r_j=e^{-j/s},\qquad
p(x)=\prod_{j=0}^{m-1}(x+r_j),
\qquad
h(k)=\frac{p(\cos k)}{p(1)}.
```

The gain and loss amplitudes are $`\sqrt{\Gamma/2}\,h(k)`$ and $`\sqrt{\Gamma/2}\,h(k+\pi)`$. Thus

```math
a(k)=\frac{\Gamma}{2}h(k)^2,\qquad
b(k)=\frac{\Gamma}{2}h(k+\pi)^2,
\qquad
g(k)=a(k)+b(k).
```

Both amplitudes are Laurent polynomials with exponents from $`-m`$ to $`m`$, so they are implemented by actual linear jumps of radius $`m`$. The [model convention](model.md) gives

```math
\frac{d}{dt}\langle n_k\rangle
=a(k)-g(k)\langle n_k\rangle,
\qquad
n_\infty(k)=\frac{a(k)}{g(k)}.
```

Use the fixed nearest-neighbor target Hamiltonian. It commutes with every momentum occupation and leaves these equations unchanged.

For $`-1\le x\le1`$, every factor satisfies $`|x+r_j|\le1+r_j`$. Hence $`|h(k)|\le1`$ and $`g(k)\le\Gamma`$. At least one of $`\cos k`$ and $`-\cos k`$ is nonnegative, where $`p`$ is strictly positive. Therefore $`g(k)>0`$ for every real momentum.

Positive mode rates give a unique attracting stationary state. Its occupation errors are

```math
e_\infty(k)=
\begin{cases}
1-n_\infty(k),&\cos k>0,\\
n_\infty(k),&\cos k<0,
\end{cases}
\qquad
F_\infty=\prod_{k\in K_N}(1-e_\infty(k)).
```

## Stationary error bound

For every

```math
e^{-(m-1)/s}\le x\le1,
```

at least $`s-1`$ of the roots $`r_j`$ lie within a factor $`e`$ of $`x`$. To see this, write $`x=e^{-t}`$ with $`0\le t\le(m-1)/s`$. The root exponents form a grid of spacing $`1/s`$. Intersecting the interval $`[t-1,t+1]`$ with the available exponent range always leaves an interval of length at least one. It contains at least $`s-1`$ grid points, including the endpoint cases.

For each such root,

```math
\frac{|r_j-x|}{r_j+x}
=\left|\tanh\frac{\log(r_j/x)}2\right|
\le q_0.
```

Every other factor is at most one. Consequently,

```math
\left|\frac{p(-x)}{p(x)}\right|
\le q_0^{\,s-1}.
```

The smallest sampled absolute cosine is

```math
\min_{k\in K_N}|\cos k|
=\sin(\pi/N)\ge\frac2N.
```

Our parameter choice ensures both

```math
s-\frac1s\ge\log(N/2),
\qquad
2\kappa(s-1)\ge\log(4N/\epsilon).
```

The first condition places every sampled absolute cosine in the root estimate's domain. The second yields

```math
e_\infty(k)\le q_0^{\,2(s-1)},
\qquad
\sum_k e_\infty(k)\le\frac{\epsilon}{4}.
```

The operator product defining the target is a classical product for this stationary state, so

```math
F_\infty\ge1-\sum_k e_\infty(k)
\ge1-\frac{\epsilon}{4}.
```

Since $`s=O(\log(N/\epsilon))`$, the jump radius is $`m=O(\log^2(N/\epsilon))`$.

## A nonzero amplitude margin

A finite precision statement needs more than formal positivity. Define

```math
u=\exp\!\left[-\frac{s^3+s+2}{2}\right].
```

For nonnegative $`x`$, $`p(x)\ge p(0)`$, and

```math
p(0)=e^{-(s^3-s)/2},
\qquad
\log p(1)
=\sum_{j=0}^{s^2-1}\log(1+e^{-j/s})
\le\frac1{1-e^{-1/s}}\le s+1.
```

At least one of the two polynomial arguments is nonnegative. Therefore

```math
\left\|\bigl(h(k),h(k+\pi)\bigr)\right\|_2\ge u,
\qquad
g(k)\ge\frac{\Gamma}{2}u^2.
```

This is uniform in real momentum. It is deliberately conservative, but it prevents coefficient rounding from eliminating damping at a sampled mode.

## Normalized Fourier coefficients

Write

```math
h(k)=\sum_{r=-m}^{m}\alpha_r e^{irk}.
```

The coefficients are real, nonnegative and symmetric, and they sum to one. Each factor has the expansion

```math
\frac{\cos k+r_j}{1+r_j}
=\frac{r_j}{1+r_j}
+\frac{e^{ik}+e^{-ik}}{2(1+r_j)}.
```

Its three Fourier coefficients are a probability distribution on the offsets $`\{-1,0,1\}`$. Multiplication convolves those distributions, giving

```math
\alpha_r\ge0,\qquad
\alpha_{-r}=\alpha_r,\qquad
\sum_{r=-m}^{m}\alpha_r=1.
```

The loss coefficients are $`(-1)^r\alpha_r`$. Thus $`m+1`$ independent nonnegative real numbers specify both families. The normalized coefficients can be formed by positive convolution, avoiding an unnormalized polynomial with a very large dynamic range.

For example, a real-space realization is

```math
L_x^+
=\sqrt{\frac{\Gamma}{2}}
\sum_{r=-m}^{m}\alpha_r c_{x+r}^\dagger,
\qquad
L_x^-
=\sqrt{\frac{\Gamma}{2}}
\sum_{r=-m}^{m}(-1)^r\alpha_r c_{x+r}.
```

The coefficient symmetry makes the Fourier sign convention immaterial to the stated amplitudes. After periodization, repeated site offsets can be combined.

## Dyadic rounding theorem

Let $`K=2m+1`$ and choose the integer

```math
b_{\mathrm{prec}}=
\left\lceil
\frac{s^3+s+2}{2\log2}
+\log_2\frac{4\sqrt2\,KN}{\epsilon}
\right\rceil.
```

Round each independent coefficient downward and share it with its symmetric partner:

```math
\widehat\alpha_r
=2^{-b_{\mathrm{prec}}}
\left\lfloor2^{b_{\mathrm{prec}}}\alpha_r\right\rfloor,
\qquad
\widehat\alpha_{-r}=\widehat\alpha_r.
```

Use the resulting polynomial $`\widehat h(k)`$ in the same two jump families. The coefficients remain nonnegative, with sum at most one. Therefore the rounded physical rates still obey $`\widehat g(k)\le\Gamma`$.

The uniform amplitude error satisfies

```math
|\widehat h(k)-h(k)|
\le K2^{-b_{\mathrm{prec}}}
\le\frac{\epsilon u}{4\sqrt2\,N}.
```

Set $`v=(h(k),h(k+\pi))`$ and $`\widehat v=(\widehat h(k),\widehat h(k+\pi))`$. With $`\nu=\epsilon/(4N)`$,

```math
\|\widehat v-v\|_2
\le\nu u\le\nu\|v\|_2.
```

It follows that

```math
(1-\nu)^2g(k)
\le\widehat g(k)
\le(1+\nu)^2g(k).
```

In particular, all rounded rates are positive and

```math
\widehat g_{\min}
\ge\frac{\Gamma}{4}
e^{-s^3-s-2}.
```

The constant is loose: $`N\ge2`$ and $`\epsilon<1`$ imply $`(1-\nu)^2>1/2`$.

To control stationary occupations, for nonzero vectors $`v,w\in\mathbb C^2`$ use

```math
\left|
\frac{|v_1|^2}{\|v\|_2^2}
-\frac{|w_1|^2}{\|w\|_2^2}
\right|
\le
\sqrt{1-\left|
\left\langle\frac v{\|v\|_2},\frac w{\|w\|_2}\right\rangle
\right|^2}
\le\frac{\|v-w\|_2}{\|v\|_2}.
```

The first inequality is the measurement bound for pure-state trace distance. The second follows by projecting $`v`$ onto the orthogonal complement of $`w`$. Thus

```math
|\widehat n_\infty(k)-n_\infty(k)|
\le\frac{\epsilon}{4N}.
```

Combining rounding error with the ideal error budget gives

```math
\sum_k\widehat e_\infty(k)\le\frac{\epsilon}{2},
\qquad
\widehat F_\infty\ge1-\frac{\epsilon}{2}.
```

The precision cost is

```math
b_{\mathrm{prec}}
=O\!\left(\log^3\frac N\epsilon\right),
\qquad
(m+1)b_{\mathrm{prec}}
=O\!\left(\log^5\frac N\epsilon\right).
```

These are sufficient absolute-precision and coefficient-description bounds. They are not lower bounds on implementation precision.

## A finite procedure at rounding boundaries

The mathematical floor rule need not be implemented by deciding whether a transcendental coefficient lies exactly on a binary boundary. Use $`B=b_{\mathrm{prec}}+2`$ fractional bits instead. Compute a certified interval $`[\ell_r,u_r]`$ containing $`\alpha_r`$ with width at most $`2^{-B}`$, and program

```math
\widehat\alpha_r
=\max\left\{
0,\ 2^{-B}\left\lfloor2^B\ell_r\right\rfloor
\right\}.
```

Then

```math
0\le\widehat\alpha_r\le\alpha_r,
\qquad
\alpha_r-\widehat\alpha_r
\le2^{1-B}<2^{-b_{\mathrm{prec}}}.
```

All previous bounds remain valid. Use the same interval and value for symmetric partners. The coefficients are finite products and sums of computable exponentials of rational numbers. Certified intervals can therefore be narrowed to the stated width without resolving equality at a rounding boundary.

The common factor $`\sqrt{\Gamma/2}`$ sets the physical rate units. Alternating phases are exact signs in this model. The bit bound concerns the normalized amplitudes; it does not claim that ordinary double precision resolves their near-Fermi cancellation.

Continue to [preparation time and the exact worst-case curve](preparation_costs.md). The [verification guide](../verification/README.md) describes the high-precision rounding checks and their distinction from interval certification.

