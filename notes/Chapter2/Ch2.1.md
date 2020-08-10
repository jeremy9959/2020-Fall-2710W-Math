# Logic and Statements

\newcommand{\Q}{\mathbb{Q}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\Z}{\mathbb{Z}}

## Logic

- Informally, logic is the set of rules that govern reasoning.  

- The rules of logic allow one to combine truths together to conclude other truths.  For example,
if we know that every bird has wings, and we know that a turkey is a bird, then we "automatically" know
that a turkey has wings.

- Naively we might think that if we have a complete set of axioms, or basic truths, then using
logic we could derive all other truths. 

- The work of Godel  showed that there are true statements that can't be proved.  The book
Godel, Escher, Bach by Douglas Hofstadter is a beautiful explanation of Godel's work that
is accessible to everyone. See

> Hofstadter, Douglas R. (1999) [1979], Gödel, Escher, Bach: An Eternal Golden Braid, Basic Books, ISBN 0-465-02656-7, 

## Statements

A **statement** is a sentence which is either True or False. Some examples:

- Every buffalo is a mammal.

- Every system of $n$ linear equations in $n$ unknowns has a solution.

- There have been 62 presidents of the United States.

- There is an $x\in\Q$ such that $x^2=2$.

## Non-statements

- Speak friend, and enter.

- $\{2x: x\in\N \}$.

- 42

## Naming statements and statements with variables

- $P$ is the statement "Every odd number is prime."

- $Q$ is the statement "No even number is prime."

- $P(x)$ is the statement: The integer $x$ is even. The truth of this depends on $x$; this is really
infinitely many statements, one for each integer $x$.  When the truth depends on the values of the variables
it is called an **open sentence.**

## Some statements are mysterious

Book gives Goldbach Conjecture and Fermat's Last Theorem.

The Collatz Game: Pick a natural number $x$.  If $x$ is even, divide it by $2$.  If $x$ is odd,
multiply it by $3$ and add $1$.  Repeat.  
$$
7,22,11,34,17,52,26,13,40,20,10,5,16,8,4,2,1,4,2,1,2,1,\ldots
$$

Let $C(x)$ be the statement:

> if you start with $x$, you will eventually (after finitely many steps) 
> reach the cycle $1,2,4,1,2,4,\ldots$. 

Is $C(x)$ always true?




