from collections import Counter
A='01 02 03 12 23 14 24 34 45 46 05 13 15'.split()
B='01 02 03 12 23 14 24 34 45 46 56'.split()
classes=[[(0,0)],[(0,3)],[(3,0)],[(3,3)],[(0,1),(0,2)],[(1,0),(2,0)],[(1,1),(2,2)],[(3,1),(3,2)],[(1,3),(2,3)],[(1,2),(2,1)]]
hkm={p:i for i,g in enumerate(classes) for p in g}
def adj(edges):
 a=[0]*7
 for e in edges:
  i,j=map(int,e);a[i]^=1<<j;a[j]^=1<<i
 return a
def lc(a,v):
 b=a.copy();ns=[i for i in range(7) if a[v]>>i&1]
 for i in ns:
  for j in ns:
   if i!=j:b[i]^=1<<j
 return b
def words(a):
 return [tuple(((x>>i)&1)+2*((a[i]&x).bit_count()%2) for i in range(7)) for x in range(128)]
def invariants(a):
 w=words(a);coarse=Counter();ten=Counter()
 for u in w:
  coarse[tuple(sum({0:0,1:1,2:1,3:2}[v]==k for v in u) for k in range(3))]+=1
 for u in w:
  for v in w:
   counts=[0]*10
   for p in zip(u,v):counts[hkm[p]]+=1
   ten[tuple(counts)]+=1
 return coarse,ten
if __name__=='__main__':
 ca,ta=invariants(adj(A));cb,tb=invariants(adj(B))
 assert ca==cb and sum(ta[k]!=tb[k] for k in ta.keys()|tb.keys())==756
 for label,edges in [('A',A),('B',B)]:
  a=adj(edges);c,t=invariants(a)
  for v in range(7):
   cc,tt=invariants(lc(a,v))
   print(label,v,'coarse_equal',c==cc,'HKM10_equal',t==tt,'HKM10_diff',sum(t[k]!=tt[k] for k in t.keys()|tt.keys()))
 for v in (4,5):
  c,t=invariants(lc(adj(A),v))
  assert c==cb and t==tb
 print('PASS: LC at A vertices 4 or 5 matches both B enumerators exactly; HKM10 not LC invariant')
