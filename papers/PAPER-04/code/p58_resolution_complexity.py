from fractions import Fraction as Q

def E(b):
    return Q(2)+Q(18,53)*b*b

def threshold(b1,b2):
    return abs(E(b1)-E(b2))/2

cases=[(Q(0),Q(1,10)),(Q(1,10),Q(1,5)),(Q(-1,5),Q(1,5))]
for a,b in cases:
    print(f'b={a} vs {b}: energies {E(a)}, {E(b)}; disjoint-error tolerance delta < {threshold(a,b)}')
assert E(Q(1,5))==E(Q(-1,5))
assert threshold(Q(0),Q(1,10))==Q(9,5300)
assert threshold(Q(1,10),Q(1,5))==Q(27,5300)
assert threshold(Q(-1,5),Q(1,5))==0
print('PASS: exact rational precision thresholds')
