from fractions import Fraction as F
from itertools import product
from collections import Counter
from math import isqrt
def spectra(A,r,L,axis):
 g1,g2=A/r,A*r
 c=min(g1,g2,1/g1,1/g2)
 R=isqrt(L//c)
 out=Counter()
 for m1,m2,n1,n2 in product(range(-R,R+1),repeat=4):
  E=m1*m1/g1+m2*m2/g2+g1*n1*n1+g2*n2*n2
  if E<=L:
   s=m1*n1+m2*n2
   sign=(-1 if (m1 if axis==1 else m2)%2 else 1)
   out[(E,s)]+=sign
 return out
A,r,L=F(2),F(3,2),F(4)
x1=spectra(A,r,L,1)
y1=spectra(A,1/r,L,1)
y2=spectra(A,1/r,L,2)
assert x1==y2
assert x1!=y1
first=min(e for e,s in set(x1)|set(y1) if x1[(e,s)]!=y1[(e,s)])
assert first==F(1,3)
print('PASS: transported character equality through L=4')
print('False discrepancy at',first,'if same coordinate label is compared')
print('Differing coefficient positions',sum(x1[k]!=y1[k] for k in set(x1)|set(y1)))
