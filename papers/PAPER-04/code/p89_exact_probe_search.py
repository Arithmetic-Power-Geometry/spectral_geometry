from fractions import Fraction as F
from itertools import combinations, product
from collections import defaultdict

# Restricted diagonal coordinate slice; these are coordinate-labelled data, NOT duality invariants.
params=list(product((F(1),F(2),F(3)),(F(1),F(2),F(3)),(F(0),F(1,3),F(2,3))))
probes=[((1,0),(0,0)),((0,1),(0,0)),((0,0),(1,0)),((0,0),(0,1)),((1,0),(0,1)),((0,1),(1,0)),((1,1),(1,0)),((1,0),(1,1))]
def energy(t,p):
 a,c,b=t;m,n=p
 x=F(m[0])+b*n[1];y=F(m[1])-b*n[0]
 return x*x/a+y*y/c+a*n[0]*n[0]+c*n[1]*n[1]
def signature(t,ids):return tuple(energy(t,probes[i]) for i in ids)
def classes(ids):
 d=defaultdict(list)
 for t in params:d[signature(t,ids)].append(t)
 return list(d.values())
if __name__=='__main__':
 print('backgrounds',len(params),'probes',len(probes))
 for k in range(1,len(probes)+1):
  wins=[ids for ids in combinations(range(len(probes)),k) if len(classes(ids))==len(params)]
  print('k',k,'injective_subsets',len(wins),'example',wins[0] if wins else None)
  if wins:
   assert all(len(classes(ids))<len(params) for j in range(1,k) for ids in combinations(range(len(probes)),j))
   print('minimum',k,'witness',wins[0]);break
 print('full signature classes',len(classes(tuple(range(len(probes))))))
