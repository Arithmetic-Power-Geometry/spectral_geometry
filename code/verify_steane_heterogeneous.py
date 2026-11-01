import sympy as s,json
from pathlib import Path
from itertools import product
T=s.symbols('t');n=7;checks=[int(x[::-1],2) for x in ('1111000','1100110','1010101')];S={0}
for a in checks:S|={x^a for x in tuple(S)}
def syn(z):return sum(((z&a).bit_count()%2)<<i for i,a in enumerate(checks))
def key(z):return min(z^a for a in S)
M={}
for z in range(128):
 p=s.prod((T*(2 if i>=4 else 1) if z>>i&1 else 1-T*(2 if i>=4 else 1)) for i in range(7))
 h=(syn(z),key(z));M[h]=M.get(h,0)+p
by=[[s.expand(M[(sy,co)]) for co in sorted(co for (ss,co) in M if ss==sy)] for sy in range(8)]
assert all(len(v)==2 for v in by)
assert sum(max(v[0].subs(T,s.Rational(1,4)),v[1].subs(T,s.Rational(1,4))) for v in by)==s.Rational(1,2)
base=s.expand(sum(v[0] for v in by));diff=[s.expand(v[1]-v[0]) for v in by]
polys={}
for bits in product((0,1),repeat=8):
 p=s.factor(base+sum(bit*diff[i] for i,bit in enumerate(bits)))
 polys.setdefault(str(p),''.join(map(str,bits)))
threshold=s.Rational(4999,10000)
witness=[]
for poly,bits in polys.items():
 p=s.sympify(poly)
 w=next(((j,s.factor(p.subs(T,s.Rational(j,1000)))) for j in range(501) if p.subs(T,s.Rational(j,1000))<threshold),None)
 if w is None: print('FAIL',bits,poly);raise SystemExit(1)
 witness.append({'polynomial':poly,'bits':bits,'t':f'{w[0]}/1000','value':str(w[1])})
print('PASS',len(polys),'distinct of 256, each <',threshold,'at a rational witness; Rrand=RML=1/2, strict gap.')
print('maximum witness value',max(s.Rational(w['value']) for w in witness))
json.dump({'family':'Steane seven-qubit (t,t,t,t,2t,2t,2t), t in [0,1/2]','threshold':str(threshold),'unique_polynomials':len(polys),'witnesses':witness},open(Path(__file__).resolve().parents[1] / 'evidence/steane_heterogeneous_witnesses.json','w'),indent=2)
