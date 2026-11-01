import sympy as s, collections
x=s.symbols('t',real=True); gens=['XZZXI','IXZZX','XIXZZ','ZXIXZ']; n=5
G=[(sum(1<<i for i,c in enumerate(w) if c in 'XY'),sum(1<<i for i,c in enumerate(w) if c in 'ZY')) for w in gens]
S={(0,0)}
for a,b in G:S|={(u^a,v^b) for u,v in tuple(S)}
def syn(z):return sum(((z&a).bit_count()%2)<<i for i,(a,b) in enumerate(G))
def key(z):return min((a<<n)+(z^b) for a,b in S)
M=collections.defaultdict(lambda:s.Integer(0)); N=collections.defaultdict(list)
for z in range(32):
 p=s.prod((x if i<2 else 2*x) if z>>i&1 else (1-(x if i<2 else 2*x)) for i in range(5))
 M[syn(z),key(z)]+=p;N[syn(z)].append(z)
by=collections.defaultdict(list)
for (sy,k),p in M.items():by[sy].append((k,s.expand(p)))
assert len(by)==16 and s.expand(sum(M.values()))==1
D={}; alternate={}
for sy,entries in by.items():
 entries=sorted(entries,key=lambda e:sum(s.Rational(1,10)**z.bit_count()*s.Rational(9,10)**(5-z.bit_count()) for z in N[sy] if key(z)==e[0]),reverse=True)
 D[sy]=entries[0];alternate[sy]=entries[1]
F=s.factor(sum(p for k,p in D.values()));print('fixed polynomial:',F)
print('fixed endpoints:',F.subs(x,0),F.subs(x,s.Rational(1,2)))
print('fixed derivative:',s.factor(s.diff(F,x)))
print('fixed critical:',s.polys.polytools.intervals(s.Poly(s.diff(F,x),x),eps=s.Rational(1,10**12)))
print('fixed min:',s.minimum(F,x,s.Interval(0,s.Rational(1,2))))
branches=[-(2*x-1)*(24*x**4-30*x**3+4*x**2+2*x+1),-(x-1)*(32*x**4-24*x**3+x+1),(x-1)*(32*x**4-24*x**3+x-1),2*x*(24*x**4-42*x**3+31*x**2-12*x+3),-4*x*x*(4*x-3)]
for j,p in enumerate(branches):print('ML branch',j+1,'derivative',s.factor(s.diff(p,x)))
print('ML endpoints',branches[0].subs(x,0),branches[-1].subs(x,s.Rational(1,2)))
for j,p in enumerate(branches):
 roots=s.polys.polytools.intervals(s.Poly(s.diff(p,x),x),eps=s.Rational(1,10**10));print('critical',j+1,[(float(a),float(b)) for (a,b),m in roots if a>=0 and b<=s.Rational(1,2)])
print('ML 1/2:',branches[-1].subs(x,s.Rational(1,2)))
print('nominal fixed at 1/2',F.subs(x,s.Rational(1,2)))
print('nominal fixed at 1/4',F.subs(x,s.Rational(1,4)))
# Full randomized minimax: at t=0 only identity; at t=1/2 last three bits are certainly Z, first two fair.
# For each syndrome, compare endpoint supported coset keys.
for sy in range(16):
 z0=[z for z in range(32) if syn(z)==sy and ((z>>2)&7)==7]
 if z0:print('endpoint t=.5',sy,z0,[(z,key(z)) for z in z0], 'Dkey',D[sy][0])

# Exact randomized policy: choose nominal winner for syndrome indices
# 0,2,4,6,9,11,13; nominal loser for remaining except 14;
# at syndrome 14 use nominal winner with probability 2/3.
winners={0,2,4,6,9,11,13}
R=s.factor(sum((D[sy][1] if sy in winners else alternate[sy][1]) for sy in range(16) if sy!=14)+s.Rational(2,3)*D[14][1]+s.Rational(1,3)*alternate[14][1])
assert s.factor(R-s.Rational(3,4))==(2*x-1)*(4*x-1)**2*(8*x*x-6*x-3)/12
assert s.expand(F+(2*x-1)*(24*x**4-30*x**3+4*x*x+2*x+1))==0
assert branches[1].subs(x,s.Rational(1,4))==s.Rational(3,4)
print("PASS: fixed nominal worst=0; adaptive ML worst=3/4; randomized fixed robust=3/4")
print("Randomized polynomial:",R)
