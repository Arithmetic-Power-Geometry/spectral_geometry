from collections import deque
from itertools import permutations,product
A='01 02 03 12 23 14 24 34 45 46 05 13 15'.split()
B='01 02 03 12 23 14 24 34 45 46 56'.split()
def enc(edges):return sum(1<<(int(e[0])*7+int(e[1])) for e in edges)
def lc(s,v):
 ns=[i for i in range(7) if i!=v and s>>(min(i,v)*7+max(i,v))&1]
 for k,i in enumerate(ns):
  for j in ns[k+1:]:s^=1<<(min(i,j)*7+max(i,j))
 return s
def edges(s):return [(i,j) for i in range(7) for j in range(i+1,7) if s>>(i*7+j)&1]
def orbit(s):
 seen={s:()};q=deque([s])
 while q:
  a=q.popleft()
  for i,j in edges(a):
   b=lc(lc(lc(a,i),j),i)
   if b not in seen:seen[b]=seen[a]+((i,j),);q.append(b)
 return seen
def canonical(s):
 rr=[sum(1<<j for j in range(7) if i!=j and s>>(min(i,j)*7+max(i,j))&1) for i in range(7)]
 groups=[tuple(i for i in range(7) if rr[i].bit_count()==d) for d in sorted(set(x.bit_count() for x in rr))]
 best=None
 for gp in product(*(permutations(g) for g in groups)):
  p=sum((list(g) for g in gp),[]);t=0
  for i in range(7):
   for j in range(i+1,7):
    if rr[p[i]]>>p[j]&1:t|=1<<(i*7+j)
  if best is None or t<best:best=t
 return best
if __name__=='__main__':
 a=orbit(enc(A));b=orbit(enc(B));ca={canonical(s) for s in a};cb={canonical(s) for s in b}
 assert (len(a),len(b),len(a.keys()&b.keys()))==(15,15,0)
 assert (len(ca),len(cb),len(ca&cb))==(9,10,0)
 print('PASS: ELC labelled orbits 15 and 15; 9 and 10 unlabeled classes; no intersection')
