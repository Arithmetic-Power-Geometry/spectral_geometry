#!/usr/bin/env python3
from fractions import Fraction as F
from collections import Counter
H=F(4);t=F(10)
def fingerprint(b):
    counts=Counter()
    # n_i in [-1,1] is sufficient since nonzero winding energy >=10>4.
    # m_i in [-7,7] contains all zero-winding states below H.
    for m1 in range(-7,8):
      for m2 in range(-7,8):
       for n1 in range(-1,2):
        for n2 in range(-1,2):
         e=((F(m1)+b*n2)**2+(F(m2)-b*n1)**2)/t+t*(n1*n1+n2*n2)
         if e<=H:counts[e]+=1
    return counts
a=fingerprint(F(0));b=fingerprint(F(1,5))
assert a==b and sum(a.values())==129 and len(a)==21
print("PASS: identical 21 energies, 129 states, H=4, t=10, b=0 versus 1/5")
