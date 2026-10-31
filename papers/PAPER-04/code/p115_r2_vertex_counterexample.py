from fractions import Fraction as F
from itertools import product

def interpolate(v,ts):
    return sum((v[bits]*__import__('functools').reduce(lambda a,bt:a*(bt[1] if bt[0] else 1-bt[1]),zip(bits,ts),F(1)) for bits in product((0,1),repeat=len(ts))),F(0))

v={(0,0):F(3,10),(0,1):F(1,5),(1,0):F(2,5),(1,1):F(1,10)}
for i,j in product(range(11),repeat=2):
    assert interpolate(v,(F(i,10),F(j,10)))>=min(v.values())
assert min(max(F(i,100),1-F(i,100)) for i in range(101))==F(1,2)
assert max(F(0),1-F(0))==max(F(1),1-F(1))==1
print('PASS: fixed-decoder vertex bound and reoptimized-ML counterexample')
