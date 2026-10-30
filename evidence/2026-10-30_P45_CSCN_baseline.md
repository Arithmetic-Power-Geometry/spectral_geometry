# P45 CSCN candidate: theorem, reproducible benchmark, novelty gate

## Problem
Recover parameters p=(a,c,d,b) of positive-definite G=[[a,d],[d,c]], B=bJ from five charge-labelled zero-mode energies, or later from smooth spectral statistics. The five labelled-probe inverse is already proved in Manuscript 1; it is NOT novel.

## Exact inverse
Let x=E(e1), y=E(e2), z=E(e1+e2), w=E(e4), h=E(e1+e4). Put q=(z-x-y)/2, A=[[x,q],[q,y]], G=A^{-1}, b=(h-x-w)/(2x). This reconstructs exactly in rational arithmetic.

## Newton theorem (classical)
For a C2 map F:R4 -> R5 with F(p*)=data and Jacobian of full column rank at p*, Gauss-Newton with exact derivatives has local quadratic convergence for zero-residual consistent data, provided the Jacobian remains Lipschitz and the initial iterate is sufficiently close. Proof: Taylor F(p)=J(p)(p-p*)+O(||p-p*||²); left pseudoinverse J(p)^+ bounded in a neighbourhood; update p+ = p-J(p)^+(F(p)-data), hence ||p+-p*|| <= (L/2) sup||J^+|| ||p-p*||². This is a standard Newton/Gauss-Newton argument, NOT a novel theorem. Finite-difference Jacobian in supplied implementation is an approximation, so this quadratic theorem does not certify its asymptotic behavior.

## Executed test
At p*=(2,3,1/3,1/5), exact rational inverse recovers p* exactly. Starting p0=(1.9,3.1,0.25,0.25), damped finite-difference Gauss-Newton residual infinity norm sequence:
0.19760342552795418, 0.006165311229215931, 2.0147869684183917e-05, 2.680762278828297e-10, 1.1102230246251565e-16.
Executable script /mnt/data/p45_cscn.py.

## Scope
This is a baseline on LABELLED charge observations. It does not solve the hard unlabelled inverse problem and is not yet a new algorithm. Proposed future candidate: rigorously bounded homotopy continuation on smooth heat/theta moments with adaptive observation selection; must establish global identifiability or certify local branches and duality ambiguity. Trapezoidal quadrature can approximate heat integrals, but fast quadrature and Newton convergence do not themselves imply novel mathematics.

## Novelty gate
Prior art includes classical Newton-Kantorovich, Gauss-Newton and numerical continuation; exact labelled inverse already in Manuscript 1. NO-GO novelty. Next P46: define genuinely unlabelled smooth heat observables, test identifiability rank and duality ambiguity, and compare against established inverse theta/heat trace algorithms before claiming any new contribution.
