# P19 exact published n=7 code pair reproduction (2026-10-30)

Primary source: Johan Henriksson, Ashish Kakkar, Brian McPeak, 'Narain CFTs and quantum codes at higher genus', JHEP 04 (2023) 011, DOI 10.1007/JHEP04(2023)011, equation (4.19) page 33, and text after equation (4.20). https://scoap3-prod-backend.s3.cern.ch/media/files/76861/10.1007/JHEP04(2023)011_a.pdf

Exact matrices transcribed:
B1 rows 0100010 / 1010001 / 0101111 / 0010100 / 0011000 / 1010001 / 0110010
B2 rows 0100011 / 1010001 / 0101111 / 0010100 / 0011000 / 1010001 / 1110010

Independent execution: each symmetric B defines binary graph stabilizer labels (a,Ba) for all a in F2^7. The refined genus-one enumerator counts I=(0,0), Y=(1,1), X/Z=(1,0)/(0,1), reproducing equality of 16 monomial coefficients and total 128 words. The complete 16-variable genus-two joint-type enumerator counts ordered pairs: 16384 pairs each; nonzero terms 5186 and 5246; differing coefficient labels 7956. Lexicographically first differing 16-entry exponent vector (0,0,0,0,0,0,0,0,0,0,0,3,0,1,2,1) has coefficients 0 and 1. All calculations are exact integer arithmetic, and checks are asserted in saved code.

Limits: this is reproduction of an already published example, NOT novel; no complete genus-two physical partition function, oscillator normalization or Sp(4,Z) covariance has been independently calculated. A difference in complete enumerators alone does not establish an independently normalized physical observable without checking the relevant theta substitution. Published authors establish genus-two difference.
