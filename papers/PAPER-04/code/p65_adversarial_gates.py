from itertools import product
from collections import Counter
A='01 02 03 12 23 14 24 34 45 46 05 13 15'.split()
B='01 02 03 12 23 14 24 34 45 46 56'.split()
classes=[[(0,0)],[(0,3)],[(3,0)],[(3,3)],[(0,1),(0,2)],[(1,0),(2,0)],[(1,1),(2,2)],[(3,1),(3,2)],[(1,3),(2,3)],[(1,2),(2,1)]]
hkm={p:i for i,g in enumerate(classes) for p in g}
def poly(edges):
 adj=[0]*7
 for e in edges:
  i,j=map(int,e);adj[i]^=1<<j;adj[j]^=1<<i
 ws=[tuple(((x>>i)&1)+2*((adj[i]&x).bit_count()%2) for i in range(7)) for x in range(128)]
 coarse=Counter(tuple(sum({0:0,1:1,2:1,3:2}[v]==k for v in w) for k in range(3)) for w in ws)
 two=Counter(tuple(sum(hkm[p]==i for p in zip(u,v)) for i in range(10)) for u in ws for v in ws)
 return coarse,two
a,aa=poly(A);b,bb=poly(B)
assert a==b and aa!=bb
assert sum(aa[e]!=bb[e] for e in aa.keys()|bb.keys())==756
print('C1 rejected: same genus-one polynomial, different genus-two polynomial')
n=7;weights=[(n+1)**i for i in range(10)]
for obj in (aa,bb):
 assert len({sum(v*w for v,w in zip(e,weights)) for e in obj})==len(obj)
print('C2 algebraic finite-degree recovery is standard Kronecker encoding, not physical theta measurement')
assert sum(aa.values())==sum(bb.values())==4**n
print('C3 infinite-family minimal physical genus remains OPEN')
print('P65 PASS')
