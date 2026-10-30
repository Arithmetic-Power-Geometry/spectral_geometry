from fractions import Fraction as Q
from collections import Counter
from itertools import product
G=((Q(2),Q(1,3)),(Q(1,3),Q(3)))
det=G[0][0]*G[1][1]-G[0][1]*G[1][0]
Gi=((G[1][1]/det,-G[0][1]/det),(-G[1][0]/det,G[0][0]/det))
def energy(m,n,b):
 x=(Q(m[0])+b*n[1],Q(m[1])-b*n[0])
 return sum(x[i]*Gi[i][j]*x[j] for i in range(2) for j in range(2))+sum(n[i]*G[i][j]*n[j] for i in range(2) for j in range(2))
def spectrum(b,K,spin=False):
 out=Counter()
 for a in product(range(-K,K+1),repeat=4):
  m,n=a[:2],a[2:];E=energy(m,n,b);s=sum(m[i]*n[i] for i in range(2))
  out[(E,s) if spin else E]+=1
 return out
for K in (1,2,3):
 a=spectrum(Q(1,3),K);b=spectrum(Q(-1,3),K)
 assert a==b
 sa=spectrum(Q(1,3),K,True);sb=spectrum(Q(-1,3),K,True)
 assert all(sa[(E,s)]==sb[(E,-s)] for E,s in sa)
 print('K',K,'charges',(2*K+1)**4,'energy_equal',a==b,'energy_spin_equal',sa==sb,'different_joint_keys',sum(sa[k]!=sb[k] for k in sa.keys()|sb.keys()))
print('PASS: exact sign-reversal obstruction; no claim of physical inequivalence')
