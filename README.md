# Five-Qubit Robust Stabilizer Decoding — Reproducibility Code

Exact arithmetic for the results in:

Akhtar, M. A. K. (2026). *Exact Robustness Certificates for Five-Qubit Stabilizer Decoding: Decoder Switching and a Deterministic–Randomized Minimax Separation* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.23853848

## Requirements

Python 3.10+ and SymPy.

```bash
python -m pip install sympy
python code/p127_two_parameter_dephasing.py
python code/p128_exact_switching.py
python code/p132_independent_exact_audit.py
python code/verify_additional_claims.py
```

All checks use symbolic or exact rational arithmetic. No random seeds or external datasets are needed.

## Scope

- `p127_two_parameter_dephasing.py`: two-parameter syndrome–coset masses and nominal decoder change.
- `p128_exact_switching.py`: coupled-family switching roots and per-syndrome audit.
- `p132_independent_exact_audit.py`: 256 deterministic candidates, 21 polynomials, 20 exact rational witnesses, and stationary points. Its output contains the rational witnesses.
- `verify_additional_claims.py`: homogeneous polynomial, coupled-family randomized certificate, adaptive upper bound, and orientation test.

The code assumes ideal syndrome extraction and independent Pauli errors conditional on the noise parameter. It is a small-code exact certificate, not a scalable quantum decoder. The Zenodo article is the scholarly reference; this repository contains reproduction software only.

Copyright © 2026 Mohammad Amir Khusru Akhtar. Licensed under Apache License 2.0.
