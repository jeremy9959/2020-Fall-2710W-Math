# The Power Set of a Set


\newcommand{\Z}{\mathbb{Z}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\Q}{\mathbb{Q}}
\renewcommand{\P}{\mathop{\mathcal{P}}}
\renewcommand{\subset}{\subseteq}

## Definition

**Definition:** If $A$ is a set, the **power set** of $A$, written
$\P(A)$, is the set whose elements are all subsets of $A$.  In set builder
notation,
$$
\P(A)=\{X: X\subset A\}
$$

## Example

$$A=\{0,1,3\}$$.  

$$\P(A)=\{\emptyset,\{0\},\{1\},\{3\},\{0,1\},\{0,3\},\{1,3\},\{0,1,3\}\}$$

## Example

$$\P(\emptyset)=\{\emptyset\}$$

Notice that $|\emptyset|=0$ and $|\P(\emptyset)|=2^{0}=1$.

## Example

$\P(\{a\})=\{\emptyset,\{a\}\}$

## Example -- some common mistakes

 $\P(1)$ makes no sense because $1$ is not a set.

## Example -- some common mistakes 2
$\P(\{1,\{1,2\}\}=\{\emptyset,1,\{\{1,2\}\},\{1,\{1,2\}\}\}$.  Notice
that $\{1,2\}$ is not an element of $\P(\{1,\{1,2\}\})$ but $\{\{1,2\}\}$
is.

## Infinite case

THe power set $\P(\N)$ is very large and can be identified with infinite sequences of $I$'s and $O$'s.

## The set $\P(\R^2)$

$\P(\R^2)$ is huge and includes every graph of every function plus lots of other things, more than we can really comprehend.

## Problem 1.4.15

What is $\P(A\times B)$ if $|A|=m$ and $|A|=n$?

