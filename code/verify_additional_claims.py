"""Independent exact checks for additional claims in the associated article."""
import sympy as s
from collections import defaultdict
t=s.symbols("t", real=True)
gens=("XZZXI","IXZZX","XIXZZ","ZXIXZ")
G=[(sum(1<<i for i,c in enumerate(w) if c in "XY"),sum(1<<i for i,c in enumerate(w) if c in "ZY")) for w in gens]
S={(0,0)}
for a,b in G:S|={(x^a,z^b) for x,z in tuple(S)}
def syn(x,z):
 return sum((((x&b).bit_count()+(z&a).bit_count())%2)<<i for i,(a,b) in enumerate(G))
def key(x,z):
 return min(((x^a)<<5)+(z^b) for a,b in S)
def masses(rates):
 M=defaultdict(lambda:s.Integer(0))
 for z in range(32):
  p=s.Integer(1)
  for i,q in enumerate(rates):p*=q if z>>i&1 else 1-q
  M[syn(0,z),key(0,z)]+=p
 assert s.expand(sum(M.values())-1)==0
 return {j:sorted((k,s.expand(p)) for (sy,k),p in M.items() if sy==j) for j in range(16)}
H=masses([t]*5)
f=1-10*t**3+15*t**4-6*t**5
assert s.expand(sum(max(pair,key=lambda x:x[1].subs(t,s.Rational(1,10)))[1] for pair in H.values())-f)==0
C=masses([t,t,2*t,2*t,2*t])
assert sum(max(pair,key=lambda x:x[1].subs(t,s.Rational(1,4)))[1].subs(t,s.Rational(1,4)) for pair in C.values())==s.Rational(3,4)
# Explicit randomized choice in the nominal winner/rival ordering at t=1/10.
nominal={}
for j,pair in C.items():
 a,b=pair
 nominal[j]=(a,b) if a[1].subs(t,s.Rational(1,10))>=b[1].subs(t,s.Rational(1,10)) else (b,a)
chosen={0,2,4,6,9,11,13}
R=s.expand(sum(nominal[j][0 if j in chosen else 1][1] for j in range(16) if j!=14)
 +s.Rational(2,3)*nominal[14][0][1]+s.Rational(1,3)*nominal[14][1][1])
expected=(t-1)*(64*t**4-48*t**3-4*t**2+3*t-3)/3
assert s.expand(R-expected)==0
assert s.factor(R-s.Rational(3,4))==(2*t-1)*(4*t-1)**2*(8*t**2-6*t-3)/12
# All possible phase-free Pauli errors for an independent biased Pauli channel.
def pauli_success(Hsite=None):
 masses=defaultdict(lambda:s.Rational(0))
 probs={"I":s.Rational(90,100),"X":s.Rational(1,100),"Y":s.Rational(1,100),"Z":s.Rational(8,100)}
 from itertools import product
 for word in product("IXYZ",repeat=5):
  x=sum(1<<i for i,c in enumerate(word) if c in "XY")
  z=sum(1<<i for i,c in enumerate(word) if c in "ZY")
  if Hsite is not None:
   # Conjugating the code by H on one site equals conjugating the noise in the opposite direction.
   xbit=(x>>Hsite)&1;zbit=(z>>Hsite)&1
   x=(x&~(1<<Hsite))|(zbit<<Hsite)
   z=(z&~(1<<Hsite))|(xbit<<Hsite)
  p=s.prod(probs[c] for c in word)
  masses[syn(x,z),key(x,z)]+=p
 return sum(max((p for (sy,k),p in masses.items() if sy==j),default=0) for j in range(16))
v0=pauli_success()
assert v0==s.Rational(91983723,100000000)
assert any(pauli_success(i)==s.Rational(920436794,1000000000) for i in range(5))
print("PASS homogeneous success polynomial, coupled randomized factorization, adaptive upper bound, biased orientation")
