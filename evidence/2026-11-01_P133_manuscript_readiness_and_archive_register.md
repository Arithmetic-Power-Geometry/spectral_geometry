# P133 — manuscript writing decision and reproducibility register (2026-11-01)

## Decision
**GO to drafting the revised existing paper now; REVISE before journal submission.** No separate paper is authorized by this decision. The manuscript should be framed as an exact, reproducible five-qubit robust-decoding case study, not a new general theorem.

## Established results and provenance
P127: exact heterogeneous dephasing mass polynomials and a decoder switch.
P128: four algebraic switching thresholds, 13 syndrome changes.
P129: five-piece exact adaptive ML curve.
P130: fixed randomized certificate of worst-case success 3/4; adaptive ML robust success 3/4; nominal fixed deterministic worst case zero.
P131–P132: optimal fixed deterministic robust success min F(t)≈0.74959189859249, F(t)=16t^5-28t^4+10t^3+3t^2-2t+1. Exhaustive proof reduces to 256 candidates, 21 polynomials, with rational counter-witnesses for 20 and root-isolation bound for F. Distinguish nominal failure from optimal deterministic performance.

## Executable code status
Existing repository: code/p127_two_parameter_dephasing.py and code/p128_exact_switching.py. Newly committed: code/p132_independent_exact_audit.py. P129, P130, and P131 scripts were executed in the local workspace and are **not yet archived as GitHub source files**; their evidence records remain in evidence/. Do not claim full source archival until all three scripts and logs are uploaded and verified.

## Important caution
The P131 local script emits a separate 'CERT_DETERMINISTIC' line for a *different* polynomial with lower success; that line is not the optimal result. Use its 'TOP' ranking and the independently verified P132 candidate enumeration. P132 explicitly identifies optimal decision string 0011011000111011. Do not use the unrelated CERT_DETERMINISTIC line as the optimum.

## Remaining targeted work
1. Upload remaining P129/P130/P131 executable scripts and logs.
2. Audit proof against nearest literature, especially prior robust quantum decoder optimization and exact enumerator approaches; no unverified first-ever claim.
3. Integrate one clear results section into original manuscript LaTeX with definitions, proofs, reproducibility pointers and limitations; avoid changing unrelated claims.
4. Rebuild PDF and check tables, equations, citations, numerical precision, and appendix.
5. Separate conditional independent site errors from uncertainty coupling; distinguish syndrome-decoder randomization from quantum recovery in general.
6. If targeting a high-selectivity journal, add a fair generalization or independent baseline benchmark.

## Gate
Writing: GO. Submission: REVISE. Fundamental-theorem novelty: NOT ESTABLISHED.
