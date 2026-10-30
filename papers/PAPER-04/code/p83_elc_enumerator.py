from collections import Counter,deque
A='01 02 03 12 23 14 24 34 45 46 05 13 15'.split(); B='01 02 03 12 23 14 24 34 45 46 56'.split()
classes=[[(0,0)],[(0,3)],[(3,0)],[(3,3)],[(0,1),(0,2)],[(1,0),(2,0)],[(1,1),(2,2)],[(3,1),(3,2)],[(1,3),(2,3)],[(1,2),(2,1)]]
hkm={p:i for i,g in enumerate(classes) for p in g}
def adj(edges):
 a=[0]*7
 for e in edges:
  i,j=map(int,e);a[i]^=1<<j;a[j]^=1<<i
 return tuple(a)
def lc(a,v):
 b=list(a);ns=[i for i in range(7) if a[v]>>i&1]
 for i in ns:
  for j in ns:
   if i!=j:b[i]^=1<<j
 return tuple(b)
def orbit(a):
 seen={a};q=deque([a])
 while q:
  x=q.popleft()
  for i in range(7):
   for j in range(i+1,7):
    if x[i]>>j&1:
     y=lc(lc(lc(x,i),j),i)
     if y not in seen:seen.add(y);q.append(y)
 return seen
def inv(a):
 ws=[tuple(((x>>i)&1)+2*((a[i]&x).bit_count()%2) for i in range(7)) for x in range(128)]
 coarse=Counter(tuple(sum({0:0,1:1,2:1,3:2}[v]==k for v in w) for k in range(3)) for w in ws)
 ten=Counter()
 for u in ws:
  for v in ws:
   cc=[0]*10
   for p in zip(u,v):cc[hkm[p]]+=1
   ten[tuple(cc)]+=1
 return coarse,ten
if __name__=='__main__':
 for name,e in [('A',A),('B',B)]:
  oo=orbit(adj(e)); spectra=[inv(a) for a in oo]
  base=inv(adj(e));coarse_d=sum(x[0]!=base[0] for x in spectra);ten_d=sum(x[1]!=base[1] for x in spectra)
  print(name,'orbit',len(oo),'coarse_changes',coarse_d,'HKM10_changes',ten_d,'unique coarse',len({frozenset(x[0].items()) for x in spectra}),'unique HKM10',len({frozenset(x[1].items()) for x in spectra}))
  assert len(oo)==15 and coarse_d==ten_d==0
