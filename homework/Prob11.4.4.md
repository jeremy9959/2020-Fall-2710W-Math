# Problem 11.4.4

\renewcommand{\subset}{\subseteq}

**Problem:** Suppose that $P$ is a partition of a set $A$. Define
a relation $R$ on $A$ by declaring that $xRy$ if and only if
$x,y\in X$ for some set $X\in P$.  Prove that

- $R$ is an equivalence relation on $A$.
- $P$ is the set of equivalence classes of $R$.


**Discussion:** Remember that a partition $P$ of $A$ is a set of
subsets $X\subset A$ such that each element of $A$ belongs to exactly one
of the subsets and the union of all of the subsets is $A$.

In other words, the partition divides $A$ up into a family of disjoint
subsets that together cover all of $A$.

**Proof:**
An ordered pair $(x,y)$ belongs to $R$ if and only
if $x$ and $y$ belong to the same set $X$ of the partition $P$.
We need to show that this definition yields a relation that is
reflexive, symmetric, and transitive.  

*$R$ is reflexive.*  By definition, $(x,x)$ belongs to $R$
if and only if $x$ belongs to the same set $X$ as $x$.
This is clearly true since there is only one element $x$ involved.

*$R$ is symmetric.* Suppose that $(x,y)\in R$.  This means
that $x$ and $y$ belong to the same set $X\in P$.  This condition
doesn't care about the order of $x$ and $y$, so $R$ is symmetric.

*$R$ is transitive.*  Suppose that $(x,y)\in R$ and $(y,z)\in R$.
This means there are two sets $X_1,X_2\in P$ so that
$x,y\in X_1$ and $y,z\in X_2$.  But in this case, $y\in X_1\cap X_2$,
and since the elements of a partition are either disjoint or equal,
we must have $X_1=X_2=X$.  Therefore $x,z\in X$ so $(x,z)\in R$.

Next, we have to prove that the equivalence classes of the
relation $R$ are exactly the sets of the partition $P$.  This
is a question about *equality of sets* -- if we let $Q$ be
the set of equivalence classes of $R$, we are trying to show
that $Q=P$. As usual with such proofs, we need to prove that
$Q\subset P$ and $P\subset Q$.  In other words, we must show
both of the following:

- every equivalence class of $R$ is an element of the set $P$.
- every element of the set $P$ is an equivalence class of $R$.

For the first, let $a\in A$ and let
$$
[a]=\{x\in A: xRa\}.
$$
Let $X$ be the element of $P$ containing $a$. (We know there
is only one such $X$ since $P$ is a partition).  If
$z\in X$, then $zRa$, so $z\in [a]$.  Therefore $X\subset [a]$.
If $z\in [a]$, then $zRa$, so $z$ belongs to $X$, so $[a]\subset X$.
Therefore $[a]=X$.  We have shown that every equivalence class is
one of the sets of the partition $P$.

Now let $X\in P$ be one of the elements of the partition.  Choose
$a\in X$ and let $[a]$ be the equivalence class of $a$ under $R$.
If $z\in X$, then $zRa$ so $z\in [a]$; therefore $X\subset [a]$.
If $z\in [a]$, then $zRa$ which means $z$ and $a$ belong to the
same set of the partition; since $a\in X$, we have $z\in X$.
Therefore $[a]\subset X$.  Thus $[a]=X$ and so every $X\in P$
is one of the equivalence classes.

Thus the two partitions (the one given by $P$, and the one given
by equivalence classes of $R$) are actually the same.

