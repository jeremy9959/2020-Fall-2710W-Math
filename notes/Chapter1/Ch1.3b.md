
# Counting Subsets
\renewcommand{\subset}{\subseteq}

## Counting subsets of a finite set

**Theorem:** A finite set with $n$ elements has $2^{n}$ subsets.

$\{1,2\}$ has $4$ subsets: 

- the empty set $\emptyset$, 
- the one element sets $\{1\}$ and $\{2\}$,
- the two element set $\{1,2\}$.

## Counting subsets

The book gives one explanation for why this is true on page 13.  We will give
a slighly different one.

## Counting subsets

Suppose we have a finite set  $A$ with $n$ elements.  We will list the elements
as $a_1,a_2,\ldots, a_n$.

$$
A=\{a_1,a_2,\ldots,a_n\}.
$$

Here, we've decided to put the elements of $A$ in order, but it doesn't matter what order you use.

## Counting subsets

A subset $B$ of $A$ is determined by going through the elements of $A$ and marking each element
as either "in" our "out" of the subset.  So we can describe a subset of $A$ by giving a list

$$
I,I,O,I,O,\ldots, I
$$

where we have an $I$ if that element is in the subset, or an $O$ if it isn't.

## Counting example

Suppose $A=\{-1,4,7,8\}$.  We put the elements of $A$ in that order, so $a_1=-1,a_2=4,a_3=7,$ and $a_4=8.$
Let $B=\{-1,7\}$ so that $B\subset A$. 

Then $B$ corresponds to the list
$$
I,O,I,O
$$
since $-1$ is IN $B$, $4$ is OUT of $B$, $7$ is IN $B$, and $8$ is OUT of $B$.

The list $O,I,O,O$ corresponds to the subset $\{4\}$ since only $4$ is IN this set.

## Counting subsets

**Theorem:** The number of subsets of a set $A$ with $n$ elements is the same as the number of
ordered sequences of $I$ and $O$ of length $n$, and this number is $2^{n}$.

**Proof:** Let $S=\{I,O\}$.  We've seen above how a sequence of $I$ and $O$ correspond to a subset.
The set of sequences of $I$ and $O$ of length $n$ is exactly $S^{n}$.  By our earlier counting
result, $|S^{n}|=|S|^{n}=2^{n}$.
