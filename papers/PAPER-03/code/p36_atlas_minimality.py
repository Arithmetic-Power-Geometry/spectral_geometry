import networkx as nx
from collections import Counter,defaultdict
I=(0,0);Y=(1,1);X=(1,0);Z=(0,1)
classes=[[(I,I)],[(I,Y)],[(Y,I)],[(Y,Y)],[(I,X),(I,Z)],[(X,I),(X,Z)],[(X,X),(Z,Z)],[(Y,X),(Y,Z)],[(X,Y),(Z,Y)],[(X,Z),(Z,X)]]
# Correct Eq. (3.47) classes: the sixth group is (X,I),(Z,I).
classes[5]=[(X,I),(Z,I)]
idx={p:j for j,cl in enumerate(classes) for p in cl}
assert len(idx)==16
type1={I:0,Y:1,X:2,Z:2}
def fingerprint(g):
 n=len(g);adj=[sum(1<<j for j in g.neighbors(i)) for i in range(n)]
 C=[]
 for a in range(1<<n):
  z=sum(((adj[j]&a).bit_count()%2)<<j for j in range(n))
  C.append(tuple(((a>>j)&1,(z>>j)&1) for j in range(n)))
 W1=Counter(tuple(sum(type1[t]==k for t in c) for k in range(3)) for c in C)
 W2=Counter(tuple(sum(idx[(u[j],v[j])]==k for j in range(n)) for k in range(10)) for u in C for v in C)
 return tuple(sorted(W1.items())),tuple(sorted(W2.items()))
for n,expected in [(5,(34,21,0)),(6,(156,64,0))]:
 gs=[g for g in nx.graph_atlas_g() if len(g)==n]
 groups=defaultdict(set)
 for g in gs:
  a,b=fingerprint(g);groups[a].add(b)
 splits=sum(len(v)>1 for v in groups.values())
 print(n,len(gs),len(groups),splits)
 assert (len(gs),len(groups),splits)==expected
print('PASS: no genus-one fingerprint class splits at genus two for n=5,6')
