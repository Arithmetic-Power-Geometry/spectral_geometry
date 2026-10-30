# P02 — Four-probe reconstruction: exact derivation (2026-10-30)

## Status
A correct elementary improvement of the source five-probe construction, not a claimed novel publishable theorem. Fixed integral charge basis and B-field branch b∈[-1/2,1/2] are essential.

Let G=[[a,d],[d,c]] positive definite, B=b[[0,1],[-1,0]], v=(m1,m2,n1,n2), E(v)=(m+Bn)^T G^-1(m+Bn)+n^T G n. Standard basis e1,...,e4 of Z^4.

Take x=E(e1), y=E(e2), z=E(e1+e2), h=E(e1+e4).
A=G^-1=[[x,(z-x-y)/2],[(z-x-y)/2,y]].
Set c=(A^-1)[2,2]. Since e4 has n=(0,1), Bn=(b,0), and e1+e4 has m=(1,0), we have h=x(1+b)^2+c. For b∈[-1/2,1/2], 1+b>0 and b=sqrt((h-c)/x)-1. Hence the map of these four energies is injective on SPD(2)×[-1/2,1/2] in the specified basis. This uses the principal nonnegative square root and x>0.

**Classical lower bound:** SPD(2)×(-1/2,1/2) is a four-dimensional open parameter manifold. A continuous injective map into R^k requires k≥4 by invariance of dimension. All fixed charge-labelled energy maps are continuous. Thus four is minimal among nonadaptive fixed continuous scalar charge-energy evaluations in this restricted fixed-basis model. This is a direct dimension argument, not a new topological theorem.

**Crucial limitation:** On unrestricted real b, h has reflection ambiguity b ↦ -2-b; e.g. b=0 and b=-2 produce the same four chosen readings for fixed G. Integral B-shifts relate these particular parameters physically, but fixed-basis injectivity over all b is false. The principal interval is not asserted to be a full fundamental domain for O(2,2;Z) including all other dualities.

**Novelty gate:** This formula is elementary, and prior-art uniqueness is unverified. It does not by itself justify writing a research paper. The original five-probe theorem was only a sufficient upper bound, so this is a correction/strengthening of the baseline, not a contradiction.

**Verification:** SymPy exact symbolic derivation and two rational examples tested during P02; persistent standalone verification program is saved separately. Reproducibility must be rerun by a second implementation before stronger certification.
