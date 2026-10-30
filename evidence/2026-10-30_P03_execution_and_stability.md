# P03 evidence — 2026-10-30

Independent clean-process execution: Python SymPy 1.14.0, exact arithmetic. Assertions: A reconstructed symbolically equals G^-1; fourth energy equals x(1+b)^2+c; rational test backgrounds (2,3,1/3,1/5) and (3/2,7/4,1/4,-2/5) both exactly recovered; unrestricted-b collision b=0 versus b=-2 for all four probes. All PASS.

Derived deterministic noise bound: if lambda_min(G^-1)>=alpha>0, each measured energy error<=eps, 3eps<=alpha/2 and K(alpha)eps<=1/8 with K(alpha)=13/(2alpha)+12/alpha^3, then ||Ghat-G||_2<=6eps/alpha^2 and |bhat-b|<=2K(alpha)eps. Proof and caveats in papers/PAPER-01/P03_stability_and_validation.md. Not independently formalized or established novel.

Negative findings: P02 improvement over five probes is elementary, stability follows standard inverse perturbation inequalities; no justified standalone paper claim. No additional verified bibliography was needed for these internal computations; reference/reference.bib remains append-only and unchanged.
