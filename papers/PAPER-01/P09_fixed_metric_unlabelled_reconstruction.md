# P09 — Exact unlabelled reconstruction for a fixed metric family

Let G=2I_2 and B=bJ with J=[[0,1],[-1,0]], 0<=b<=1/2. Define E_b(m,n)=||m+bJn||^2/2+2||n||^2. Let E_*(b) be the smallest spectral energy strictly greater than 2.

**Proposition:** For 0<b<=1/2, E_*(b)=2+b²/2. At b=0, E_*(0)=5/2. Thus the unlabelled spectrum through energy 5/2 determines b on [0,1/2].

Proof: If ||n||²>=2 then E>=4. If n=0, energies are ||m||²/2, and the smallest strictly greater than 2 is 5/2 (||m||²=5). If ||n||²=1, the winding term is 2 and minimizing over integer m reduces to the distance from bJn to Z². For 0<=b<=1/2 the minimum squared distance is b², achieved by m=0. Every such state with energy >2 has energy at least 2+b²/2, except b=0 where these minima equal 2. For b>0, 2+b²/2<=17/8<5/2, hence is the first level strictly above 2. At b=0, the next winding level is 5/2, and the momentum level 5/2 exists. QED.

This is an elementary restricted-family result. It is NOT an assertion of novelty or generic Narain spectral rigidity. b=0 is identifiable because E_*=5/2, while positive b gives E_*<=17/8. Fixed G and parity-reduced b interval are essential. A finite cutoff of 5/2 suffices in this family, though the claim is not optimality of the cutoff.

P10: test robustness to measurement errors, degeneracy and unknown G; perform theorem-level prior-art kill-test before any paper.
