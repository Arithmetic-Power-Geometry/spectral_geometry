from itertools import combinations,product
from collections import Counter,defaultdict
I=(0,0);Y=(1,1);X=(1,0);Z=(0,1)
classes=[[(I,I)],[(I,Y)],[(Y,I)],[(Y,Y)],[(I,X),(I,Z)],[(X,I),(Z,I)],[(X,X),(Z,Z)],[(Y,X),(Y,Z)],[(X,Y),(Z,Y)],[(X,Z),(Z,X)]]
idx={p:j for j,cl in enumerate(classes) for p in cl}
type1={I:0,Y:1,X:2,Z:2}
def fingerprints(A):
 n=len(A);C=[]
 for a in product((0,1),repeat=n):
  z=tuple(sum(A[i][j]*a[j] for j in range(n))%2 for i in range(n))
  C.append(tuple(zip(a,z)))
 W1=Counter(tuple(sum(type1[t]==j for t in c) for j in range(3)) for c in C)
 W2=Counter(tuple(sum(idx[(u[i],v[i])]==j for i in range(n)) for j in range(10)) for u in C for v in C)
 return tuple(sorted(W1.items())),tuple(sorted(W2.items()))
for n in range(2,5):
 es=list(combinations(range(n),2)); groups=defaultdict(set); graphs=0
 for bits in range(1<<len(es)):
  A=[[0]*n for _ in range(n)]
  for k,(i,j) in enumerate(es): A[i][j]=A[j][i]=(bits>>k)&1
  a,b=fingerprints(A);groups[a].add(b);graphs+=1
 split=sum(len(s)>1 for s in groups.values())
 print('n',n,'graphs',graphs,'genus1 fingerprints',len(groups),'genus1 classes split by genus2',split,'genus2 fingerprints',sum(map(len,groups.values())))
 assert sum(map(len,groups.values()))>=len(groups)
