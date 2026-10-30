from fractions import Fraction as F
from itertools import product
from collections import Counter, defaultdict

H=F(2)
params=[(a,c,d,b) for a,c,d,b in product(
    [F(3,2),F(2),F(5,2)],
    [F(3,2),F(2),F(5,2)],
    [F(0),F(1,4)],
    [F(0),F(1,5),F(2,5)])]
groups=defaultdict(list)
for a,c,d,b in params:
    det=a*c-d*d
    assert det>0
    def E(m1,m2,n1,n2):
        x=m1+b*n2; y=m2-b*n1
        return (c*x*x-2*d*x*y+a*y*y)/det+a*n1*n1+2*d*n1*n2+c*n2*n2
    # All E<=2 charges fit: lambda_min(G)>=1.25, lambda_max(G)<=2.75,
    # ||B||<=0.4. Therefore ||n||<=sqrt(2/1.25)<1.265,
    # ||m||<=sqrt(2*2.75)+0.4*sqrt(2/1.25)<2.86.
    count=Counter()
    for v in product(range(-3,4),range(-3,4),range(-2,3),range(-2,3)):
        e=E(*v)
        if e<=H: count[e]+=1
    groups[tuple(sorted(count.items()))].append((a,c,d,b))
collisions=[v for v in groups.values() if len(v)>1]
pairs=sum(len(v)*(len(v)-1)//2 for v in collisions)
assert len(params)==54 and len(groups)==28 and len(collisions)==20 and pairs==34
print("PASS: 54 parameter points, 28 fingerprints, 20 collision groups, 34 collision pairs")
print("CAUTION: no O(2,2;Z) orbit classification, no inequivalent-isospectral claim")
