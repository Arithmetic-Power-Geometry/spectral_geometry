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
def words(a):return [tuple(((x>>i)&1)+2*((a[i]&x).bit_count()%2) for i in range(7)) for x in range(128)]
def one(w):
 c=Counter()
 for u in w:
  n=[0]*3
  for v in u:n[{0:0,3:1,1:2,2:2}[v]]+=1
  c[tuple(n)]+=1
 return c
def two(w):
 c=Counter()
 for u in w:
  for v in w:
   n=[0]*10
   for p in zip(u,v):n[hkm[p]]+=1
   c[tuple(n)]+=1
 return c
# HKM eq 3.48; y8=x2*x1', y9=x2*x2'
map_y=[(0,0),(0,1),(1,0),(1,1),(0,2),(2,0),(2,2),(1,2),(2,1),(2,2)]
def factorize(poly):
 result=Counter()
 for exponent,coeff in poly.items():
  e=[0]*6
  for j,p in enumerate(exponent):
   a,b=map_y[j];e[a]+=p;e[3+b]+=p
  result[tuple(e)]+=coeff
 return result
def product(w):
 c=Counter()
 for u,cu in w.items():
  for v,cv in w.items():c[u+v]+=cu*cv
 return c
if __name__=='__main__':
 for name,edges in [('A',A),('B',B)]:
  w=words(adj(edges));c1=one(w);c2=two(w)
  assert factorize(c2)==product(c1)
  print(name,'genus1 terms',len(c1),'genus2 terms',len(c2),'factorization PASS')
