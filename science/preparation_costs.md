# Preparation time and resource accounting

The [explicit reservoir](reservoir_construction.md) attains the optimal spatial order. This page accounts for its dynamics and coefficient precision. The time statements describe that construction; the [range converse](range_lower_bound.md) applies to the full allowed Gaussian class.

Let $`\widehat a_k,\widehat b_k`$ be the rounded gain and loss rates, $`\widehat g_k=\widehat a_k+\widehat b_k`$, and $`\widehat e_k`$ the stationary wrong-occupation probabilities. The construction proves

```math
\sum_k\widehat e_k\le\frac{\epsilon}{2},
\qquad
0<\widehat g_{\min}\le\widehat g_k\le\Gamma,
\qquad
\widehat g_{\min}
\ge\frac{\Gamma}{4}e^{-s^3-s-2}.
```

An occupation-relaxation rate is defined by the scalar number equation. It is not identified here with the full Liouvillian spectral gap.

## Arbitrary initial states

For each momentum, let $`d_k`$ be the projector onto the wrong occupation:

```math
d_k=
\begin{cases}
1-c_k^\dagger c_k,&\cos k>0,\\
c_k^\dagger c_k,&\cos k<0.
\end{cases}
```

These projectors commute, and the target projector is

```math
P_{\mathrm{FS}}=\prod_k(1-d_k).
```

The operator union bound gives

```math
I-P_{\mathrm{FS}}\le\sum_kd_k.
```

The Heisenberg equation closes on every occupation for any initial state:

```math
\langle d_k\rangle_t
=\widehat e_k+
\bigl(\langle d_k\rangle_0-\widehat e_k\bigr)
e^{-\widehat g_k t}.
```

No Gaussian-state assumption enters this equation. Since $`0\le\langle d_k\rangle_0\le1`$,

```math
\begin{aligned}
1-F_{\rho_0}(t)
&\le\sum_k\widehat e_k+
\sum_k e^{-\widehat g_k t}\\
&\le\frac{\epsilon}{2}
+N e^{-\widehat g_{\min}t}.
\end{aligned}
```

Consequently,

```math
t\ge
\frac{1}{\widehat g_{\min}}\log\frac{2N}{\epsilon}
```

suffices for overlap at least $`1-\epsilon`$ from every physical initial density matrix, including non-Gaussian states and states with coherence between occupation patterns. Substitution of the elementary rate bound gives the fully explicit guarantee

```math
\boxed{
t_{\mathrm{suff}}
=\frac4\Gamma e^{s^3+s+2}
\log\frac{2N}{\epsilon}.
}
```

A trace-distance target follows by using the corresponding squared fidelity-error budget, as described in the [model](model.md).

## Exact worst-case fidelity curve

The occupation-diagonal algebra evolves as independent two-state classical gain/loss chains. This follows directly after Fourier mixing the translated jump labels. The target Hamiltonian is diagonal in occupations. Initial off-diagonal matrix elements do not contribute to the target population.

Starting a mode in the wrong bit gives target-bit probability

```math
(1-\widehat e_k)
\left(1-e^{-\widehat g_k t}\right).
```

Starting it in the correct bit increases that probability by $`e^{-\widehat g_k t}`$. Therefore the complementary Fock state, with every target bit reversed, minimizes the target population. Mixtures cannot lower this minimum, and coherences do not affect it. The complementary state has $`N/2`$ particles and is a legitimate physical state.

It follows that

```math
\boxed{
\inf_{\rho_0}F_{\rho_0}(t)
=
\widehat F_\infty
\prod_{k\in K_N}\left(1-e^{-\widehat g_k t}\right),
\qquad
\widehat F_\infty=\prod_k(1-\widehat e_k).
}
```

Only the diagonal classical subalgebra is used in this proof. No factorization of the full fermionic channel on arbitrary coherences is assumed.

Let $`t_{\mathrm{worst}}(\epsilon)`$ be the earliest time at which every physical initial state has overlap at least $`1-\epsilon`$. Since the worst-case product is at most the factor of any one mode,

```math
\frac{\log(1/\epsilon)}{\widehat g_{\min}}
\le t_{\mathrm{worst}}(\epsilon)
\le\frac{\log(2N/\epsilon)}{\widehat g_{\min}}.
```

The exact product determines the finite-size answer between those bounds. In particular, the construction's worst-case time has the same leading logarithm as its inverse minimum occupation rate at fixed $`\epsilon`$.

## Actual minimum rate of the ideal filter

The polynomial $`p(x)`$ has positive real coefficients. Thus $`p(x)^2+p(-x)^2`$ is an even polynomial with nonnegative coefficients and is increasing with $`|x|`$. The ideal minimum rate on the finite momentum grid is attained at

