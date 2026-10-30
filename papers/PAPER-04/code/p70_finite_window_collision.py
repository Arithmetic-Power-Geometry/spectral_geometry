from fractions import Fraction as F
from itertools import product
from collections import Counter,defaultdict
from math import isqrt
V=[F(1),F(4,3),F(3,2),F(2),F(3)]
def sig(A,r,L,spin):
 g=(A/r,A*r);c=min(g[0],g[1],1/g[0],1/g[1]);R=isqrt(L//c)
 out=Counter()
 for m1,m2,n1,n2 in product(range(-R,R+1),repeat=4):
  e=m1*m1/g[0]+m2*m2/g[1]+g[0]*n1*n1+g[1]*n2*n2
  if e<=L:out[(e,m1*n1+m2*n2) if spin else e]+=1
 return tuple(sorted(out.items()))
def canon(A,r):return tuple(sorted((max(A,1/A),max(r,1/r))))
for L in [F(1,4),F(1,2),F(1),F(2),F(4)]:
 for spin in [False,True]:
  groups=defaultdict(set)
  for A,r in product(V,repeat=2):groups[sig(A,r,L,spin)].add(canon(A,r))
  collisions=[g for g in groups.values() if len(g)>1]
  print('L',L,'spin',spin,'signatures',len(groups),'cross-orbit collision groups',len(collisions),'max_orbits_per_collision',max(map(len,collisions),default=0))
  if collisions:print(' example',sorted(collisions[0]))
