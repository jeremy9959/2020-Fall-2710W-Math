---
title: Chapter 1 Section 1
---

# Section 1.1
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\Q}{\mathbb{Q}}

## Sets

- A **Set** is collection of things, called the "elements" of the set.
- Two sets are the same means they have exactly the same elements.  Knowing the elements means knowing the set.

## Describing sets by listing elements

A set can be described by listing its elements using curly braces.

$$
A = \{1,2,3\}
$$
means $A$ is the set whose elements are $1$, $2$, and $3$.  The symbols $\{$ and $\}$
are special and are used to describe sets.

**Note:** The sets $A=\{1,2,3\}$ and $B=\{3,1,2\}$ are the same because they have the same elements.

## Basic examples

- The natural numbers $\mathbb{N}$ is the set of counting numbers $1,2,3,\ldots$
$$
\mathbb{N} = \{1,2,3,\ldots\}
$$

- The integers are the are the positive and negative whole numbers, and zero:
$$
\mathbb{Z} = \{\ldots, -5,-4,-3,-2,-1,0,1,2,3,\ldots\}
$$

- The rational numbers $\mathbb{Q}$ are the positive and negative fractions and zero. 

We take for granted addition, multiplication, commutative, associative, laws etc.

## Set builder notation (predicates)

Set builder notation picks elements out of another set.  

Example:
$$
\{x\in \Z : x\ge 0\}
$$

means "pick from the set $\Z$ those elements that satisfy the condition $x\ge 0$".  

The condition is called a *predicate*. 


## Other sets

- the alphabet
- the set of words in English
- the set of people now living
- the set of chairs in my house (what's a chair....)

## The empty set

There is exactly one set which nas no elements, called the *empty set.*  
The empty set can be written $\emptyset$ or $\{\}$.

## The cardinality of a set

- If $A$ is a set, we write $|A|$ for the *number of elements* in the set if that number is finite.

- If $A=\{1,2,3\}$ then $|A|=3$

- We will study cardinality in more detail at the end of the class; for now, we will take this
idea for granted.  We also take for granted that a set like $\mathbb{Z}$ has infinitely many elements.

## The real numbers

- The real numbers is the set of all numbers with possibly infinite decimal expansions (positive or negative).
A proper definition is hard to give and is usually done in analysis.  We will work with the real numbers
informally as we did in Calculus.

## Intervals  $\mathbb{R}$
See page 7 of the text.

- $(a,b) = \{x\in\R : x>a \mathrm{\ and\ } x<b\}$ "open"
- $[a,b) = \{x\in\R: x\ge a \mathrm{\ and\ } x<b\}$ "half open"
- $(a,b] = \{x\in\R: x>a \mathrm{\ and\ } x\le b\}$ "half open"
- $[a,b] = \{x\in\R: x\ge a \mathrm{\ and\ } x\le b\}$ "closed"
- $[a,\infty) = \{x\in\R: x\ge a\}$ "infinite"
- $(a,\infty) = \{x\in\R: x>a\}$ "infinite"
- $(\infty,a) = \{x\in\R: x< a\}$ "infinite"
- $(\infty,a] = \{x\in\R: x\le a\}$ "infinite"

## Closer look: Example 1.1

**Claim:** $\{n^2: n\in\Z\} = \{0,1,4,9,16,25,\ldots\}$

- Say this in words
- What about $\{n^2:n\in\N\}$?
- What about $\{n^2:n\in\Q\}$?

## Closer look: Example 1.2

**Problem:** Describe the set $A=\{7a+3b:a,b\in\Z\}$.

## Closer look: Problem 1.1.7

**Problem:** Describe the set $\{x\in \R: x^2+5x=-6\}$.

- The back of the book gives the answer $\{-2,-3\}$.  Why is this the answer?

- What about if we replace $\R$ with $\Q$?

- What about if we replace $\R$ with $\N$?

<!--
%- cardinality
%- the empty set
%- integers, natural numbers, rational numbers
%- real numbers, and intervals
%- other examples of sets
%----
%Cartesian product
%ordered pairs
%cardinality of product of two finite sets
%triples, cartesian powers
%R^n
%----
%subsets
%empty set is subset of all sets
%counting subsets
%----
%power sets
%cardinality of a power set
-->
