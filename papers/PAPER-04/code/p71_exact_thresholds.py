from fractions import Fraction as F
from itertools import product,combinations
from collections import Counter
from math import isqrt
V=[F(1),F(4,3),F(3,2),F(2),F(3)]
models=[(a,b) for i,a in enumerate(V) for b in V[i:]]
def coefficients(A,r):
 g1,g2=A/r,A*r
 return Counter((g1,1/g1,g2,1/g2))
def spectrum(A,r,L):
 g1,g2=A/r,A*r
 c=min(g1,g2,1/g1,1/g2)
 R=isqrt(L//c)
 out=Counter()
 for m1,m2,n1,n2 in product(range(-R,R+1),repeat=4):
  E=m1*m1/g1+m2*m2/g2+g1*n1*n1+g2*n2*n2
  if E<=L:out[(E,m1*n1+m2*n2)]+=1
 return out
def first_difference(x,y,spin):
 if spin:return min((e for e,s in set(x)|set(y) if x[(e,s)]!=y[(e,s)]),default=None)
 def coarse(z):
  o=Counter()
  for (e,s),v in z.items():o[e]+=v
  return o
 a,b=coarse(x),coarse(y)
 return min((e for e in set(a)|set(b) if a[e]!=b[e]),default=None)
S={p:spectrum(*p,F(4)) for p in models}
hist=Counter()
for p,q in combinations(models,2):
 a,b=coefficients(*p),coefficients(*q)
 delta=min(c for c in a.keys()|b.keys() if a[c]!=b[c])
 e=first_difference(S[p],S[q],False)
 s=first_difference(S[p],S[q],True)
 assert e==delta and s==e,(p,q,delta,e,s)
 hist[e]+=1
assert sum(hist.values())==105
print('PASS: 105 exact pairwise thresholds; coefficient-multiset prediction agrees with complete energy and spin spectra')
print('histogram',sorted(hist.items()))
print('maximum',max(hist))
