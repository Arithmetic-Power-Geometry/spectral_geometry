from fractions import Fraction as F
from itertools import product
def transform(z,a,b,c,d):
 x,y=z;u=a*x+b;v=a*y;w=c*x+d;t=c*y;den=w*w+t*t
 return ((u*w+v*t)/den,(v*w-u*t)/den)
def mats(B):
 return [(a,b,c,d) for a,b,c,d in product(range(-B,B+1),repeat=4) if a*d-b*c==1]
def orbit_witness(p,q,B):
 mm=mats(B)
 for swap in (False,True):
  s=p[::-1] if swap else p
  for a in mm:
   if transform(s[0],*a)!=q[0]:continue
   for b in mm:
    if transform(s[1],*b)==q[1]:return swap,a,b
 return None
I=(F(0),F(1));II=(F(0),F(2));HALF=(F(0),F(1,2));SHIFT=(F(1),F(1))
assert transform(II,0,-1,1,0)==HALF
assert orbit_witness((II,I),(HALF,I),1)
assert orbit_witness((II,I),(I,II),1)
assert orbit_witness((I,I),(SHIFT,I),1)
assert orbit_witness((I,I),(II,I),2) is None
print('PASS exact modular inversion, mirror, integer shift, bounded non-witness')
print('inversion',orbit_witness((II,I),(HALF,I),1))
print('mirror',orbit_witness((II,I),(I,II),1))
print('shift',orbit_witness((I,I),(SHIFT,I),1))
print('No bounded witness B=2 for (i,i) -> (2i,i); NOT global inequivalence')
