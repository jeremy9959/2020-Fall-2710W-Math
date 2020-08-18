# Quantifiers
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\R}{\mathbb{R}}
## Quantifiers

Remember that an open sentence is a sentence that includes variables; when you specify
the variables, the open sentence becomes a statement that can be true or false. 

## Quantifiers

Most equations that we want to "solve" are really open sentences. For example, 
$$\begin{aligned}
3x&=&7\\
x^2+5x+6&=&0\\
\end{aligned}
$$
are open sentences whose truth depends on the choice of $x$. 

Whether or not these equations even *have* solutions depends on what kind of values $x$ is allowed to have.

## Quantifiers

For example:

- neither of these equations have solutions if $x$ is required to be a natural number.
- if $x$ is allowed to be an integer, then the second equation has two solutions, but the first one still has none.
- if $x$ is allowed to be a rational number, then both equations have solutions.

## Quantifiers

Quantifiers are an element of the logical language that put a scope on the possible values
of a variable in an open sentence, and in the process convert the open sentence into a statement.

The are two quantifiers:
- "there exists" makes the statement about *some* $x$ in a particular set,
- "for all" makes the statement about *all* $x$ in a particular set.

## Existential quantifier (there exists)

"There exists $x\in\Q$ such that $3x=7$" 

This statement is true if and only if the subset 
$$
X=\{x: x\in\Q, 3x=7\}
$$
has at least one element -- there is *some* $x$ so that $3x=7$ among the $x\in\Q$.

- "There exists $x\in\Q$ such that $3x=7$" is True
- "There exists $x\in\Z$ such that $3x=7$"  is False

More generally, if $X$ is any set, and $P(x)$ is an open sentence,
then the statement "There exists $x\in X$ so that $P(x)$" (in symbols "$\exists x, P(x)$") is true  exactly when the
set
$$
Y=\{x: x\in X, P(x)\}
$$
has at least one element.


## Univeral quantifier (for all)

The statement "For all $x\in\N$, $x^2>0$" is true if  and only if
$$
X=\{x: x\in \N, x^2>0\}=\N.
$$

It claims something is true for *all* $x\in\N$.  This is in fact a true statement.

On the other hand, the statement "For all $x\in\Z$, x^2>0" is false since $0^2=0$ and $0\in\Z$.

More generally, the statement "For all $x\in X$, $P(x)$" (in symbols "$\forall x, P(x)$") is true exactly when
$$
X=\{x\in X: P(x)\}.
$$

This is a statement about *all* $x\in X$.

## A few more examples

- There exists $x\in\R$ such that $x^2=15$.
- For all $y\in\R$, $|\sin(y)|\le 1$.
- There exists a subset $X$ of $\N$ which has 5 elements.

## Negating quantified statements

The statement "There exists $x\in X$ such that $P(x)$" is false exactly when "For all $x\in X$, not $P(x)$" is true.

For example, "There exists $x\in\R$ such that $x^2<0$" is false because "For all $x\in\R$, $x^2\ge 0$" is true.

The statement "For all $x$, $P(x)$" is false exactly when "There exists $x$ such that not $P(x)$" is true.

For example, the statement "For all $x\in\N$, $x^2>0$" is true because "There exists $x\in\N$ with $x^2\le 0$." is
false. 

## Existence and "OR", For all and "AND"

There exists $x\in X$ such that $P(x)$ is a kind of  "OR" statement.

For all $x\in X$ such that $P(x)$ is a kind of  "AND" statement.













