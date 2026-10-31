"""P107 exact TV robustness margins for [[5,1,3]] code local-Hadamard orientations."""
from fractions import Fraction as F
from collections import defaultdict
G=['XZZXI','IXZZX','XIXZZ','ZXIXZ']
def enc(s):return sum((c in 'XY')<<i for i,c in enumerate(s)),sum((c in 'ZY')<<i for i,c in enumerate(s))
def sym(a,b):return ((a[0]&b[1]).bit_count()+(a[1]&b[0]).bit_count())%2
def cert(mask):
 strings=[''.join(({'X':'Z','Z':'X','Y':'Y','I':'I'}[c] if (mask>>i)&1 else c) for i,c in enumerate(s)) for s in G]
 g=list(map(enc,strings));S={(0,0)}
 for x,z in g:S|={(a^x,b^z) for a,b in tuple(S)}
 p={(0,0):F(90,100),(1,0):F(1,100),(0,1):F(8,100),(1,1):F(1,100)}
 buckets=defaultdict(lambda:defaultdict(F))
 for x in range(32):
  for z in range(32):
   sy=sum(sym((x,z),v)<<i for i,v in enumerate(g))
   key=min(((x^a)<<5)|(z^b) for a,b in S)
   mass=F(1)
   for i in range(5):mass*=p[((x>>i)&1,(z>>i)&1)]
   buckets[sy][key]+=mass
 gaps=[]
 for cs in buckets.values():
  values=sorted(cs.values(),reverse=True)
  gaps.append(values[0]-values[1])
 return min(gaps),sum(max(v.values()) for v in buckets.values())
if __name__=='__main__':
 expected={0:(F(19096819,10000000000),F(91983723,100000000)),1:(F(2647127,2000000000),F(460218397,500000000)),28:(F(13781397,5000000000),F(2316216227,2500000000))}
 for mask,(margin,success) in expected.items():
  m,s=cert(mask);assert(m,s)==(margin,success) and m>0
  print('mask',mask,'success',s,'margin',m,'strict_TV_radius',m/10)
 print('PASS P107 exact robustness margins')
