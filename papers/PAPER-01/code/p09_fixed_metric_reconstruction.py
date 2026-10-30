#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import product
def first_above_two(b):
    energies=set()
    # For E<=5/2, ||n||<=sqrt(5/4)<2; |m_i|<=sqrt(5)+b*sqrt(5/4)<3.
    for m1,m2,n1,n2 in product(range(-3,4),range(-3,4),range(-1,2),range(-1,2)):
        e=((F(m1)+b*n2)**2+(F(m2)-b*n1)**2)/2+2*(n1*n1+n2*n2)
        if F(2)<e<=F(5,2):energies.add(e)
    return min(energies)
for b in [F(0),F(1,10),F(1,5),F(2,5),F(1,2)]:
    expected=F(5,2) if b==0 else F(2)+b*b/2
    assert first_above_two(b)==expected
print("PASS: exact five-point fixed-metric unlabelled reconstruction")
