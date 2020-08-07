# Indexed sets

\newcommand{\N}{\mathbb{N}}
\newcommand{\R}{\mathbb{R}}
\renewcommand{\subset}{\subseteq}
## Summation notation

"Recall" that we can write a long sum of a bunch of numbers using summation notation.

$$
a_1+a_2+\cdots+a_n = \sum_{i=1}^{n} a_{i}
$$

We can even write infinite sums:

$$
1+\frac{1}{2}+\frac{1}{4}+\cdots+\frac{1}{2^{i}}+\cdots = \sum_{i=1}^{\infty}\frac{1}{2^{i}}
$$

## Indexed sets

Suppose we have a bunch of sets $A_1,A_2,\ldots, A_n$.  Then we can write:

$$
A_1\cup A_2 \cup \cdots \cup A_n = \bigcup_{i=1}^{n} A_{i}
$$

and

$$
A_1\cap A_2 \cap \cdots \cap A_n = \bigcap_{i=1}^{n} A_{i}
$$

## Indexed sets

If $A_1,A_2,\ldots, A_n$ are all sets, then 

$$
\bigcup_{i=1}^{n} A_{i} = \{x : x\mathrm{\ belongs\ to\ at\ least\ one\ set\ }A_{i}\}
$$

- $A_{1}=\{1,4,10,12\}$
- $A_{2}=\{5,12,15\}$
- $A_{3}=\{1,4,15,35\}$

What is $\bigcup_{i=1}^{3}A_{i}$?

## Indexed sets

$$
\bigcap_{i=1}^{n} A_{i} = \{x : x\mathrm{\ belongs\ to\ every\ set\ }A_{i}\}
$$

- $A_{1}=\{1,4,10,12\}$
- $A_{2}=\{5,12,15\}$
- $A_{3}=\{1,4,15,35\}$

What is $\bigcap_{i=1}^{3}A_{i}$?

## Indexed sets

One can also take the union and intersection of infinitely many sets.

$\bigcup_{i=1}^{\infty} A_{i}$ and $\bigcap_{i=1}^{\infty} A_{i}$.

The first means the elements in **at least one** of the sets; the second means the elements in **every** set.

Example.  For each $i\in\N$, let

$$A_{i}=\{-i,0,i\}$$

What is $\bigcup_{i=1}^{\infty} A_{i}$ and $\bigcap_{i=1}^{\infty} A_{i}.$?

## Index sets

Instead of numbering the sets, one can label them with elements of any set $I$ called an index set.

$\bigcup_{i\in I} A_{i}$ is the set of elements that belong to *at least one* of the sets $A_{i}$.

$\bigcap_{i\in I} A_{i}$ is the set of elements that belong to *every one* of the sets $A_{i}$.


## Index sets example

Let $C$ be the set of Counties in the state of Connecticut (there are 8 of these). 
For each county $c\in C$, let $T(c)$ be the set of Towns in that County.

For example, if $c$ is Tolland County, then the elements of $T(c)$ are Andover, Bolton,
Columbia, Coventry, Ellington, Hebron, Mansfield, Somers, Stafford, Tolland, Union, Vernon, and Willington.

What is $\bigcup_{c\in C} T(c)$?

## Index sets

Let
$$
\R_{+} = \{r: r\in \R, r>0\}.
$$

For every real number $r\in \R_{+}$, let 
$$
A_{r} = \{(x,y)\in \R^{2} : x^2+y^2<r^2\}.
$$

## Index sets
What is $\bigcap_{r\in\R_{+}} A_{r}$?


## Index Sets
What is $\bigcup_{r\in\R_{+}} A_{r}$?

## Example
What is $\bigcap_{i\in\N} [0,i+1]$?

## Example
Suppose that $I$ and $J$ are sets, that $J\not=\emptyset$, and that $J\subseteq I$.  Is
$$
\bigcap_{a\in I}A_{a}\subset \bigcap_{a\in J}A_{a}?
$$
Explain. 
