"""P101: exact HKM eq (4.19) graph pair, binary symplectic tests."""
from collections import Counter
A=[[0,1,0,0,0,1,0],[1,0,1,0,0,0,1],[0,1,0,1,1,1,1],[0,0,1,0,1,0,0],[0,0,1,1,0,0,0],[1,0,1,0,0,0,1],[0,1,1,0,0,1,0]]
B=[[0,1,0,0,0,1,1],[1,0,1,0,0,0,1],[0,1,0,1,1,1,1],[0,0,1,0,1,0,0],[0,0,1,1,0,0,0],[1,0,1,0,0,0,1],[1,1,1,0,0,1,0]]
def audit(M):
 n=len(M)
 assert all(M[i][i]==0 and all(M[i][j]==M[j][i] for j in range(n)) for i in range(n))
 adj=[sum(M[i][j]<<j for j in range(n)) for i in range(n)]
 st=[]
 for x in range(1<<n):
  z=0
  for i in range(n):
   if x>>i&1:z^=adj[i]
  st.append((x,z))
 hist=Counter((x|z).bit_count() for x,z in st)
 return hist,st
def pair_hist(st):
 return Counter(((x|z).bit_count(),(u|v).bit_count(),((x^u)|(z^v)).bit_count()) for x,z in st for u,v in st)
if __name__=='__main__':
 h1,s1=audit(A);h2,s2=audit(B)
 print('A',sorted(h1.items()));print('B',sorted(h2.items()))
 assert h1==h2
 assert sum(h1.values())==128
 p1=pair_hist(s1);p2=pair_hist(s2)
 print('pair histogram equal:',p1==p2,'ordered pairs per graph:',len(s1)**2)
 assert p1==p2
 print('PASS; no operational advantage established')
