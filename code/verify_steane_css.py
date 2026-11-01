"""Exact independent [[7,1,3]] Steane CSS dephasing audit."""
from collections import defaultdict
from fractions import Fraction
N=7
rows=("1111000","1100110","1010101")
checks=[sum(1<<i for i,c in enumerate(row) if c=="1") for row in rows]
assert len(set(checks))==3 and all(x.bit_count()==4 for x in checks)
stab={0}
for a in checks:
    stab|={v^a for v in tuple(stab)}
assert len(stab)==8
def syndrome(z):
    return sum(((z&a).bit_count()%2)<<i for i,a in enumerate(checks))
def coset(z):
    return min(z^v for v in stab)
by=defaultdict(lambda:defaultdict(list))
for z in range(1<<N):
    by[syndrome(z)][coset(z)].append(z)
assert len(by)==8
assert all(len(v)==2 for v in by.values())
assert all(len(errors)==8 for v in by.values() for errors in v.values())
assert syndrome(127)==0 and 127 not in stab
assert sum(max(map(len,v.values())) for v in by.values())==64
assert all(syndrome(z)==syndrome(z^127) and coset(z)!=coset(z^127) for z in range(128))
for t in (Fraction(0),Fraction(1,10),Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1)):
    masses=[sum(t**z.bit_count()*(1-t)**(7-z.bit_count()) for z in errors)
            for v in by.values() for errors in v.values()]
    assert sum(masses)==1
    assert sum(Fraction(1,2)*mass for mass in masses)==Fraction(1,2)
assert len({coset(z) for z in range(128) if syndrome(z)==0})==2
print("PASS Steane [[7,1,3]]: 8 syndromes, two Z-cosets each, 8 errors/coset; uniform ML=1/2; deterministic endpoints=0; uniform randomized=1/2.")
