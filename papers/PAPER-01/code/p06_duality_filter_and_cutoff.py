from fractions import Fraction as F
from itertools import product, combinations
from collections import Counter, defaultdict
from math import sqrt, ceil

PARAMS=list(product([F(3,2),F(2),F(5,2)],[F(3,2),F(2),F(5,2)],[F(0),F(1,4)],[F(0),F(1,5),F(2,5)]))
def energy(p,v):
    a,c,d,b=p
    m1,m2,n1,n2=v
    x=m1+b*n2
    y=m2-b*n1
    det=a*c-d*d
    return (c*x*x-2*d*x*y+a*y*y)/det+a*n1*n1+2*d*n1*n2+c*n2*n2

def fingerprint(p,H):
    # Valid for THIS grid only: eigmin(G)>=5/4, eigmax(G)<=11/4, |b|<=2/5.
    # If E<=H, ||n||<=sqrt(4H/5), ||m||<=sqrt(11H/4)+(2/5)sqrt(4H/5).
    N=ceil(sqrt(float(H)*4/5))
    M=ceil(sqrt(float(H)*11/4)+F(2,5)*sqrt(float(H)*4/5))
    hist=Counter()
    for m1,m2,n1,n2 in product(range(-M,M+1),range(-M,M+1),range(-N,N+1),range(-N,N+1)):
        e=energy(p,(m1,m2,n1,n2))
        if e<=H:hist[e]+=1
    return tuple(sorted(hist.items()))

def obvious(u,v):
    a,c,d,b=u; aa,cc,dd,bb=v
    return ((a,c,d)==(aa,cc,dd) or (a,c,d)==(cc,aa,dd)) and (b==bb or b==-bb)

groups=defaultdict(list)
for p in PARAMS:groups[fingerprint(p,F(2))].append(p)
pairs=[(u,v) for g in groups.values() for u,v in combinations(g,2)]
obvious_pairs=[(u,v) for u,v in pairs if obvious(u,v)]
remaining=[(u,v) for u,v in pairs if not obvious(u,v)]
assert (len(PARAMS),len(groups),len(pairs),len(obvious_pairs),len(remaining))==(54,28,34,18,16)
f4={p:fingerprint(p,F(4)) for pair in remaining for p in pair}
assert all(f4[u]!=f4[v] for u,v in remaining)
example_u=(F(2),F(2),F(0),F(1,5))
example_v=(F(2),F(2),F(0),F(2,5))
A=dict(f4[example_u]);B=dict(f4[example_v])
first=min(e for e in set(A)|set(B) if A.get(e,0)!=B.get(e,0))
assert first==F(101,50) and (A[first],B.get(first,0))==(4,0)
print("PASS: 54 backgrounds; 34 H=2 collision pairs; 18 obvious; 16 split by H=4")
print("EXACT witness: E=101/50, multiplicities 4 versus 0")
