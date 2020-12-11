# Solutions to selected homework from chapter 12

## 12.5.10

**Problem:** Consider $f:\mathbb{N}\to\mathbb{Z}$ defined by
$$
f(n) = \frac{(-1)^{n}(2n-1)+1}{4}.
$$
This function is bijective by a previous exercise.  Find its inverse.

**Solution:** Because of the term $(-1)^n$, the values of this function depend heavily on whether or not
$n$ is even.  If $n$ *is* even then we can write $n=2k$ and we have
$$
f(n)=\frac{2n-1+1}{4} = \frac{n}{2}=k.
$$
In other words, if $n$ is even, then $f(n)$ is $n/2$.  Since $n$ is an even natural number, $n/2$ is
a positive integer greater than or equal to $1$.

To construct the inverse of this part of the function, we can start with a positive integer $k\ge 1$
and define $f^{-1}(k)=2k$.  

If $n$ is odd, then we can write $n=2k+1$ and we have
$$
f(n)=\frac{(1-2n)+1}{4}=\frac{2-2n}{4}=\frac{2-4k-2}{4}=-k
$$
so if $n$ is odd then $f(n)$ is $(1-n)/2$.  Since $n$ is a natural number, $(1-n)/2$ will be a
non-positive integer.  So to reverse this part of the function, given a non-positive integer $k$,
we can let $n=1-2k$.  This will be a positive odd natural number.

So putting the two parts together, we have
$$
f^{-1}(k) = \begin{cases} 2k & k>0 \\ 1-2k & k\le 0\end{cases}
$$

## Problem 12.6.6

**Problem:** Given a function $f:A\to B$ and a subset $Y\subset B$, is $f(f^{-1}(Y))=Y$ always true? Prove
or give a counterexample.

**Solution:** Notice that $f^{-1}(Y)$ is the subset of $A$ consisting of elements $a\in A$ such that
$f(a)\in Y$.  So $f(f^{-1}(Y))\subset Y$.  The question is whether $f(f^{-1}(Y))$ might be *smaller* than
all of $Y$; and indeed it can.  Here is a simple example.  Let $A=\{0\}$ and $B=\{0,1\}$.  Suppose
that $f=\{(0,0)\}\subset A\times B$ and let $Y=B$.  Then $f^{-1}(B)=A$ since $f^{-1}(0)=0$.  But
$f(A)=\{0\}\subset B$ which is smaller than all of $B$.

## Problem 12.6.8

**Problem:** Given a function $f:A\to B$ and subsets $W,X\subset A$, then $f(W\cap X)=f(W)\cap f(X)$ is *false*
in general.  Give a counterexample.

**Solution:** Suppose $A=\{0,1\}$ and $B=\{0\}$.  Suppose that $f=\{(0,0),(1,0)\}\subset A\times B$.
Let $W=\{0\}$ and $X=\{1\}$.  Then $W\cap X=\emptyset$ so $f(W\cap X)=\emptyset$.  On the other hand,
$f(W)=B$ and $f(X)=B$ so $f(W)\cap f(X)=B\not=\emptyset$.

Notice that you can find a counterexample in both of these cases using very small sets.

## Problem 12.6.12

**Problem:** Consider $f:A\to B$.  Prove that $f$ is injective if and only if $X=f^{-1}(f(X))$ for all
$X\subset A$.  Prove that $f$ is surjective if and only if $f(f^{-1}(Y))=Y$ for all $Y\subset B$.

**Solution:**  Let's first notice that $X\subset f^{-1}(f(X))$ for any $X$ and any $f$.  To see this, 
suppose $x\in X$.
Then $f(x)\in f(X)$.  Since $f^{-1}(f(X))$ is the set of all elements $a$ of $A$ such that $f(a)\in X$,
we have $x\in f^{-1}(f(X))$.  Therefore $X\subset f^{-1}(f(X))$.  Suppose that there exists
$u\in f^{-1}(f(X))$ such that $u\not\in X$.  Then $f(u)\in f(X)$ so $f(u)=f(x)$ for some $x\in X$,
and $u\not=x$ since $u\not\in X$.  Therefore $f$ is not injective.  Thus we've proven that if 
$X\not=f^{-1}(f(X))$ then $f$ is not injective.  

Now suppose $f$ is not injective, so there are two elements $a$ and $a'$ in $A$ with $f(a)=f(a')$.
Let $X=\{a\}$.   Then $f(a)\in f(X)$, so $a'\in f^{-1}(f(X))$, and therefore $f^{-1}(f(X))\not=X$ for this
particular $X$.  So if $f$ is not injective then there is an $X$ with $X\not=f^{-1}(f(X))$.

The surjectivity argument is similar, although everything is switched around.  First notice that,
for any $f$, $f(f^{-1}(Y))\subset Y$.  This is because if $a\in f^{-1}(Y)$, then $f(a)\in Y$ by definition.
So suppose there is an element $y$ of $Y$ that is not in $f(f^{-1}(Y))$.  If there were an $x$ with $f(x)=y$,
then $x$ would be in $f^{-1}(Y)$, and so $y=f(x)$ would be in $f(f^{-1}(Y))$.  So there is no such $x$,
and therefore $f$ is not surjective.

On the other hand, suppose $f$ is not surjective.  Then there is a $b\in B$ for which there is no $a\in A$
with $f(a)=b$.  Let $Y=\{b\}$.  Then $f^{-1}(Y)=\emptyset$ and $f(f^{-1}(Y))=f(\emptyset)=\emptyset$. Thus
if $f$ is not surjective, there is a subset $Y$ for which $f(f^{-1}(Y))\not=Y$.


