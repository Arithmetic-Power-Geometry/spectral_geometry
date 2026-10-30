from collections import Counter
from itertools import product
A='01 02 03 12 23 14 24 34 45 46 05 13 15'.split()
B='01 02 03 12 23 14 24 34 45 46 56'.split()
def words(edges):
 adj=[0]*7
 for e in edges:
  i,j=map(int,e);adj[i]^=1<<j;adj[j]^=1<<i
 return [tuple(((x>>i)&1)+2*((adj[i]&x).bit_count()%2) for i in range(7)) for x in range(128)]
classes=[[(0,0)],[(0,3)],[(3,0)],[(3,3)],[(0,1),(0,2)],[(1,0),(2,0)],[(1,1),(2,2)],[(3,1),(3,2)],[(1,3),(2,3)],[(1,2),(2,1)]]
hkm={p:i for i,g in enumerate(classes) for p in g}
copy={p:tuple(sorted(p)) for p in product(range(4),repeat=2)}
def calc(edges):
 ws=words(edges);coarse=Counter();full=Counter();ten=Counter();exch=Counter()
 for w in ws:
  coarse[tuple(sum({0:0,1:1,2:1,3:2}[v]==k for v in w) for k in range(3))]+=1
 for u in ws:
  for v in ws:
   pairs=list(zip(u,v))
   full[tuple(pairs.count(p) for p in product(range(4),repeat=2))]+=1
   ten[tuple(sum(hkm[p]==i for p in pairs) for i in range(10))]+=1
   exch[tuple(sum(copy[p]==g for p in pairs) for g in sorted(set(copy.values())))]+=1
 return coarse,full,ten,exch
x=calc(A);y=calc(B)
for i,name in enumerate(['coarse','full16','HKM10','copy10']):
 cx,cy=x[i],y[i]
 diff=sum(cx[k]!=cy[k] for k in cx.keys()|cy.keys())
 print(name,'monomials',len(cx),len(cy),'different positions',diff,'total',sum(cx.values()),sum(cy.values()))
assert x[0]==y[0]
assert sum(x[2].values())==16384
assert (len(x[1]),len(y[1]))==(7579,5246)
assert sum(x[1][k]!=y[1][k] for k in x[1].keys()|y[1].keys())==9448
assert (len(x[2]),len(y[2]))==(1251,1251)
assert sum(x[2][k]!=y[2][k] for k in x[2].keys()|y[2].keys())==756
assert sum(x[3][k]!=y[3][k] for k in x[3].keys()|y[3].keys())==1743
print('ALL P63 ASSERTIONS PASS')
