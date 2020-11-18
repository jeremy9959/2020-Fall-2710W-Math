# Pascal's Triangle and the binomial theorem

## Pascal's Triangle

We proved that $\binom{n}{k}$ counts the number of subsets with $k$ elements that can be found
in a set with $n$ elements.

We know that
$$
\binom{n}{k} = \frac{n!}{(n-k)!}{k!}
$$

We set $\binom{n}{k}=0$ if $k>n$ (there are no subsets with $k$ elements in a set with $n$ elements if $k>n$.)

In the inductive proof that $\binom{n}{k}$ counts subsets, we proved that
$$
\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}
$$

This relation defines "Pascal's Triangle".
\vfill\eject


## Binomial Theorem

**Theorem:** 
$$
(x+y)^{n} = \sum_{i=0}^{n} \binom{n}{i}x^i y^{n-i}
$$

**Proof:** By induction.
