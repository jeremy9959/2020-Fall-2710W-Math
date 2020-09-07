# Checking cases

## Cases

**Proposition:**  If $n$ is a natural number, then $1+(-1)^n(2n-1)$ is a multiple of $4$.





## Cases

**Proof:** Let $K(n)=1+(-1)^n(2n-1)$.  We consider the cases where $n$ is odd and even separately. When
$n$ is even, $K(n)=1+(2n-1)=2n$.  Since $n$ is even, $n=2m$ for some $m$, and therefore $K(n)=2(2m)=4m$.  Therefore
$K(n)$ is a multiple of $4$.

When $n$ is odd, $K(n)=1-(2n-1)=2-2n$.  Since $n$ is odd, $n=2m+1$ for some $m$, and therefore 
$$K(n)=2-2(2m+1)=2-4m-2=4m$$ 
and again $K(n)$ is a multiple of $4$.


## Cases

**Proposition:** (The Triangle Inequality) For any real numbers $x$ and $y$, we have
$$
|x+y|\le |x|+|y|
$$

Note:  $|x|=x$ if $x\ge 0$, otherwise $|x|=-x$.



## Cases

**Proof:** There are four cases to consider, depending on the signs of $x$ and $y$, and we take them in turn.

1. $x\ge 0$ and $y\ge 0$. Then $x+y\ge 0.$  Therefore, in this case, $|x|=x$, $|y|=y$, and $|x+y|=x+y$ and so 
$|x+y|=|x|+|y|$.


2. If $x<0$ and $y<0$ then $|x+y|=-x-y=|x|+|y|$.


## Cases

3. $x\ge 0$ and $y<0$.  







## Cases

3. $x\ge 0$ and $y<0$.  

Note that in this case $|x|=x$ and $|y|=-y$.

We also see that $y<x+y<x$.  If $x+y\ge 0$, then $|x+y|=x+y=|x|-|y|\le |x|+|y|$. If $x+y<0$,
then $|x+y|=-x-y=-|x|+|y|\le |x|+|y|$.


The 4th case, $x<0$ and $y\ge 0$, follows by the same argument.
