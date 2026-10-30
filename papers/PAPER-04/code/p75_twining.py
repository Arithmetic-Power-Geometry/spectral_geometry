from fractions import Fraction as F
from itertools import product
from collections import Counter
from math import isqrt

def spectra(A,r,L):
    g1,g2=A/r,A*r
    c=min(g1,g2,1/g1,1/g2)
    R=isqrt(L//c)
    ordinary=Counter()
    twined=Counter()
    for m1,m2,n1,n2 in product(range(-R,R+1),repeat=4):
        e=m1*m1/g1+m2*m2/g2+g1*n1*n1+g2*n2*n2
        if e<=L:
            s=m1*n1+m2*n2
            ordinary[(e,s)]+=1
            twined[(e,s)]+=(-1 if m1%2 else 1)
    return ordinary,twined,R

for A,r in [(F(1),F(1)),(F(1),F(4,3)),(F(3,2),F(2))]:
    ordinary,twined,R=spectra(A,r,F(2))
    assert ordinary[(F(0),0)]==twined[(F(0),0)]==1
    assert all(abs(twined[k])<=ordinary[k] for k in ordinary)
    first=min(e for (e,s),v in ordinary.items() if twined[(e,s)]!=v)
    print('A,r=',A,r,'R=',R,'first twining change=',first)
print('PASS exact charge-sector shift twining')
