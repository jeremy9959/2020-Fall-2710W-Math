# Logical Equivalence

## Equivalence

Two statements $P$ and $Q$ are logically equivalent if $P\iff Q$ is **always true.**

For example, $P\implies Q$ and "$Q$ or $\sim P$" are logically equivalent.  To see this,
look at the truth table for

$$
(P\implies Q) \iff (\sim P \vee Q).
$$

We can write "=" instead of $\iff$ in these situations.

## Other ways of thinking about logical equivalence

Another way to think of logical equivalence is that two statements made up of statements
$P, Q, R,\ldots$ are logically equivalent if their truth tables are the same.  

## Boolean Algebra

One can think of a kind of algebra made up of statements together with operations And, Or, Not,
implies, and so on.  From this point of view, two expressions made up of statements are "equal"
or "the same" if they are logically equivalent.

In fact this is called Boolean Algebra and is an important tool in computer science.

## DeMorgan's Laws

- NOT (P AND Q) is equivalent to ((NOT P) or (NOT Q))
- NOT (P OR Q) is equivalent to ((NOT P) and (NOT Q))

## Contrapositive
$(P\implies Q)=(\sim Q \implies \sim P)$


## Associative Laws

$P\wedge (Q\wedge R) = (P\wedge Q)\wedge R$


## Distributive Laws for AND over OR or OR over AND

$P\wedge (Q\vee R)=((P\wedge Q)\vee (P\wedge R))$





