# Stage 01 — freeze baseline and map every claim

**Instruction:** inspect the supplied authoritative source files and compiled PDF; make no mathematical additions yet.

1. Inventory all files, their SHA-256 hashes, manuscript page count and build commands. Confirm article title, author, sections, theorem/proposition/corollary/table/figure/algorithm counts and actual cited reference count.
2. Extract every mathematical assertion: definitions, results, formulas, sample computations, complexity claims, empirical claims, scope limitations and novelty claims. Record the exact source section, equation/label, assumptions and dependency list.
3. Classify each as classical fact, proved here, derived corollary, computational observation, interpretation or unsupported claim. Create `CLAIM_MATRIX.md`.
4. Identify conflicting definitions of original masking and strict masking; clarify disjoint decomposition O_N=K_N+J_D+J_H and whether diagonals are excluded for each statistic.
5. Map abstract sentence ↔ numbered result ↔ proof ↔ verification ↔ conclusion sentence. Flag absent support rather than supplying it by assumption.
6. Verify local list T_p(a) is defined before first use; record all forward references, duplicate theorem proofs and notational collisions.
7. Compare source and rendered PDF page by page. Note text overflows, math glyph errors, table alignment, bibliography formatting and standalone declarations.

**Deliver:** `BASELINE_MANIFEST.md`, `CLAIM_MATRIX.md`, `DEPENDENCY_GRAPH.md`, `ISSUE_REGISTER.md`. **Gate:** all claims located and dependencies identified; otherwise FAIL. Do not call any part submission-ready.
