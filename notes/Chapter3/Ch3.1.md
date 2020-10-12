# Counting

## The multiplication principle

**From the text, p. 69:** Suppose in making a list of length $n$ there are $a_1$ possible choices for
the first entry, $a_2$ possible choices for the second entry, $a_3$ possible choices for the third entry,
and so on.  Then the total number of lists that can be made is this way is the product
$a_1\cdot a_2 \cdots a_n$.

We will treat this as a proposition, put it in more formal language, and prove it by induction.

##

Notice that a "list" where the first element is chosen from $X_1$, the second from $X_2$, and so on
is precisely an element of $X_1\times X_2\times \cdots X_n$, so we are really trying to compute the
number of elements in a cartesian product of finite sets.

**Proposition:** Let $X_1,X_2,\ldots, X_n$ be finite sets and suppose that $|X_{i}|=a_{i}$ for $i=1,\ldots, n$.  Then
the number of elements  
$$|X_1\times X_2\times \cdots\times X_n| = a_1\cdot a_2\cdots a_n
$$

##

**Proof:** (by induction).  First we consider the case where $n=2$.  We have two sets $X_1$ and $X_2$
with $a_1$ and $a_2$ elements respectively.  Explicitly we have
$$
X_1\times X_2 = \{(x,y):x\in X_1,y\in X_2\}.
$$
For each element $b\in X_{2}$, we have $a_1$ elements $(x,b)\in X_1\times X_2$.  
Counting up these $a_1$ elements for each of the $a_2$ elements $b$, we see that $X_1\times X_2$ has $a_1a_2$
elements.

##

Now suppose we know that $X_1\times\cdots\times X_n$ has $a_1\cdots a_n$ elements.  We must show that this implies
that $X_1\times\cdots\times X_n\times X_{n+1}$ has $(a_1\cdots a_n)a_{n+1}$ elements. Let
$$
Y = X_1\times\cdots \times X_{n}. 
$$
Then $Y\times X_{n+1}$ consists of pairs $(y,x)$ where $y$ is an element of the cartesian product of the
$X_{i}$ and $x$ is an element of $X_{n+1}$.  Strictly speaking $Y\times X_{n+1}$ and $X_{1}\times \cdots\times X_{n}\times X_{n+1}$ are not equal sets, but they do have the same number of elements. Why?

##


By the inductive hypothesis
$|Y\times X_{n+1}|=a_{1}\cdots a_{n}a_{n+1}$ which is equal to $|X_{1}\times \cdots X_{n+1}|$, as we hoped to prove.

##

## Some applications: Problem 1, pg. 73

- How many length 4 lists can be made from the letters THEORY, with repetition allowed.
\vfill\eject

- How many length 4 lists begin with T?

\vfill\eject
- How many length 4 lists do *not* begin with T?

\vfill\eject
## Problem 7.  Consider 4 letter code sequences made from the letters $A$, $B$, $C$, $\ldots$, $Z$.

- How many such codes are there?
\vfill\eject
- How many codes have no two such consecutive letters the same?
\fill\eject
