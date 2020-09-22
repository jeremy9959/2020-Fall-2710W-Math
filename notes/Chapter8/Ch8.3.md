\renewcommand{\subset}{\subseteq}
## Set equality

The assertion that two sets $A$ and $B$ are equal is equivalent to saying that
$$
x\in A\Leftrightarrow x\in B.
$$
In other words, $x$ is in $A$ if and only if $x$ is in $B$.  Now $(x\in A)\Leftrightarrow (x\in B)$
is the same as
$$
\left[(x\in A)\implies (x\in B)\right] \hbox{\rm\ AND\ } \left[(x\in B)\implies (x\in A)\right]
$$
and this is just $A\subset B$ and $B\subset A$.

So we prove two sets are equal by proving BOTH $A\subset B$ and $B\subset A$.

## Euclid's algorithm

Here's what we proved in the discussion in Chapter 7.

**Proposition:** Let $d=\gcd(a,b)$ and let $m$ be any integer.  Then there exist $k$ and $l$
such that $m=ak+bl$ if and only if $d|m$.

Set version:

**Proposition:** Let $a$ and $b$ be natural numbers, and let $d=\gcd(a,b)$. 
Define sets $A=\{dn: n\in\mathbb{Z}\}$ and $B=\{ax+by: x,y\in\mathbb{Z}\}$.  Then $A=B$.

Here:

- $A\subset B$ means that every multiple of $d$ can be written in the form $ax+by$.

- $B\subset A$ means that every number of the form $ax+by$ is a multiple of $d$.

## More examples

**Proposition:** Let $a$ and $b$ be prime numbers.  Let $A=\{da:d\in\mathbb{Z}\}$ and 
$B=\{db:d\in\mathbb{Z}\}$. Then $A\cap B = \{dab: d\in\mathbb{Z}\}$.

## More examples

**Proposition:** If $A$, $B$, and $C$ are sets then $A\times (B\cap C) = (A\times B)\cap (A\times C)$.
(this is problem 17 on page 171)


## More examples

**Proposition:** Prove that $\{12a+4b:a,b\in\mathbb{Z}\}=\{4c:c\in\mathbb{Z}\}$.

## More examples

**Proposition:** Let $A=\{(x,y)\in\mathbb{R}^{2}:y=x^2\}$.  Let 
$B$ be the set of real numbers $z$ such that there exists $x\in\mathbb{R}$ such that $(x,z)\in A$.  Then
$B=\{z\in\mathbb{R}:z\ge 0\}$.

