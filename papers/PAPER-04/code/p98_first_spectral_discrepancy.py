"""P98 exact first spectral difference; complete energy-cutoff enumeration."""
from fractions import Fraction as F
from itertools import product
from collections import Counter
G=(F(2),F(1,3),F(3))
def energy(b,z):
 m1,m2,n1,n2=z
 a,d,c=G; det=a*c-d*d
 x=m1+b*n2; y=m2-b*n1
 return (c*x*x-2*d*x*y+a*y*y)/det+a*n1*n1+2*d*n1*n2+c*n2*n2
def spectrum(b,T):
 # G eigenvalues in [5/3,10/3] by Gershgorin; E<=4 => |n_i|<=1,
 # |m_i|<sqrt(40/3)+2/3<5 for b in [0,2/3].
 out=Counter(); witnesses={}
 for z in product(range(-5,6),repeat=4):
  e=energy(b,z)
  if e<=T:
   out[e]+=1
   witnesses.setdefault(e,[]).append(z)
 return out,witnesses
if __name__=='__main__':
 S={b:spectrum(b,F(4)) for b in (F(0),F(1,3),F(2,3))}
 A=S[F(0)][0]; B=S[F(1,3)][0]
 first=min(e for e in A.keys()|B.keys() if A[e]!=B[e])
 assert first==2 and A[first]==2 and B[first]==0
 assert S[F(0)][1][first]==[(0,0,-1,0),(0,0,1,0)]
 assert S[F(1,3)][0]==S[F(2,3)][0]
 assert [sum(S[b][0].values()) for b in (F(0),F(1,3),F(2,3))]==[75,73,73]
 print('first difference:',first,'multiplicity b=0:',A[first],'b=1/3:',B[first])
 print('common levels below 2:',[(str(e),A[e]) for e in sorted(A.keys()|B.keys()) if e<2])
 print('state counts:',[sum(S[b][0].values()) for b in (F(0),F(1,3),F(2,3))])
 print('PASS')
