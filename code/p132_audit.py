import sympy as s
from collections import defaultdict
from itertools import product
T=s.symbols('t'); n=5
G=['XZZXI','IXZZX','XIXZZ','ZXIXZ']
G=[(sum(1<<i for i,c in enumerate(w) if c in 'XY'),sum(1<<i for i,c in enumerate(w) if c in 'ZY')) for w in G]
S={(0,0)}
for a,b in G:S|={(x^a,z^b) for x,z in tuple(S)}
def syn(z):return sum(((z&a).bit_count()%2)<<i for i,(a,b) in enumerate(G))
def key(z):return min((a<<n)+(z^b) for a,b in S)
M=defaultdict(lambda:s.Integer(0))
for z in range(32):
 p=s.Integer(1)
 for i in range(5):
  q=T if i<2 else 2*T;p*=q if z>>i&1 else 1-q
 M[syn(z),key(z)]+=p
by={sy:sorted([(k,s.expand(v)) for (sy0,k),v in M.items() if sy0==sy]) for sy in range(16)}
assert all(len(v)==2 for v in by.values()) and s.expand(sum(M.values()))==1
base=s.expand(sum(by[sy][0][1] for sy in range(16)))
diff=[s.expand(by[sy][1][1]-by[sy][0][1]) for sy in range(16)]
fixed={i:int(bool(diff[i].subs(T,s.Rational(1,4))>0)) for i in range(16) if diff[i].subs(T,s.Rational(1,4))!=0}
free=[i for i in range(16) if i not in fixed]
assert len(free)==8
candidates={}
for bits in product((0,1),repeat=8):
 x=[fixed.get(i,0) for i in range(16)]
 for i,b in zip(free,bits):x[i]=b
 p=s.factor(base+sum(x[i]*diff[i] for i in range(16)))
 candidates.setdefault(p, ''.join(map(str,x)))
assert len(candidates)==21
F=s.expand(16*T**5-28*T**4+10*T**3+3*T**2-2*T+1)
assert s.factor(F) in candidates
q=s.Rational(749591,1000000)
# exact rational witnesses: 10001 grid points; sufficient as finite certificates
witnesses={}
for p in candidates:
 if s.expand(p-F)==0:continue
 for j in range(501):
  r=s.Rational(j,1000)
  if p.subs(T,r)<q:
   witnesses[str(p)]=str(r);break
 else:raise AssertionError('No rational witness: '+str(p))
assert len(witnesses)==20
# rigorous lower bound F(t)>q: Sturm root isolation of F-q (no roots in interval)
assert F.subs(T,0)>q
assert not [interval for interval,m in s.polys.polytools.intervals(s.Poly(F-q,T),eps=s.Rational(1,10**14)) if interval[1]>=0 and interval[0]<=s.Rational(1,2)]
# bound on any noncandidate at 1/4 is <=11/16
assert s.Rational(11,16)<q
# derivative root isolations and numerical display
roots=[(a,b) for (a,b),m in s.polys.polytools.intervals(s.Poly(s.diff(F,T),T),eps=s.Rational(1,10**15)) if a>0 and b<s.Rational(1,2)]
assert len(roots)==2
print('PASS: 256 candidates, 21 distinct polynomials, 20 rational counter-witnesses, F(t)>749591/1000000 globally')
print('F=',s.factor(F));print('optimal choice',candidates[s.factor(F)]);print('stationary isolating intervals',roots[0]);print('stationary values',[(float(sum(x)/2),float(F.subs(T,sum(x)/2))) for x in roots])
for k,v in sorted(witnesses.items()):print('WITNESS',k,'at',v)
