# Proof by Contrapositive

## The contrapositive.

**Important:** The contrapositive of an implication $P\implies Q$ is $\sim Q\implies \sim P$. 

- If $\sim Q$ is false (meaning $Q$ is true) the implication $\sim Q\implies \sim P$ is automatically true.
- So we assume $\sim Q$ is true -- that is, that $Q$ is false -- and try to conclude that $\sim P$ is true --
meaning that $P$ is false.

## Contrapositive.

**Proposition:** Suppose that $x\in\mathbb{Z}$.  Suppose  $x^2-4x+3$
is even.  Then $x$ is odd.

## Contrapositive

**Proof:** Suppose $x$ is even.  Then $x=2m$ for some integer $m$.   Therefore 
$$
B=x^2-4x+3=4m^2-8x+3 = 2(2m^2-2m+1)+1.
$$
Since $B$ is of the form $2k+1$ with $k=2m^2-2m+1$, we conclude that $B$ is odd.  Therefore $B$
is not even.  We have shown that if $x$ is not odd, then $B$ is not even, and therefore if $B$ is even,
$x$ is odd.

## Contrapositive

**Proposition:** Suppose that $x\in\mathbb{Z}$, that $a$ is even, and that $b$ is odd.  
If $x^2-ax+b$ is even, then $x$ is odd.



## An example from calculus

**Theorem:** Let $f:[a,b]\to\mathbb{R}$ be a function that is continuous on the closed interval $[a,b]$
and differentiable on the open interval $(a,b)$.  If $f'(x)=0$ for all $x\in [a,b]$, then $f$ is constant.

**Proof:**

- We will show that if $f$ is not constant, then there is an $x\in [a,b]$ with $f'(x)\not=0$.

- Suppose that $f(x)$ is not constant.  Then there are two (different) points $u$ and $v$ in $[a,b]$ such that
$f(u)\not=f(v)$.  

## calculus cont'd



- $f:[u,v]\to\mathbb{R}$ is continuous on $[u,v]$ and differentiable on $(u,v)$.  Therefore, by the mean
value theorem, there is a point $c\in (u,v)$ such that 
$$
f'(c)=\frac{f(v)-f(u)}{v-u}.
$$
Since $f(v)\not=f(u)$, the quantity on the right is not zero, and so $f'(c)\not=0$.

- Therefore $f'(x)$ is not zero for all $x\in [a,b]$.  This proves our result.









