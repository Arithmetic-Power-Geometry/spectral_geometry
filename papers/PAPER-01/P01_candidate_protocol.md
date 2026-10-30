# P01 candidate protocol — no manuscript

**Priority P02 question:** Can four predeclared integer charge probes recover all four real d=2 background parameters, in a fixed charge basis, for all G≻0 and b in a specified B-field fundamental interval? If not, characterize maximal generic recovery and produce a rational exact counterexample.

## Exact model
G=[[a,d],[d,c]], ac-d²>0; B=b[[0,1],[-1,0]]. For v=(m,n)∈Z²×Z², E(v)=(m+Bn)^T G^{-1}(m+Bn)+n^T G n.

## Independent tests
T01 Reimplement five-probe inversion from source using Fraction and symbolic algebra; enumerate small rational SPD G and b, verify equality of reconstructed inputs.
T02 Enumerate all probe 4-tuples from charge box {-1,0,1}⁴ modulo sign and trivial duplicates; compute 4×4 symbolic Jacobian and its determinant; discard identically singular sets. A nonsingular Jacobian proves *local* generic invertibility only, not global uniqueness.
T03 For surviving tuples solve polynomial systems after clearing det G, with exact rational inputs; search distinct real SPD solutions and distinct b within stated interval. Reject extraneous roots and report full rational witnesses if found.
T04 Test symmetry-related collisions: b↦-b, b↦b+integer, basis GL(2,Z) and full O(2,2;Z) separately. Record fixed-basis versus orbit equivalence.
T05 Compare with five-probe inverse under interval perturbations; calculate certified Jacobian singular-value bounds on compact parameter boxes; exclude boundary/degenerate regions.
T06 Reproduce original threshold at b=1/5, 3313/1325 and independently verify older 3373/1325 is not the minimum.
T07 Attempt 3-probe global reconstruction and record dimension-theoretic obstruction; do not count it as new.
T08 Independent implementation using SageMath or SymPy and exact rational test corpus, with pinned versions and logs.

## Falsification standards
Finite search does not prove a universal theorem. A rank-4 Jacobian does not prove global injectivity. A numerical collision does not prove exact equality. A proof in a fixed basis is not a classification of T-duality orbits. All failed searches remain archived.
