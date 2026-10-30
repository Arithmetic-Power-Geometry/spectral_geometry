# P46 Trapezoidal Heat–Newton (THN) exploratory experiment

## Exact obstruction (proved)
E_{G,B}(m,n)=E_{G,-B}(-m,n), hence every unlabelled energy-only functional, including full heat traces and integrated heat traces, is even under B reversal. No algorithm can infer the sign of B from these observations. This is known from Paper 1 and standard parity; not novel.

## Tested functional
For rational G=[[2,1/3],[1/3,3]], define truncated H_3(t,b)=sum_{(m,n):E<=3}exp(-tE), I_N(b)=composite trapezoidal quadrature of integral_1^2 H_3(t,b)dt. Enumerate all m in [-4,4]^2 and n in [-1,1]^2; the analytic E<=3 charge bound holds for |b|<=1/2. This is a TRUNCATED spectral statistic, not the full heat trace. At b=0 and at parameter values where a level crosses E=3, H_3 can be discontinuous; local Newton theorem applies only in a fixed active-set chamber.

## Executed numbers
b=0: I16=5.759860250965326, I32=5.75795541793958, I64=5.757479069625405, 43 states.
b=1/10: 5.697186243953071, 5.695419302149652, 5.694977445660414, 39 states.
b=1/5: 5.696884716328809, 5.695117947387817, 5.694676134095948, 39 states.
b=2/5: 5.6953147585388555, 5.693549087688473, 5.693107548853283, 39 states.
b=1/2: 5.696363828394451, 5.694597014637521, 5.694155190085165, 39 states.
Newton with finite-difference derivative and clipping, fixed N=32, target generated at b=1/5, initial b=.25: residuals -0.0010761701406751811, -0.00018636639321290005, -1.3090837432727653e-05, -8.7428626116548e-08, -4.004796494427865e-12, final b=.20000000026093304. This demonstrates fast LOCAL convergence to a synthetic target, not global injectivity, not error-certified inversion, and not the full spectrum.

## Quadrature theorem (classical)
For f in C²([1,2]), composite trapezoidal rule with N equal panels has error |I-T_N| <= (1/12N²) sup|f''|. For H_3, f''(t)=sum E²exp(-tE) and E<=3, so a crude uniform bound is (9 M)/(12N²), M=#active states; stronger termwise bounds possible. This bound controls quadrature only, NOT spectral truncation bias or inverse conditioning.

## Novelty audit
Trefethen & Weideman, The Exponentially Convergent Trapezoidal Rule, SIAM Review 56 (2014), 385-458, DOI 10.1137/130932132, establishes classical high-accuracy trapezoidal regimes; our finite-interval ordinary composite rule has only O(N^-2), not exponential convergence.
Dorai & Tortorelli, Transient inverse heat conduction problem solutions via Newton's method, International Journal of Heat and Mass Transfer 40 (1997), 4115-4127, DOI 10.1016/S0017-9310(97)00044-6, establishes Newton-type inverse heat algorithms.
Thus THN as tested is a combination of known numerical methods with a Narain-specific benchmark; NOT proven novel.

## Correct next research gate
Replace hard cutoff H_3 by full theta heat trace with certified lattice tail; derive interval-enclosed derivatives and inverse conditioning; show a local identifiable domain modulo B->-B and dualities, and compare numerical cost against direct spectral inversion. Search literature at theorem level. Publication NO-GO.
