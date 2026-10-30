from fractions import Fraction as F
from collections import Counter
from itertools import product

# Exact rational G=[[2,1/3],[1/3,3]], B=b[[0,1],[-1,0]]
def energy(v,b):
    m1,m2,n1,n2=v
    x=F(m1)+b*n2; y=F(m2)-b*n1
    return (27*x*x-6*x*y+18*y*y)/53+2*n1*n1+F(2,3)*n1*n2+3*n2*n2

V=list(product(range(-4,5),range(-4,5),range(-1,2),range(-1,2)))
assert len(V)==729
b=F(1,5)
plus=Counter();minus=Counter()
for v in V:
    for sign,table in [(1,plus),(-1,minus)]:
        e=energy(v,sign*b)
        if e<=3:
            table[(e,v[0]*v[2]+v[1]*v[3])]+=1
assert sum(plus.values())==sum(minus.values())==39
def unlabelled(table):
    out=Counter()
    for (e,s),n in table.items():out[e]+=n
    return out
assert unlabelled(plus)==unlabelled(minus)
energies=sorted(set(e for e,s in plus)|set(e for e,s in minus))
spins=set(s for e,s in plus)|set(s for e,s in minus)
diffs=[e for e in energies if any(plus[(e,k)]!=minus[(e,k)] for k in spins)]
assert diffs and diffs[0]==F(3313,1325)
assert (plus[(diffs[0],-1)],plus[(diffs[0],1)],minus[(diffs[0],-1)],minus[(diffs[0],1)])==(2,0,0,2)
# Algebraic parity identity: E_b(m,n)=E_-b(-m,n), and spin reverses.
for v in V:
    m1,m2,n1,n2=v
    assert energy(v,b)==energy((-m1,-m2,n1,n2),-b)
print("PASS: 729 candidate charges; 39 states per background; unlabelled equality; first spin difference 3313/1325; parity involution")
