# Problem 11.3.14

\renewcommand{\subset}{\subseteq}

**Problem:** Suppose that $R$ is a reflexive and symmetric relation
on a finite set $A$.  Define a relation $S$ on $A$ by declaring
that $xSy$ if and only if, for some $n\in\mathbb{N}$, there are
elements $x_1,\ldots, x_n\in A$ satisfying $xRx_1,x_1Rx_2,\ldots, x_{n-1}Rx_{n}$ and $x_{n}Ry$.

1. Show that $S$ is an equivalence relation.
2. Show that $R\subset S$.
3. Show that $S$ is the unique smallest equivalence relation on $A$
containing $R$.

**Discussion:** The idea of this problem is to show that, given
a reflexive and symmetric relation $R$ which isn't necessarily transitive,
you can make a relation that is consistent with the original relation
but which *is* transitive.  The way you do this is to add in
all the ordered pairs $(x,y)$ that *should* be related if the relation
were transitive.  For example, if $(a,b)\in R$ and $(b,c)\in R$,
and $R$ were transitive, then $(a,c)$ should be in $R$.  In making
our transitive relation, then, we keep all the ordered pairs in $R$
and also add $(a,c)$.

The condition that we declare $xSy$ -- meaning that we include
$(x,y)$ in $S$ if "there exist $x_1,\ldots, x_n\in A$ so that
$xRx_1, x_1Rx_2,\ldots,x_{n-1}Rx_{n},x_{n}Ry$" expresses in formal terms
the idea that we include $(x,y)$ in $S$ if $x$ and $y$ *should* be related
if $R$ *were* transitive.

In particular, suppose $R$ were in fact already transitive.  Then
if there were a sequence of $x_i$ as above, the transitive property
would force $(x,y)$ to already be in $R$.  So if $R$ is transitive,
then the $S$ constructed in this problem would already be $R$.

**Proof:** First we prove that $S$ is an equivalence relation.
We must show that $S$ is reflexive, symmetric, and transitive.

*$S$ is reflexive.* Given $x\in A$, let $x_1=x$ and $y=x$.  Then
 because $R$ is reflexive we know that $xRx_1$ and $x_1Ry$.
 So $x_1$ is a sequence of length one that meets the condition
 for $xSx$ to be true.

*$S$ is symmetric.* Let $x,y\in A$ and suppose $xSy$.  Then
there is a sequence $x_1,\ldots, x_n$ so that
$$
xRx_1,\ldots, x_nRy
$$
as in the defining property for $S$.  Since $R$ is symmetric,
we can reverse all of these ordered pairs to obtain a sequence
$$
yRx_n,\ldots, x_1Rx.
$$
If we renumber the sequence $x_1,\ldots, x_n$ in reverse order,
with $x'_i=x_{n-i+1}$ for $i=1,\ldots, n$, then we have a sequence
$$
yRx'_1,\ldots, x'_nRx
$$
and therefore $ySx$.

*$S$ is transitive.*  Let $x,y,z\in A$ and suppose $xSy$ and $ySz$.
Then we have sequences $x_1,\ldots, x_n$ and $x'_1,\ldots, x'_m$
so that
$$
xRx_1,\ldots, x_nRy
$$
and
$$
yRx'_1,\ldots, x'_nRz.
$$
If we combine the two sequences into a long sequence of length
$n+m$ where $x''_i=x_i$ for $i=1,\ldots, n$ and $x''_i=x'_{i-n}$
then we have
$$
xRx''_1,\ldots, xRx''_n,xRx''_{n+1},\ldots, x''_{n+m}Rz
$$
and so $xSz$.  Therefore $S$ is transitive.

Next we must show that $R\subset S$. In other words, we must show
that if $x$ and $y$ are in $A$, and  $xRy$, then $xSy$.  For this,
make a sequence where $x_1=x$ and $x_2=y$.  Then $xRx_1$
since $R$ is reflexive, $x_1Rx_2$ by hypothesis, and $x_2Ry$ by reflexivity
again.  Therefore
$$
xRx_1, x_1Rx_2, x_2Ry
$$
gives a sequence that tells us that $xSy$.

Finally, we need to show that $S$ is the *unique smallest equivalence
relation on $A$ containing $R$*.  Here, *smallest* means that any
other equivalence relation that contains $R$ also contains $S$. In
other words, if you want to make $R$ transitive, the very least you
can do is add the relations that create $S$.  So
we must show that if $T$ is an equivalence relation that contains $R$,
then $S\subset T$.

Suppose therefore that $(x,y)\in S$.  This means that there is a sequence
$x_1,\ldots, x_n$ so that
$$
xRx_1,\ldots, x_nRy
$$
as in the defining property for $S$.  Since $R\subset T$, we have
$$
xTx_1,\ldots, x_nTy
$$
and since $T$ is transitive, this means that $xTy$.  Therefore
$(x,y)\in T$ and we have shown that $S\subset T$.

Finally, we must show that $S$ is the *unique* smallest equivalence relation.  This means that if $S$ and $S'$ are two equivalence relations
containing $R$, and having the property that, if $T$ is another equivalence
relation containing $R$, then $S\subset T$ and also $S'\subset T$, then
$S=S'$.  But if $S$ has this property, it means that $S\subset S'$
since $S'$ is an equivalence relation; and if $S'$ has this property it means that $S'\subset S$.  Therefore indeed $S=S'$.



