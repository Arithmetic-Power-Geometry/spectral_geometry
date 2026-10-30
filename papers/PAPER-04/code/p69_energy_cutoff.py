from fractions import Fraction as F
from itertools import product
from collections import Counter
from math import isqrt
def spectrum(A,r,L):
 g1,g2=A/r,A*r
 c=min(g1,g2,1/g1,1/g2)
 R=isqrt((L/c).__floor__())
 out=Counter()
 for m1,m2,n1,n2 in product(range(-R,R+1),repeat=4):
  E=m1*m1/g1+m2*m2/g2+g1*n1*n1+g2*n2*n2
  if E<=L:out[(E,m1*n1+m2*n2)]+=1
 return out,R,c
def canonical_imag(t):return max(t,1/t)
vals=[F(1),F(3,2),F(2),F(3)]
models=[(A,r) for A,r in product(vals,repeat=2)]
for L in [F(2),F(4),F(6)]:
 records={}; collisions=[]; same=[]
 for A,r in models:
  s,R,c=spectrum(A,r,L)
  key=tuple(sorted([canonical_imag(A),canonical_imag(r)]))
  signature=tuple(sorted(s.items()))
  for (A0,r0,key0,sig0) in records.values():
   if key==key0 and signature!=sig0:same.append(((A,r),(A0,r0)))
   if key!=key0 and signature==sig0:collisions.append(((A,r),(A0,r0)))
  records[(A,r)]=(A,r,key,signature)
 print('L',L,'models',len(records),'different-orbit collisions',len(collisions),'same-orbit mismatches',len(same),'maxR',max(spectrum(A,r,L)[1] for A,r in models))
 assert not collisions and not same
print('PASS: exact complete energy cutoff and 16-model checks')
