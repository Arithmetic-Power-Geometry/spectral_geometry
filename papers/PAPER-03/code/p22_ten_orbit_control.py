from collections import Counter
from itertools import product
from p19_published_pair import B1,B2,enumerators
s=list(product((0,1),repeat=2))
pairs=list(product(s,repeat=2))
orbits=sorted({tuple(sorted(p)) for p in pairs})
index=[orbits.index(tuple(sorted(p))) for p in pairs]
def project(t):
    out=Counter()
    for ex,c in t.items():
        z=[0]*len(orbits)
        for i,v in enumerate(ex):z[index[i]]+=v
        out[tuple(z)]+=c
    return out
w1,t1=enumerators(B1);w2,t2=enumerators(B2)
p1,p2=project(t1),project(t2)
diff=[k for k in p1.keys()|p2.keys() if p1[k]!=p2[k]]
assert w1==w2 and len(orbits)==10
assert len(p1)==1432 and len(p2)==1395 and len(diff)==1636
assert sum(p1.values())==sum(p2.values())==16384
print('PASS: 10 unordered pair-type variables; terms',len(p1),len(p2),'differences',len(diff))
print('first lexicographic differing exponent',min(diff))
