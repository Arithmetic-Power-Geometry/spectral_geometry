from fractions import Fraction as F
from math import gcd,isqrt
from collections import Counter
from itertools import product
def E(z,c):
 m1,m2,n1,n2=z
 return F(m1*m1,2)+F(m2*m2,1)/c+2*n1*n1+c*n2*n2
def spectrum(c,T):
 bounds=[isqrt((v*T).numerator//(v*T).denominator)+1 for v in (2,4,1,1)]
 out=Counter()
 for z in product(*(range(-b,b+1) for b in bounds)):
  e=E(z,c)
  if e<=T:out[e]+=1
 return out
def family(H):
 return sorted({F(p,q) for q in range(1,H+1) for p in range(1,H+1) if 3*q<=p<=4*q and gcd(p,q)==1})
def nearest(x,h):
 z=x/h+F(1,2)
 return z.numerator//z.denominator
if __name__=='__main__':
 for H in (12,24,48):
  C=family(H)
  for c in C:
   s=spectrum(c,F(1,2))
   v=min(e for e in s if e>0)
   assert v==1/c and s[v]==2
  gap=min(abs(1/C[i]-1/C[i+1]) for i in range(len(C)-1))
  assert gap>=F(1,H*H)
  assert len({nearest(1/c,gap/2) for c in C})==len(C)
  print('H',H,'N',len(C),'min_gap',gap,'H2gap',H*H*gap,'PASS')
 print('PASS')
