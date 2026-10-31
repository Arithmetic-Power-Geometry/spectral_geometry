"""P105 exact 32 Hadamard-orientation quantum-code audit; Python stdlib only."""
from fractions import Fraction as F
from collections import defaultdict
G=['XZZXI','IXZZX','XIXZZ','ZXIXZ']
def enc(s):
 return sum((c in 'XY')<<i for i,c in enumerate(s)),sum((c in 'ZY')<<i for i,c in enumerate(s))
def sym(a,b):return ((a[0]&b[1]).bit_count()+(a[1]&b[0]).bit_count())%2
def calc(mask,prob):
 strings=[''.join(({'X':'Z','Z':'X','Y':'Y','I':'I'}[c] if (mask>>i)&1 else c) for i,c in enumerate(s)) for s in G]
 g=list(map(enc,strings));S={(0,0)}
 for x,z in g:S|={(a^x,b^z) for a,b in tuple(S)}
 assert len(S)==16
 hist=tuple(sum((x|z).bit_count()==w for x,z in S) for w in range(6))
 norm=[(x,z) for x in range(32) for z in range(32) if all(sym((x,z),v)==0 for v in g)]
 d=min((x|z).bit_count() for x,z in norm if (x,z) not in S)
 buckets=defaultdict(lambda:defaultdict(F))
 for x in range(32):
  for z in range(32):
   sy=sum(sym((x,z),v)<<i for i,v in enumerate(g))
   key=min(((x^a)<<5)|(z^b) for a,b in S)
   mass=F(1)
   for i in range(5):mass*=prob[((x>>i)&1,(z>>i)&1)]
   buckets[sy][key]+=mass
 return hist,d,sum(max(v.values()) for v in buckets.values())
if __name__=='__main__':
 biased={(0,0):F(90,100),(1,0):F(1,100),(0,1):F(8,100),(1,1):F(1,100)}
 dep={(0,0):F(9,10),(1,0):F(1,30),(0,1):F(1,30),(1,1):F(1,30)}
 results=[calc(m,biased) for m in range(32)]
 deps=[calc(m,dep) for m in range(32)]
 assert len(set(x[0] for x in results))==1 and set(x[1] for x in results)=={3}
 assert len(set(x[2] for x in deps))==1
 assert results[0][2]==F(91983723,100000000)
 assert results[1][2]==F(460218397,500000000)
 assert len(set(x[2] for x in results))==3
 print('hist',results[0][0],'distance',results[0][1])
 print('depolarizing',deps[0][2])
 print('biased distinct',len(set(x[2] for x in results)))
 print('minimum',min((r[2],i) for i,r in enumerate(results)))
 print('maximum',max((r[2],i) for i,r in enumerate(results)))
 print('original',results[0][2],'first_h',results[1][2])
 print('PASS 32 exact rational orientations')
