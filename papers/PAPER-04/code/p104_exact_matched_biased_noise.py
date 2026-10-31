"""P104 exact matched [[5,1,3]] comparison under biased Pauli noise."""
from fractions import Fraction as F
from collections import defaultdict
G=['XZZXI','IXZZX','XIXZZ','ZXIXZ']
H=[''.join({'X':'Z','Z':'X','Y':'Y','I':'I'}[c] if i==0 else c for i,c in enumerate(s)) for s in G]
def enc(s):
 return sum((c in 'XY')<<i for i,c in enumerate(s)),sum((c in 'ZY')<<i for i,c in enumerate(s))
def sym(a,b):return ((a[0]&b[1]).bit_count()+(a[1]&b[0]).bit_count())%2
def run(strings,p):
 g=list(map(enc,strings));S={(0,0)}
 for x,z in g:S|={(a^x,b^z) for a,b in tuple(S)}
 assert len(S)==16
 hist={w:sum(((x|z).bit_count()==w) for x,z in S) for w in range(6)}
 norm=[(x,z) for x in range(32) for z in range(32) if all(sym((x,z),v)==0 for v in g)]
 d=min((x|z).bit_count() for x,z in norm if (x,z) not in S)
 buckets=defaultdict(lambda:defaultdict(F))
 for x in range(32):
  for z in range(32):
   sy=sum(sym((x,z),v)<<i for i,v in enumerate(g))
   key=min(((x^a)<<5)|(z^b) for a,b in S)
   mass=F(1)
   for i in range(5):mass*=p[((x>>i)&1,(z>>i)&1)]
   buckets[sy][key]+=mass
 return hist,d,sum(max(v.values()) for v in buckets.values())
if __name__=='__main__':
 p={(0,0):F(90,100),(1,0):F(1,100),(0,1):F(8,100),(1,1):F(1,100)}
 a=run(G,p);b=run(H,p)
 assert a[:2]==b[:2] and a[1]==3
 assert a[2]==F(91983723,100000000)
 assert b[2]==F(460218397,500000000)
 assert b[2]-a[2]==F(149891,250000000)
 print('A:',a,'B:',b,'B-A:',b[2]-a[2])
 print('PASS: exact rational matched-code operational counterexample')
