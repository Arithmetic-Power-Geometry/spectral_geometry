# P49 parity-completed spectral observability: candidate, test, prior art

For G fixed and B=bJ, define H_b(t)=sum_{Z^4}exp(-t E_b), O_b(t)=sum_{Z^4}(m.n)exp(-t E_b). These converge absolutely for t>0. Exact relabeling (m,n)->(-m,n) proves H_-b=H_b and O_-b=-O_b. If O_b(t)!=0, the ordered pair (H_b(t),O_b(t)) distinguishes b from -b. If O_b=0 at selected t, this particular pair does not distinguish them; multiple times may help but cannot guarantee distinction.

Candidate local conditioning score for unknown amplitude c and b: det [[H, c dH/db],[O,c dO/db]]=c(H O'-O H'). For c!=0 and nonzero determinant, inverse function theorem gives a locally unique solution for (c,b). This is a standard inverse function theorem application, not new mathematics. It does NOT establish global identifiability or distinguish arbitrary O(2,2;Z) duality classes.

Executable experiment code: papers/PAPER-03/code/p49_parity_completion.py, run using numpy over [-5,5]^4 at t=2.
b=-.2: H=3.9722045751 O=-6.20243564979e-7
b=0: H=3.97220609888 O≈0
b=+.2: H=3.9722045751 O=+6.20243564978e-7
At b=.2, H O'-O H'=5.0296628775e-6. Small O indicates severe noise sensitivity. The determinant is computed from truncated sums and not an interval certificate for the full infinite sums.

## Prior art
Datta, Duary, Kraus, Maity, Maloney, 'Adding flavor to the Narain ensemble', JHEP 05 (2022) 090, DOI 10.1007/JHEP05(2022)090, develops flavored Narain partition functions and heat equations. Spin-sensitive moments follow from differentiating appropriate torus angular/fugacity dependence; neither this observation nor the parity relation should be described as newly invented. Classical inverse function theorem, sensitivity determinants and optimal experimental design are established.

## Novelty gate
P49 introduces a named problem-specific candidate, NOT proven new mathematical theory. Known mathematical ingredients and existing flavored-partition-function literature are substantial. NO-GO as novel theorem or Q1 paper. Next P50: construct validated interval bounds for O and O', then compare with the full complex-modulus theta function and spin-resolved Fourier coefficients; test rank and conditioning across nondual and dual pairs. Any new theorem must exceed these prior methods.
