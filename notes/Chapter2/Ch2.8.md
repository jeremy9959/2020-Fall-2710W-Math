# Implications and open sentences
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}

## Implications and open sentences

Consider the statement:

For all $x\in\Z$, if $x$ is divisible by $6$ then $x$ is even.

- "$x$ is divisible by $6$" is an open sentence $P(x)$
- "$x$ is even" is an open sentence $Q(x)$
- "if $x$ is divisible by $6$ then $x$ is even" is an open sentence $P(x)\implies Q(x)$.

## Analysis of quantified implication

"For all $x\in\Z$, if $x$ is divisible by $6$ then $x$ is even"

is a statement that "ands" together $P(x)\implies Q(x)$ as $x$ runs over the integers:

$$\cdots(P(-5)\Rightarrow Q(-5))\wedge(P(-4)\Rightarrow Q(-4))\wedge\cdots\wedge(P(3)\Rightarrow Q(3))\cdots$$

This will be true if every one is true, meaning one of the following is true:

- $x$ is not divisible by $6$, so $P(x)$ is false for that $x$
- $x$ is divisible by $6$ and $x$ is even meaning $P(x)$ and $Q(x)$ are true for that $x$.

It will be false if there is at least one $x$ that is divisible by $6$ but not even.


## Conventional interpretation

It is a common convention to read a statement like

"If $x$ is an integer divisible by $6$, then $x$ is even"

as including an implicit quantifier "for all $x\in\Z$."

- If $f:\mathbb{R}\to\mathbb{R}$ is a differentiable function, then it is continuous
- If $x\in\mathbb{R}$, then $x^2= x$ implies $x=0$ or $x=1$.


