# P04 exact baseline, 2026-10-30

Execution: Python 3 with fractions.Fraction, collections.Counter, itertools.product; independently executed in container, PASS.
Input G=[[2,1/3],[1/3,3]], b=1/5, cutoff 3; analytic completeness bound inherited from source manuscripts, NOT independently reproved in this run.
Enumerated 729 integer charges, 39 states at E<=3 in each sign of B; unlabelled energy multiplicities identical; first spin-labelled discrepancy 3313/1325; counts at first difference (+b): spin -1=2, +1=0; (-b): spin -1=0, +1=2. Exact charge reflection (m,n)->(-m,n) checked on all 729 candidates.
Negative control: B sign does NOT produce distinct unoriented physical theories by itself; it is known worldsheet parity. The earlier 3373/1325 witness is not minimal.
The new script is stored in papers/PAPER-01/code/p04_unlabelled_baseline.py. This reproduces existing results and cannot count as independent new mathematics.
Literature check: Schiemann 1997 proves ternary theta rigidity (DOI 10.1007/s002080050086); Conway and Sloane 1992 give four-dimensional isospectral lattices (DOI 10.1155/S1073792892000102). Neither alone resolves constrained Narain generalized-metric theta injectivity. Existing reference.bib already contains both; no duplicate entry added.
