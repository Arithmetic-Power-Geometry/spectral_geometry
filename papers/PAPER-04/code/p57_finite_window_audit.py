from fractions import Fraction as Q
from itertools import product
from collections import Counter
def energy(m1,m2,n1,n2,b):
 x=Q(m1)+b*n2;y=Q(m2)-b*n1
 return (27*x*x-6*x*y+18*y*y)/53+2*n1*n1+Q(2,3)*n1*n2+3*n2*n2
def spectrum(b,K=5,cap=Q(3)):
 out=Counter()
 for m1,m2,n1,n2 in product(range(-K,K+1),repeat=4):
  e=energy(m1,m2,n1,n2,b)
  if e<=cap:out[e,m1*n1+m2*n2]+=1
 return out
def count_window(sp,lo,hi,spin):
 return sum(v for (e,s),v in sp.items() if lo<=e<=hi and s==spin)
for b in [Q(0),Q(1,10),Q(1,5),Q(-1,5)]:
 sp=spectrum(b)
 print(b,sum(sp.values()),count_window(sp,Q(2),Q(201,100),0))
assert energy(0,0,1,0,Q(1,10))==Q(5309,2650)
assert energy(0,0,1,0,Q(1,5))==Q(2668,1325)
print('PASS')
