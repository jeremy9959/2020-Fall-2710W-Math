# Proof by contradiction

##

**Proposition:** The square root of $2$ is not a rational number.



##

**Lemma:** If $a^2$ is even, then $a$ is even.

**Proof:** We will prove the contrapositive, which says that if $a$ is odd, then $a^2$ is odd.
Suppose $a$ is odd.  Then $a=2k+1$ for some $k$.  Therefore $a^2=(2k+1)^2=4k^2+4k+1$ is odd.


##

**Proof of Proposition:**  Suppose that $\sqrt{2}$ is a rational number.  Then we can find positive integers
$a$ and $b$ with $b\not=0$ so that 
$$
2=(\frac{a}{b})^2.
$$




##

**Proof of Proposition:**  Suppose that $\sqrt{2}$ is a rational number.  Then we can find positive integers
$a$ and $b$ with $b\not=0$ so that
$$
a^2-2b^2=0.
$$


## Logical Structure of proof by contradiction

- A contradiction is a statement of the form ($C$ and $\sim C$) which is *always false.*

- The strategy of proof by contradiction is that if $A\implies B$ is true, and $B$ is false, then $A$ is false.

**Proposition:** $P\implies Q$.

- Assume $P$ is true.
- Assume ($P$ and $\sim Q$) is true and 
$$
P \hbox{\rm\ and\ } \sim Q \implies C \hbox{\rm\ and\ }\sim C
$$
for some statement $C$.
- If ($P$ and $\sim Q$) implies ($C$ and $\sim C$) is a true implication yielding a false conclusion,
then the hypothesis must be false.  
- Therefore ($P$ and $\sim Q$)
is false.  
- If ($P$ and $\sim Q$) is false, and  $P$ is true then $\sim Q$ is false
- $Q$ is true.

## Euclid's Proof

Recall that we know that every integer can be written as a product of prime numbers. In particular,
every integer greater than $1$ has a prime divisor. 

**Proposition:** There are infinitely many primes.


## Euclid's Proof cont'd


**Proof:** Suppose that there are only finitely many prime numbers.  Multiply them together and let
$P$ be their product.  Consider the integer $P+1$.  This integer must have a prime divisor $p$, 
which must be greater than one, so we can write $P+1=pA$.  Since $P$
is the product of all the primes, we know that $p$ is a divisor of $P$, so we can write $P=pB$.  Therefore
$1=pA-P=pA-pB=p(A-B)$.  This implies that $p$ is a divisor of $1$, so $p=1$.  We've proved that $p>1$ and $p=1$,
which is a contradiction.  Thus there cannot be finitely many primes.







