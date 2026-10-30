# P24 published refined genus-two polynomial reconstruction

Primary source: Johan Henriksson, Ashish Kakkar, Brian McPeak, Narain CFTs and quantum codes at higher genus, JHEP 04 (2023) 011, DOI 10.1007/JHEP04(2023)011, https://arxiv.org/pdf/2205.00025 . Verified section 3.2.3 equations (3.37)-(3.48), section 4.4 matrices (4.19). Note PDF text extraction displays a likely typo in Eq. (3.46) x[XZ]=x[ZZ]; Eq. (3.47) unambiguously groups XZ and ZX, while XX and ZZ already form y6. The implementation follows (3.47).

Exact executable calculation (Python Counter, all 128 codewords and 16384 ordered pairs per code): genus-one refined enumerators equal; genus-two refined ten-variable enumerators each contain 1251 monomial labels; 756 coefficients differ. Lexicographically first difference in y0..y9 is exponent (0,0,0,0,0,0,1,0,2,4), coefficients 14 and 4. Separating substitution from Eq. (3.48) maps both genus-two polynomials exactly to the outer product of the shared genus-one polynomial with itself. All assertions PASS.

Unlike P22, the ten-variable grouping here is source-grounded Eq. (3.47), not unordered handle exchange. P23's warning remains valid against arbitrary orbit identifications.

LIMITS: refined polynomial coefficients are not Fourier coefficients. Although equations (3.37)-(3.46) identify the theta-function linear combinations, the normalized genus-two physical partition function, its explicit q-expansion, oscillator factor and independent Sp(4,Z) modular checks are not yet executed. The underlying genus-two distinction and factorization are already reported in section 4.4: reproduction, not novel theorem. Q1 NO-GO.
