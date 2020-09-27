# Disproof
## Disproof

A "disproof" of a statement $P$ is a proof of $\sim P$.

Suppose the result we are interested is a universally quantified statement of the form:

For all $x\in S$, $P(x)$

The negation of this statement is:

There exists $x\in S$ such that $\sim P(x)$. 

## Disproof

For example, if the original statement is:

- if $n\in\mathbb{Z}$ and $n^5-n$ is even, then $n$ is even.

The negation is:

- There exists an integer $n$, such that $n^5-n$ is even and $n$ is odd.

## Disproof by counterexample

The negation of the "for all statement" is a "there exists" statement.  To prove that negation, we need
to *find an example that satisfies the negation.*

To disprove

- if $n\in\mathbb{Z}$ and $n^5-n$ is even, then $n$ is even.

we must find an integer $n$ such that $n^5-n$ is even and $n$ is odd.  

Try a few $n$ and it doesn't take long to find $n=1$.

Let $n=1$.  Then $n^5-n=0$ is even, but $n=1$ is odd. 

This example which establishes the truth of the negation is called a *counterexample* to the original
statement.

## Another disproof by counterexample

It may not be obvious that a statement is false.  (this is problem 7 on page 179).

*Proposition:* Suppose that $A$, $B$, and $C$ are sets.  If $A\times C = B\times C$ then
$A=B$.


## Counterexamples, cont'd

Counterexamples often come from "edge cases."
- What if a variable is zero?
- What if a set is empty? 
- What if an integer is negative?

