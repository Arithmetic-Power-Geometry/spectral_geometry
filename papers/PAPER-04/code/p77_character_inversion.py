from fractions import Fraction as F
from itertools import product
from collections import Counter
from math import isqrt

def counts(A,r,L):
    g1,g2=A/r,A*r
    c=min(g1,g2,1/g1,1/g2)
    R=isqrt(L//c)
    counts=Counter()
    for m1,m2,n1,n2 in product(range(-R,R+1),repeat=4):
        E=m1*m1/g1+m2*m2/g2+g1*n1*n1+g2*n2*n2
        if E<=L:
            counts[(E,m1*n1+m2*n2,m1%2,m2%2)]+=1
    return counts,R

def transform(c):
    keys={(E,s) for E,s,_,_ in c}
    return {(E,s,a,b):sum(((-1)**(a*x+b*y))*c[(E,s,x,y)] for x,y in product(range(2),repeat=2)) for E,s in keys for a,b in product(range(2),repeat=2)}

def invert(t):
    keys={(E,s) for E,s,_,_ in t}
    return {(E,s,x,y):sum(((-1)**(a*x+b*y))*t[(E,s,a,b)] for a,b in product(range(2),repeat=2))//4 for E,s in keys for x,y in product(range(2),repeat=2)}

if __name__=='__main__':
    for A,r in [(F(1),F(1)),(F(2),F(3,2)),(F(3,2),F(2))]:
        c,R=counts(A,r,F(3));t=transform(c);inv=invert(t)
        assert all(inv[k]==c[k] for k in inv)
        assert all(sum(c[(E,s,x,y)] for x,y in product(range(2),repeat=2))==t[(E,s,0,0)] for E,s in {(e,s) for e,s,_,_ in c})
        print(f'PASS A={A},r={r},R={R},sectors={len(c)},Fourier coefficients={len(t)}')
    print('PASS: exact finite-character inversion; standard harmonic analysis, not novel')
