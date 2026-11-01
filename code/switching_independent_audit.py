"""Exact independent syndrome-by-syndrome switching audit for the five-qubit I/Z channel."""
import collections
import json
from pathlib import Path
import sympy as sp

t = sp.symbols('t')
gens = ['XZZXI','IXZZX','XIXZZ','ZXIXZ']
X = [sum(1<<i for i,c in enumerate(g) if c in 'XY') for g in gens]
Z = [sum(1<<i for i,c in enumerate(g) if c in 'ZY') for g in gens]
st = {(0,0)}
for a,b in zip(X,Z):
    st |= {(u^a,v^b) for u,v in tuple(st)}
def syndrome(z):
    return sum(((z&a).bit_count()%2)<<i for i,a in enumerate(X))
def coset(z):
    return min((u<<5)+(z^v) for u,v in st)
M = collections.defaultdict(lambda:sp.Integer(0))
for z in range(32):
    p = sp.prod((t if i<2 else 2*t) if z>>i&1 else (1-(t if i<2 else 2*t)) for i in range(5))
    M[syndrome(z),coset(z)] += p
assert len(M)==32 and sp.expand(sum(M.values()))==1
results = []
for s in range(16):
    pairs = sorted([(k,sp.expand(v)) for (ss,k),v in M.items() if ss==s])
    assert len(pairs)==2
    gap = sp.factor(pairs[0][1]-pairs[1][1])
    roots = []
    for (a,b),multiplicity in sp.polys.polytools.intervals(sp.Poly(gap,t),eps=sp.Rational(1,10**12)):
        if a>0 and b<sp.Rational(1,2):
            assert multiplicity==1
            roots.append((a,b))
    results.append((s,gap,roots))
expected = {0:3,1:2,2:4,3:2,4:4,5:2,7:2,8:2,9:4,10:2,12:2,14:2,15:1}
assert {s: (1 if r[0][0]<sp.Rational(1,10) else 2 if r[0][0]<sp.Rational(3,10) else 3 if r[0][0]<sp.Rational(7,20) else 4) for s,g,r in results if r}==expected
assert sum(len(r) for _,_,r in results)==13
assert len({round(float((a+b)/2),9) for _,_,rs in results for a,b in rs})==4
print('PASS: 16 syndromes; 13 interior switches; 4 distinct thresholds; no additional interior roots')
for s,g,rs in results:
    print(f'{s:04b}: gap={g}; roots='+','.join(f'({a},{b})' for a,b in rs))
