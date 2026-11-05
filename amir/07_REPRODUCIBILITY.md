# Stage 07 — independently reproduce numerical evidence

Write a reproducibility runner that executes all supplied scripts from a clean checkout and records Python/version/dependencies, commands, exit codes, exact output hashes and elapsed resource usage. Verify every row and column in all seven manuscript tables. Independently recompute: 153 semiprimes chosen from 18 primes; the 15×15 ordered-pair total 32,130; four recovery classifications; larger windows and scaled design; complete-residue CRT checks; bounded-window coefficients; threshold counts; square-free 3/4-prime examples; prime-power values for (5,3),(7,3),(5,4),(7,4),(5,5),(7,5),(13,4),(5,6). Check sums and denominators and distinguish deterministic selected samples from random samples.

Make verification implementations structurally independent (e.g. original congruence predicates vs local state tables; exact modular enumeration vs coefficient extraction). Never write 'independent' when implementations share the same potentially faulty core. List feasible exhaustive limits and skipped large cases.

**Deliver:** `RESULTS_AUDIT.md`, `TABLE_REPRODUCTION.csv`, executable checks, dependency manifest and full logs. **Gate:** zero unexplained discrepancies; reconcile all disagreements before manuscript freeze.
