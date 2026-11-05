# Cubic collision counting: square-free and prime-power moduli

Research notes and exact reproducibility tests for the factorization
`x^3-y^3=(x-y)(x^2+xy+y^2)`.

## Results

- Exact bounded-window coefficients for arbitrary square-free moduli whose prime factors exceed 3.
- Explicit strict prime-power masking counts for every exponent e, including p=3.
- A bridge decomposition to the original manuscript-style proper-GCD masking statistic.
- A mixed-prime first-occurrence witness: N=35, first collision at X=9.

## Reproduce

Run `python3 verify.py` and `python3 verify_bridge.py`. The scripts use only Python's standard library and exhaustively compare finite formulas with residue-pair enumeration for small moduli.

## Important distinction

**Strict prime-power masking** means `N | DH`, `N ∤ D`, and `N ∤ H`. **Original manuscript-style masking** means `N | DH` and at least one of `gcd(D,N)`, `gcd(H,N)` is strictly between 1 and N. These are distinct. For N=125, the counts are respectively 580 and 620; for N=9, respectively 12 and 24.

The full statements and proofs appear in `theorems.md`. Neither numerical agreement nor the proofs alone establishes literature priority. The existing manuscript and QEC files are unchanged.
