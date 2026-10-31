from fractions import Fraction as F
from itertools import product
from collections import Counter
G=(F(2),F(1,3),F(3))
def energy(b,z):
 m1,m2,n1,n2=z
 a,d,c=G;det=a*c-d*d
 x=F(m1)+b*n2;y=F(m2)-b*n1
 return (c*x*x-2*d*x*y+a*y*y)/det+a*n1*n1+2*d*n1*n2+c*n2*n2
def spectrum(b,T):
 # Gershgorin: lambda_min(G)>=5/3, lambda_max(G)<=10/3.
 # E<=4 => |n|²<=12/5, |m+Bn|²<=40/3.
 # For |b|<=2/3, each |m_i|<sqrt(40/3)+2/3<5.
 return Counter(energy(b,z) for z in product(range(-5,6),repeat=4) if energy(b,z)<=T)
S=[spectrum(b,F(4)) for b in (F(0),F(1,3),F(2,3))]
for i,j in ((0,1),(0,2),(1,2)):
 dif=[e for e in S[i].keys()|S[j].keys() if S[i][e]!=S[j][e]]
 print(i,j,'first_difference',min(dif) if dif else None)
assert sum(S[0].values())==75 and sum(S[1].values())==sum(S[2].values())==73
assert all(Counter({e:n for e,n in s.items() if e<=1})==Counter({e:n for e,n in S[0].items() if e<=1}) for s in S)
assert min(e for e in S[0].keys()|S[1].keys() if S[0][e]!=S[1][e])==2
assert S[1]==S[2]
print('PASS: exact complete spectra to T=4')
