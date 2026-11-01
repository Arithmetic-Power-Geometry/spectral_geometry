from fractions import Fraction
from collections import defaultdict
from itertools import product
G=('XZZXI','IXZZX','XIXZZ','ZXIXZ')
def mask(w):return (sum(1<<i for i,c in enumerate(w) if c in 'XY'),sum(1<<i for i,c in enumerate(w) if c in 'ZY'))
def ml(gens):
 B=[mask(w) for w in gens]; S={(0,0)}
 for a,b in B:S|={(x^a,z^b) for x,z in tuple(S)}
 P={'I':Fraction(90,100),'X':Fraction(1,100),'Y':Fraction(1,100),'Z':Fraction(8,100)}
 masses=defaultdict(Fraction)
 for w in product('IXYZ',repeat=5):
  x,z=mask(w);sy=sum((((x&b).bit_count()+(z&a).bit_count())%2)<<j for j,(a,b) in enumerate(B))
  key=min(((x^a)<<5)+(z^b) for a,b in S)
  p=Fraction(1)
  for c in w:p*=P[c]
  masses[sy,key]+=p
 return sum(max(v for (ss,_),v in masses.items() if ss==s) for s in range(16))
base=ml(G)
H=str.maketrans('XZ','ZX')
rot=[w[0].translate(H)+w[1:] for w in G]
other=ml(rot)
print('BASE',base,float(base),'ROTATED',other,float(other),'DIFFERENCE',other-base)
assert base==Fraction(91983723,100000000)
assert other==Fraction(920436794,1000000000)
print('PASS orientation exact')
