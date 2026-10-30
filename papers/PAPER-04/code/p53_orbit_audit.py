from fractions import Fraction as Q
from collections import Counter
from itertools import product
def spectrum(b,H=Q(3),K=5):
 out=Counter()
 for m1,m2,n1,n2 in product(range(-K,K+1),repeat=4):
  x=Q(m1)+b*n2;y=Q(m2)-b*n1
  E=(27*x*x-6*x*y+18*y*y)/53+2*n1*n1+Q(2,3)*n1*n2+3*n2*n2
  if E<=H:out[(E,m1*n1+m2*n2)]+=1
 return out
S={str(b):spectrum(b) for b in [Q(-1,5),Q(0),Q(1,5),Q(6,5)]}
assert S['1/5']==S['6/5']
keys=sorted(set().union(*(s.keys() for s in S.values())))
worlds=['-1/5','0','1/5']
patterns={}
for k in keys:
 row=tuple(S[b][k] for b in worlds)
 if len(set(row))>1:patterns.setdefault(row,[]).append(k)
print('states',[(b,sum(s.values())) for b,s in S.items()])
print('distinguishing rows',sum(map(len,patterns.values())),'patterns',len(patterns))
for row,ks in patterns.items():print(row,len(ks),ks[0])
for a,b in [('-1/5','0'),('0','1/5'),('-1/5','1/5')]:
 dif=[k for k in keys if S[a][k]!=S[b][k]]
 print('first',a,b,dif[0])
