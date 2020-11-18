# Euclid's algorithm

## An important, non-trivial example: Euclid's Algorithm

**Theorem (Book Proposition 7.1):** If $a$ and $b$ are natural numbers, then there exist integers $k$ and $l$
for which 
$$
\gcd(a,b) = ak+bl.
$$

Comments:  

- logical structure of this statement is 
"For all $a$ and $b$ in $\mathbb{N}$ there exists $k$ and $l$ in $\mathbb{Z}$ such that $\gcd(a,b)=ak+bl$."
- Note that $k$ and $l$ will depend on $a$ and $b$.

## Hidden part

## Hidden part continued

## A Lemma

**Lemma:** Let $a$ and $b$ be natural numbers.  The set $A=\{ax+by:x,y\in\mathbb{Z}\}$ is *closed*
under addition, meaning the sum (and difference) of any two elements of $A$ is an element of $A$.

## Proof from the book.

**Proposition 7.1:** If $a,b\in\mathbb{N}$, then there exist integers $k$ and $l$ so that
$$\gcd(a,b)=ak+bl.$$

**Proof:**  The set $A=\{ax+by: x,y\in\mathbb{Z}\}$ contains positive and negative integers, as well as $0$.
Let $d$ be the *smallest positive element of $A$*.  Since $d\in A$, there are values of $x$ and $y$
so that $d=ax+by$.  Call one set of these values $k$ and $l$, so that $d=ak+bl$.

## proof, cont'd.

**Step 1.** $d$ is a common divisor of $a$ and $b$.  

**Proof:** Find $q$ and $r$ so that $a=qd+r$ and $0\le r<d$. Then 
$qd$ is in $A$ and $a$ is in $A$, so $r=a-qd$ is in $A$, since $A$ is closed under addition.

Since $0\le r<d$, and $d$ is the *smallest* positive element of $A$, we must have $r=0$.



Therefore $a=qd$ and so $d$ is a divisor of $a$.  The same argument works for $b$.

## proof, cont'd

**Step 2:** $d=ax+kl$ is the *greatest* common divisor of $a$ and $b$.  

**Proof:** Let $g\in\mathbb{N}$ be any common divisor of $a$ and $b$. 

Then $a=ug$ and $b=vg$ for natural numbers $u$ and $v$.  

Therefore
$$
d = ugk+vgl = g(uk+vl).
$$


As a result, $g$ is a divisor of $d$ and so $d\ge g$.  Therefore $d$ is the greatest common divisor.

## Notes

- Notice that we in fact proved that every common divisor of $a$ and $b$ is a divisor of $\gcd(a,b)$.

- Implicit in the proof is an *algorithm* for finding $\gcd(a,b)$, as well as 
$k$ and $l$ so that $\gcd(a,b)=ak+bl$.
