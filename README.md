# Exact Robustness Certificates for Five-Qubit Stabilizer Decoding

Reproducibility materials accompanying *Exact Robustness Certificates for Five-Qubit Stabilizer Decoding: Decoder Switching and a Deterministic–Randomized Minimax Separation* (Mohammad Amir Khusru Akhtar, 2026).

## Scope

This repository version supports the five-qubit [[5,1,3]] and Steane [[7,1,3]] exact finite-code results under ideal syndrome extraction. The 128-row Steane dataset is an exhaustive **synthetic** enumeration, not hardware data. No large-code runtime or external-decoder performance superiority is claimed.

## Reproduce

Requires Python 3.10+ and SymPy. From the repository root:

```bash
python -m pip install sympy
python code/orientation_exact.py
python code/p129.py
python code/p130.py
python code/p131_verify.py
python code/p132_audit.py
python code/switching_independent_audit.py
python code/verify_steane_css.py
python code/verify_steane_heterogeneous.py
```

`p131_verify.py` is an exploratory numerical check and **not** the final optimality certificate; use `p132_audit.py` for the exact five-qubit deterministic optimum.

## Certificates and data

- `evidence/deterministic_witnesses.json`: 20 rational exclusion witnesses for the five-qubit case.
- `evidence/steane_heterogeneous_witnesses.json`: 40 rational exclusion witnesses for the strict Steane heterogeneous gap.
- `evidence/steane_128_error_patterns.csv`: all 128 supported pure-Z Steane errors, generated symbolically.
- `evidence/syndrome_switching_audit.json` and `.csv`: switching checks.
- `evidence/final_reproducibility_report.json`: earlier local verification record; not a GitHub release audit.
- `SHA256SUMS.txt`: SHA-256 checksums for files in this package.

The Steane result certifies `R_det < 0.4999 < R_rand = R_ML = 1/2` for rates `(t,t,t,t,2t,2t,2t)`, `0 <= t <= 1/2`; it does not establish the exact Steane deterministic optimum.

The five-qubit heterogeneous result certifies the deterministic optimum approximately `0.74959189859249` and randomized optimum `3/4` for rates `(t,t,2t,2t,2t)`.

## Journal version

`submitted_manuscript.pdf` is the author-supplied manuscript version for repository matching. The accompanying Python files and evidence are from the final local submission package. Check the PDF and release hashes before sharing a version-specific link with the journal.

Copyright © 2026 Mohammad Amir Khusru Akhtar. Apache License 2.0 applies to original software; third-party dependencies retain their own licenses.
