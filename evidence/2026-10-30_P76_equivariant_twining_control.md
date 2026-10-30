# P76 — Equivariant symmetry transport and false-positive control
Date: 2026-10-30.

## Exact construction
Rectangular Narain G=diag(A/r,Ar), B=0, with A=2, r=3/2. Coordinate swap P maps r to 1/r=2/3, swaps momenta and windings m1<->m2, n1<->n2, preserves E and spin, and conjugates the first-coordinate half-translation character (-1)^m1 to second-coordinate (-1)^m2. This is an exact isomorphism of symmetry-decorated charge sectors.

## Executed controls
Standard-library Fraction code papers/PAPER-04/code/p76_equivariant_twining.py, complete energy cutoff E<=4 via coercivity bound. First-coordinate character at (2,3/2) equals transported second-coordinate character at (2,2/3) at every (E,s) through 4. If first-coordinate characters are naively compared at both backgrounds, the first apparent difference is E=1/3; 13 coefficient positions differ. These are *false positives* due to inconsistent symmetry identification. Full charge-level equality follows algebraically from coordinate permutation; finite test is a cross-check, not sole proof.

## Physical scope and prior art
Target half-shifts are standard CFT symmetries, with oscillator action trivial. This example does not construct twisted-sector partition functions or establish modular covariance of the full orbifold sector array. Ando, Kawabata, Nishioka, 'Gauging Z_N symmetries of Narain CFTs', JHEP 02 (2026) 058, DOI 10.1007/JHEP02(2026)058, provides important contemporary prior art. HKM 'Narain CFTs and quantum codes at higher genus', JHEP 04 (2023) 011, DOI 10.1007/JHEP04(2023)011, establishes substantial existing genus-refinement framework.

## Strict novelty result
An arbitrary fixed coordinate-character comparison is not a duality-invariant separation test. Equivariant transport is essential and standard. P76 provides a validated negative control, not a new physical theorem or new inequivalent pair.

## P77
Search only among pairs with independently certified duality inequivalence and identical ordinary full spectra (not just finite windows); require common symmetry group, explicit equivariant identification, and physical twisted-sector covariance. If no viable candidate, terminate this fourth-paper direction and reassess independent questions.
