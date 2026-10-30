from collections import Counter
from itertools import product
from p19_published_pair import B1,B2
I=(0,0);Y=(1,1);X=(1,0);Z=(0,1)
classes=[[(I,I)],[(I,Y)],[(Y,I)],[(Y,Y)],[(I,X),(I,Z)],[(X,I),(Z,I)],[(X,X),(Z,Z)],[(Y,X),(Y,Z)],[(X,Y),(Z,Y)],[(X,Z),(Z,X)]]
type_index={pair:j for j,cl in enumerate(classes) for pair in cl}
assert len(type_index)==16
def code(rows):
 n=len(rows);out=[]
 for a in product((0,1),repeat=n):
  z=[sum(a[i]*int(rows[i][j]) for i in range(n))%2 for j in range(n)]
  out.append(tuple(zip(a,z)))
 return out
def genus2(C):
 n=len(C[0])
 return Counter(tuple(sum(type_index[(u[i],v[i])]==j for i in range(n)) for j in range(10)) for u in C for v in C)
def genus1(C):
 types={I:0,Y:1,X:2,Z:2}
 return Counter(tuple(sum(types[s]==j for s in c) for j in range(3)) for c in C)
# Eq. (3.48), left/right refined genus-one variables.
fac=[(0,0),(0,1),(1,0),(1,1),(0,2),(2,0),(2,2),(1,2),(2,1),(2,2)]
def factor(W):
 out=Counter()
 for exp,v in W.items():
  a=tuple(sum(exp[j] for j,(l,r) in enumerate(fac) if l==i) for i in range(3))
  b=tuple(sum(exp[j] for j,(l,r) in enumerate(fac) if r==i) for i in range(3))
  out[(a,b)]+=v
 return out
C1,C2=code(B1),code(B2)
G1,G2=genus1(C1),genus1(C2)
W1,W2=genus2(C1),genus2(C2)
assert G1==G2 and len(W1)==len(W2)==1251
difference=[k for k in W1.keys()|W2.keys() if W1[k]!=W2[k]]
assert len(difference)==756
target=Counter({(a,b):v*w for a,v in G1.items() for b,w in G1.items()})
assert factor(W1)==factor(W2)==target
assert sum(W1.values())==sum(W2.values())==16384
k=min(difference)
assert k==(0,0,0,0,0,0,1,0,2,4) and (W1[k],W2[k])==(14,4)
print('PASS: genus-one equality; 1251 terms each; 756 differences')
print('PASS: both published Eq. (3.48) separating factorizations')
print('First difference:',k,W1[k],W2[k])
