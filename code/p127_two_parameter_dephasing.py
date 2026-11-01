# P127 independent-site I/Z exact two-parameter test, Python 3 + SymPy
import itertools, collections, sympy as sp
n=5; gens=['XZZXI','IXZZX','XIXZZ','ZXIXZ']; t,u=sp.symbols('t u')
def masks(s):
 return (sum(1<<i for i,c in enumerate(s) if c in 'XY'),sum(1<<i for i,c in enumerate(s) if c in 'ZY'))
G=list(map(masks,gens))
S={(0,0)}
for a,b in G:S|={(x^a,z^b) for x,z in list(S)}
def syndrome(z):return sum(((z&a).bit_count()%2)<<i for i,(a,b) in enumerate(G))
def key(z):return min(((a<<n)+(z^b)) for a,b in S)
M=collections.defaultdict(lambda:sp.Integer(0))
for z in range(1<<n):
 p=sp.Integer(1)
 for i in range(n):
  v=t if i<2 else u
  p*=v if z>>i&1 else 1-v
 M[syndrome(z),key(z)]+=p
by=collections.defaultdict(list)
for (s,k),p in M.items():by[s].append((k,sp.expand(p)))
assert len(by)==16 and all(len(a)==2 for a in by.values())
rows=[]
for s,items in sorted(by.items()):
 a,b=items
 if a[1].subs({t:sp.Rational(1,10),u:sp.Rational(1,10)})<b[1].subs({t:sp.Rational(1,10),u:sp.Rational(1,10)}):a,b=b,a
 rows.append((s,a[0],b[0],sp.factor(a[1]-b[1])))
assert len({str(r[3]) for r in rows})==6
assert len({str(sp.factor(r[3].subs(u,t))) for r in rows})==3
r=next(r for r in rows if r[0]==15)
assert r[1:3]==(3,28)
assert sp.simplify(r[3].subs({t:sp.Rational(1,10),u:sp.Rational(1,10)}))==sp.Rational(81,12500)
assert sp.simplify(r[3].subs({t:sp.Rational(1,10),u:sp.Rational(1,5)}))==-sp.Rational(17,12500)
print('PASS 16 syndromes; 6 two-parameter gap expressions vs 3 shared; syndrome 1111 decoder switch')
for s,a,b,g in rows:print(format(s,'04b'),a,b,g)
