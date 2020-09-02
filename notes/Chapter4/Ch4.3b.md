# Direct Proofs Example

## The arithmetic/geometric mean inequality

**Definition:** The arithmetic mean of two real numbers $a$ and $b$ is $(a+b)/2$.

**Definition:** The geometric mean of two positive real numbers $a$ and $b$ is $\sqrt(ab)$.

**Proposition:** If $a$ and $b$ are positive real numbers, then
the geometric mean of $a$ and $b$ is less than or equal to their arithmetic mean.

##

**Proposition:** If $a$ and $b$ are positive real numbers, then
the geometric mean of $a$ and $b$ is less than or equal to their arithmetic mean.

**Proposition:** If $a$ and $b$ are positive real numbers, then:
$$
\sqrt(ab)\le \frac{(a+b)}{2}
$$

## Problem Solving Phase




## Isolating the needed lemma

**Lemma:** If $a$ and $b$ are positive, and $a\le b$, then $\sqrt{a}\le\sqrt{b}$ where $\sqrt{x}$ denotes
the positive square root of $x$.



## The proof

**Proposition:** If $a$ and $b$ are positive real numbers, then:
$$
\sqrt(ab)\le \frac{(a+b)}{2}
$$

Proof:

We know that $(a-b)^2\ge 0$.  Therefore $a^2+b^2-2ab\ge 0$ and so $a^2+b^2\ge 2ab$.  Add $2ab$ to both
sides to obtain $a^2+2ab+b^2\ge 4ab$ so $(a+b)^2\ge 4ab$. Both sides of this inequality are positive,
since the left side is a square the right side is a product of positive numbers.  Now apply the lemma
to take the square root of both sides to obtain
$$
(a+b)\ge 2\sqrt{ab}.
$$
Dividing both sides by $2$ yields the desired result.






