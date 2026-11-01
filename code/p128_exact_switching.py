import collections
import sympy as sp
n=5
T=sp.symbols('t')
gens=['XZZXI','IXZZX','XIXZZ','ZXIXZ']
def masks(word):
 return (sum(1<<i for i,c in enumerate(word) if c in 'XY'),sum(1<<i for i,c in enumerate(word) if c in 'ZY'))
G=[masks(w) for w in gens]
S={(0,0)}
for gx,gz in G:
 S |= {(x^gx,z^gz) for x,z in tuple(S)}
def syn(z):return sum(((z&gx).bit_count()%2)<<i for i,(gx,gz) in enumerate(G))
def key(z):return min((x<<n)+(z^q) for x,q in S)
M=collections.defaultdict(lambda:sp.Integer(0))
for z in range(1<<n):
 p=sp.Integer(1)
 for i in range(n):
  v=T if i<2 else 2*T
  p*=v if z&(1<<i) else 1-v
 M[syn(z),key(z)]+=p
by=collections.defaultdict(list)
for (s,k),v in M.items():by[s].append((k,sp.expand(v)))
assert len(by)==16 and all(len(a)==2 for a in by.values())
assert sp.expand(sum(M.values()))==1
rows=[]
for syndrome in sorted(by):
 a,b=by[syndrome]
 def uniform_mass(k):
  return sum(sp.Rational(1,10)**z.bit_count()*sp.Rational(9,10)**(n-z.bit_count()) for z in range(1<<n) if syn(z)==syndrome and key(z)==k)
 if uniform_mass(a[0])<uniform_mass(b[0]):a,b=b,a
 gap=sp.factor(a[1]-b[1]); poly=sp.Poly(gap,T)
 roots=[]
 for (lo,hi),multiplicity in sp.polys.polytools.intervals(poly,eps=sp.Rational(1,10**12)):
  if hi<0 or lo>sp.Rational(1,2):continue
  if lo==hi==0 or lo==hi==sp.Rational(1,2):continue
  if lo>0 and hi<sp.Rational(1,2):roots.append((lo,hi,multiplicity))
 rows.append((syndrome,a[0],b[0],gap,roots))
assert len({str(x[3]) for x in rows})==6
assert sum(len(x[4]) for x in rows)==13
assert [x[0] for x in rows if not x[4]]==[6,11,13]
assert len(rows[-1][4])==1
print('PASS: 16 syndromes, 6 distinct gap polynomials, 13 interior switching roots across 13 syndromes')
for s,a,b,g,roots in rows:
 print(f'{s:04b} {a:2d} {b:2d} gap={g} roots='+','.join(f'[{float(l):.12f},{float(h):.12f}]' for l,h,m in roots))
