"""P132 independent exact deterministic minimax audit. Requires SymPy."""
import sympy as s
from collections import defaultdict
from itertools import product
t=s.symbols("t")
words=("XZZXI","IXZZX","XIXZZ","ZXIXZ")
G=[(sum(1<<i for i,c in enumerate(w) if c in "XY"),sum(1<<i for i,c in enumerate(w) if c in "ZY")) for w in words]
S={(0,0)}
for a,b in G:S|={(x^a,z^b) for x,z in tuple(S)}
def syndrome(z):return sum(((z&a).bit_count()%2)<<i for i,(a,b) in enumerate(G))
def coset(z):return min((a<<5)+(z^b) for a,b in S)
m=defaultdict(lambda:s.Integer(0))
for z in range(32):
 p=s.Integer(1)
 for i in range(5):
  q=t if i<2 else 2*t
  p*=q if (z>>i)&1 else 1-q
 m[syndrome(z),coset(z)]+=p
assert s.expand(sum(m.values()))==1
by={j:sorted((k,s.expand(v)) for (sy,k),v in m.items() if sy==j) for j in range(16)}
assert all(len(v)==2 for v in by.values())
base=s.expand(sum(by[j][0][1] for j in range(16)))
diff=[s.expand(by[j][1][1]-by[j][0][1]) for j in range(16)]
fixed={j:(1 if diff[j].subs(t,s.Rational(1,4))>0 else 0) for j in range(16) if diff[j].subs(t,s.Rational(1,4))!=0}
free=[j for j in range(16) if j not in fixed]
assert len(free)==8
candidates={}
for bits in product((0,1),repeat=8):
 x=[fixed.get(j,0) for j in range(16)]
 for j,b in zip(free,bits):x[j]=b
 p=s.factor(base+sum(x[j]*diff[j] for j in range(16)))
 candidates.setdefault(p,"".join(map(str,x)))
assert len(candidates)==21
F=16*t**5-28*t**4+10*t**3+3*t**2-2*t+1
assert s.factor(F) in candidates
q=s.Rational(749591,1000000)
witnesses={}
for p in candidates:
 if s.expand(p-F)==0:continue
 for j in range(501):
  r=s.Rational(j,1000)
  if p.subs(t,r)<q:
   witnesses[str(p)]=str(r)
   break
 else:raise AssertionError("No witness for "+str(p))
assert len(witnesses)==20
assert F.subs(t,0)>q
assert not [(a,b) for (a,b),mult in s.polys.polytools.intervals(s.Poly(F-q,t),eps=s.Rational(1,10**14)) if b>=0 and a<=s.Rational(1,2)]
assert s.Rational(11,16)<q
roots=[(a,b) for (a,b),mult in s.polys.polytools.intervals(s.Poly(s.diff(F,t),t),eps=s.Rational(1,10**15)) if a>0 and b<s.Rational(1,2)]
assert len(roots)==2
# Recheck the archived machine-readable witness certificate, if present.
import json
from pathlib import Path
certificate=Path(__file__).resolve().parents[1]/'evidence'/'deterministic_witnesses.json'
if certificate.exists():
 data=json.loads(certificate.read_text(encoding='utf-8'))
 assert data['competing_polynomial_count']==20
 assert data['threshold']=='749591/1000000'
 assert len(data['exclusion_witnesses'])==20
 assert {r['polynomial']:r['t'] for r in data['exclusion_witnesses']}==witnesses
 for r in data['exclusion_witnesses']:
  assert s.sympify(r['polynomial']).subs(t,s.Rational(r['t']))<q
print("PASS 256 decoders / 21 polynomials / 20 rational witnesses")
print("Optimal polynomial",F)
print("Choice",candidates[s.factor(F)])
print("Critical points",[(float((a+b)/2),float(F.subs(t,(a+b)/2))) for a,b in roots])
for p,r in sorted(witnesses.items()):print("WITNESS",p,"at",r)
