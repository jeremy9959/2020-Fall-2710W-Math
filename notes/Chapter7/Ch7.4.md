# Constructive vs non-constructive proofs

## Constructive Proofs

A constructive proof of an existence claim gives an example of an object with the desired properties.

For example, the $A/(B+C)+B/(A+C)+C/(A+B)=4$ result had a constructive proof because I presented explicit values of
$A$, $B$, and $C$.

Euclid's algorithm is constructive because it explains how to find $x$ and $y$ so that $\gcd(a,b)=ax+by$.

## Non-constructive proofs

A non-constructive proof shows that something exists by "ruling out its non-existence" without necessarily
explaining how to find the example.  

See the proposition on page 154 for an example. 



Here is an example of a theorem  (the Intermediate Value Theorem) whose proof is not constructive.

**Theorem:** Let $f:[a,b]\to\mathbb{R}$ be a continuous function where $f(a)<0$ and $f(b)>0$.  Then there
exists a $c\in (a,b)$ such that $f(c)=0$.

The proof (which you will learn when you take Analysis)
shows that $c$ exists without giving an algorithm for finding it.