```math
x_*=\sin(\pi/N),
\qquad
L=\log(1/x_*),
```

and equals

```math
g_{\min}
=\frac{\Gamma}{2p(1)^2}
\left[p(x_*)^2+p(-x_*)^2\right].
```

This is the achieved rate, not the uniform lower bound used to obtain $`t_{\mathrm{suff}}`$.

Define the finite sum

```math
T_s(L)=\sum_{j=0}^{s^2-1}\min(j/s,L).
```

The parameter condition in the construction ensures $`L\le(s^2-1)/s`$. For each factor,

```math
\log(x_*+e^{-j/s})
=-\min(j/s,L)+
\log\left(1+e^{-|j/s-L|}\right).
```

The two geometric tails give

```math
0\le
\sum_{j=0}^{s^2-1}
\log\left(1+e^{-|j/s-L|}\right)
\le2(s+1).
```

Using $`|p(-x_*)|\le p(x_*)`$ and $`0\le\log p(1)\le s+1`$ yields

```math
2T_s(L)-4(s+1)
\le\log\frac{\Gamma}{g_{\min}}
\le2T_s(L)+2(s+1)+\log2.
```

With $`J=\lfloor sL\rfloor`$, the sum is explicit:

```math
\begin{aligned}
T_s(L)
&=\frac{J(J+1)}{2s}+(s^2-J-1)L\\
&=s^2L-\frac{sL^2}{2}-\frac L2+O(1/s).
\end{aligned}
```

For fixed accuracy and $`s/\log N\to c\ge1`$,

```math
\boxed{
\log\frac{\Gamma}{g_{\min}}
=\left(2c^2-c+o(1)\right)(\log N)^3.
}
```

The stated parameter choice has $`c=1`$. The [pointwise rounding bound](reservoir_construction.md) changes every rate by a factor between $`(1-\nu)^2`$ and $`(1+\nu)^2`$, where $`\nu=\epsilon/(4N)`$. It therefore preserves this asymptotic rate law. The worst-case preparation time obeys

```math
\log\!\left(\Gamma t_{\mathrm{worst}}(\epsilon)\right)
=(1+o(1))(\log N)^3
```

for that parameter choice and fixed $`\epsilon`$.

The result establishes actual slowness of this explicit spatially optimal construction. A reservoir with different coefficients might improve its time cost; the present converse does not settle that optimization.

## Quantitative finite examples

The following high-precision numerical calculations use downward-rounded coefficients and target infidelity $`\epsilon=0.1`$. All logarithms in the time columns are natural.

| Sites | Parameter | Formal radius | Fractional bits | Exact worst-case log time | Actual-rate union bound | Elementary guarantee |
|---:|---:|---:|---:|---:|---:|---:|
| 66 | 7 | 49 | 273 | 222.51754 | 223.19492 | 355.35834 |
| 258 | 7 | 49 | 275 | 283.97402 | 284.82512 | 355.53207 |
| 1026 | 8 | 64 | 400 | 458.45680 | 459.45760 | 525.68177 |

“Log time” means $`\log(\Gamma t)`$. The exact worst-case values are numerical roots of the product formula. The next column uses the actual minimum rate in the union bound. The final column uses the elementary lower rate guarantee. The distinction matters even at these modest sizes.

At $`N=66`$, the formal Laurent radius exceeds half the ring, so periodic offsets can be combined. That row checks precision and dynamics; it is not an efficient finite-size radius design or a measurement of the optimal radius.

The [reproducibility guide](../verification/README.md) gives the commands and diagnostic scope. The high-precision computations are numerical checks, not interval certificates of their output.

## Resource summary

| Resource | What is established |
|---|---|
| Spatial reach | A matching common-radius order at fixed whole-state overlap, optimized over the specified stationary Gaussian generators. |
| Distinct jump types | Two translated families. Their translates give the physical jump list across the ring. |
| Independent coefficients | Radius plus one real nonnegative numbers, reused by translation and symmetry; loss uses alternating signs. |
| Coefficient magnitudes | Normalized coefficients are bounded and sum to at most one after rounding. |
| Absolute precision | A sufficient cubic-logarithmic fractional-bit count per independent normalized coefficient. |
| Specification storage | A sufficient fifth-power logarithmic bit count for the distinct translation-invariant coefficient list. |
| Rate normalization | Every momentum occupation rate is at most the specified scale. |
| Time | The explicit construction has a cubic-logarithmic exponent in its worst-case preparation time at fixed accuracy. |

These statements keep stationary feasibility, coefficient specification and the time to approach the target separate. None is a claim about an optimized microscopic bath implementation.

