from fractions import Fraction as F
from collections import Counter
from itertools import product
def spec(b):
 c=Counter()
 for m1,m2,n1,n2 in product(range(-5,6),repeat=4):
  x=F(m1)+b*n2;y=F(m2)-b*n1
  E=(27*x*x-6*x*y+18*y*y)/53+2*n1*n1+F(2,3)*n1*n2+3*n2*n2
  if E<=3:c[E,m1*n1+m2*n2]+=1
 return c
p=spec(F(1,5));q=spec(F(-1,5));shift=spec(F(6,5));zero=spec(F(0))
assert p==shift
assert all(p[E,s]==q[E,-s] for E,s in set(p)|set(q))
first=min(E for E,s in set(p)|set(q) if p[E,s]!=q[E,s])
assert first==F(3313,1325)
assert p[first,-1]==2 and q[first,-1]==0
print('first',first,'spin -1',p[first,-1],q[first,-1])
print('shift invariant',p==shift,'parity',True)
print('E<=3 counts',sum(p.values()),sum(q.values()),sum(zero.values()))
