# P47: full Narain theta heat tail and inverse-conditioning audit

## Rigorous tail lemma
For G=[[2,1/3],[1/3,3]] and |b|<=1/2, Gershgorin yields 5/3 <= lambda_min(G), lambda_max(G)<=10/3. Writing u=m+Bn, E=u^T G^-1 u+n^T Gn >= (3/10)||u||²+(5/3)||n||² >= (3/10)(||u||²+||n||²). Since ||m||²+||n||² <=2||u||²+(1+2||B||²)||n||² <=2(||u||²+||n||²), E >= (3/20)(||m||²+||n||²).

For t>=1, omitted terms outside [-K,K]^4 in H(t)=sum_{Z^4}exp(-t E) are bounded by
8 (1+sqrt(pi/(alpha*t)))^3 exp(-alpha*t*(K+1)^2)/(1-exp(-alpha*t*(2K+3))),
alpha=3/20. Proof: union over 4 coordinates and both signs, bound remaining three Gaussian sums by 1+sqrt(pi/a), bound one-sided tail by geometric ratio of consecutive Gaussian terms. Valid for any |b|<=1/2.

## Executed script and numerical results
Executable /mnt/data/p47_full_theta_certified.py.
K=8 tail 0.00778689358020442; K=12 tail 1.3817608331869994e-08; K=16 tail 2.0786627960676565e-16.
For K=12 and b=0.2, exact termwise t-integral from 1 to 2 equals 6.212902960758656.
Trapezoidal N=16: 6.218107186676342; N=32: 6.214204941181948; N=64: 6.213228513765471; N=128: 6.212984352631599. This confirms second-order quadrature empirically.
Truncated inverse root using Brent's method b=0.19999999997547943, residual at floating-point zero. At b=0.1, integrated difference relative to b=0.2 only +3.676831354937349e-07; b=0.3 difference -4.544797640448905e-07. Root accuracy in truncated model does NOT certify parameter accuracy for infinite heat trace: tail uncertainty and ill-conditioned derivative must be propagated.

## Novelty audit and honest gate
Uniform Gaussian lattice tails, trapezoidal O(N^-2), Newton/Kantorovich, Krawczyk/interval Newton are established methods. Alefeld-Gienger-Potra, Efficient Numerical Validation of Solutions of Nonlinear Systems, SIAM J Numer Anal 31 (1994), DOI 10.1137/0731013, already combines Newton and rigorous interval certification. Trefethen-Weideman, The Exponentially Convergent Trapezoidal Rule, SIAM Rev 56 (2014), DOI 10.1137/130932132, covers stronger trapezoidal convergence in analytic settings. Novelty not established for this Narain specialization; no breakthrough claim. Next P48 derive and certify lower bound on derivative on a small b interval, choose better conditioned multiple t observations and spin refinement, and benchmark against direct spectral inversion.
