"""P109: exact directional one-site decoder stability certificates (stdlib)."""
from fractions import Fraction as F
from collections import defaultdict
G=['XZZXI','IXZZX','XIXZZ','ZXIXZ']
def enc(s):return sum((c in 'XY')<<i for i,c in enumerate(s)),sum((c in 'ZY')<<i for i,c in enumerate(s))
def sym(a,b):return ((a[0]&b[1]).bit_count()+(a[1]&b[0]).bit_count())%2
def run(mask):
 strings=[''.join(({'X':'Z','Z':'X','Y':'Y','I':'I'}[c] if mask>>i&1 else c) for i,c in enumerate(s)) for s in G]
 g=list(map(enc,strings));S={(0,0)}
 for x,z in g:S|={(a^x,b^z) for a,b in tuple(S)}
 p={(0,0):F(90,100),(1,0):F(1,100),(0,1):F(8,100),(1,1):F(1,100)}
 mass=defaultdict(lambda:defaultdict(F))
 site=defaultdict(lambda:[[F(0) for _ in range(4)] for _ in range(5)])
 for x in range(32):
  for z in range(32):
   sy=sum(sym((x,z),v)<<i for i,v in enumerate(g))
   coset=min(((x^a)<<5)|(z^b) for a,b in S)
   prob=F(1)
   for i in range(5):prob*=p[(x>>i&1,z>>i&1)]
   mass[sy][coset]+=prob
   for i in range(5):site[(sy,coset)][i][(x>>i&1)+2*(z>>i&1)]+=prob
 gamma=min(sorted(cs.values(),reverse=True)[0]-sorted(cs.values(),reverse=True)[1] for cs in mass.values())
 thresholds=[]
 for i in range(5):
  candidates=[]
  for sy,cs in mass.items():
   win=max(cs,key=cs.get)
   for c in cs:
    if c==win:continue
    gap=cs[win]-cs[c]
    def slope(key):
     m=site[(sy,key)][i]
     return m[2]/p[(0,1)]-m[0]/p[(0,0)]
    b=slope(win)-slope(c)
    if b<0:candidates.append(gap/(-b))
  thresholds.append(min(candidates) if candidates else None)
 return gamma,thresholds
if __name__=='__main__':
 expected={0:F(30653,1041300),1:F(4249,208260),28:F(7097,18300)}
 for mask in (0,1,28):
  gamma,t=run(mask)
  assert t[0]==expected[mask]
  print('mask',mask,'gamma',gamma,'P107_radius',gamma/10,'one_site_thresholds',t,'ratio',float(t[0]/(gamma/10)))
 print('PASS: all exact rational directional thresholds')
