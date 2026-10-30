from collections import deque
from itertools import permutations,product
A='01 02 03 12 23 14 24 34 45 46 05 13 15'.split()
B='01 02 03 12 23 14 24 34 45 46 56'.split()
def encode(edges):
 return sum(1<<(min(map(int,e))*7+max(map(int,e))) for e in edges)
def lc(s,v):
 ns=[i for i in range(7) if i!=v and (s>>(min(i,v)*7+max(i,v)))&1]
 for k,i in enumerate(ns):
  for j in ns[k+1:]:s^=1<<(min(i,j)*7+max(i,j))
 return s
def orbit(start):
 q=deque([start]);seen={start:()}
 while q:
  s=q.popleft()
  for v in range(7):
   t=lc(s,v)
   if t not in seen:seen[t]=seen[s]+(v,);q.append(t)
 return seen
def canon(s):
 rr=[sum(1<<j for j in range(7) if i!=j and (s>>(min(i,j)*7+max(i,j)))&1) for i in range(7)]
 deg=[r.bit_count() for r in rr]
 groups=[tuple(i for i in range(7) if deg[i]==d) for d in sorted(set(deg))]
 best=None;bestp=None
 for gp in product(*(permutations(g) for g in groups)):
  p=sum((list(g) for g in gp),[]);t=0
  for i in range(7):
   for j in range(i+1,7):
    if rr[p[i]]>>p[j]&1:t|=1<<(i*7+j)
  if best is None or t<best:best,bestp=t,p
 return best,bestp
if __name__=='__main__':
 oa=orbit(encode(A));ob=orbit(encode(B))
 assert len(oa)==len(ob)==224 and not (oa.keys()&ob.keys())
 ca={canon(s)[0] for s in oa};cb={canon(s)[0] for s in ob}
 assert ca==cb and len(ca)==66
 lookup={canon(s)[0]:s for s in oa}
 for s in ob:
  key,pb=canon(s)
  if key in lookup:
   t=lookup[key];_,pa=canon(t)
   print('A local complements',oa[t],'B local complements',ob[s])
   print('A canonical vertex order',pa,'B canonical vertex order',pb)
   break
 print('PASS 224 labelled LC states each, 66 common unlabeled LC classes')
