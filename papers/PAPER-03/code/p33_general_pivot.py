from itertools import combinations

def pivot(A,i,j):
 n=len(A); B=[r[:] for r in A]
 for a in range(n):
  for b in range(n):
   if a!=b and a not in (i,j) and b not in (i,j):
    B[a][b]=A[a][b]^(A[i][a]&A[j][b])^(A[j][a]&A[i][b])
 for a in range(n):
  if a not in (i,j):
   B[i][a]=B[a][i]=A[j][a];B[j][a]=B[a][j]=A[i][a]
 return B

def code(A):
 n=len(A); out=set()
 for k in range(1<<n):
  a=tuple((k>>i)&1 for i in range(n))
  z=tuple(sum(A[i][j]*a[j] for j in range(n))%2 for i in range(n))
  out.add((a,z))
 return out

def swap(c,i,j):
 a,z=map(list,c)
 for k in (i,j):a[k],z[k]=z[k],a[k]
 return tuple(a),tuple(z)

edges=0;graphs=0
for n in range(2,6):
 es=list(combinations(range(n),2))
 for bits in range(1<<len(es)):
  A=[[0]*n for _ in range(n)]
  for k,(i,j) in enumerate(es):A[i][j]=A[j][i]=(bits>>k)&1
  C=code(A);graphs+=1
  for i,j in es:
   if A[i][j]:
    assert {swap(c,i,j) for c in C}==code(pivot(A,i,j)),(n,bits,i,j)
    edges+=1
print('PASS',graphs,'graphs',edges,'edge pivots, n=2..5')
