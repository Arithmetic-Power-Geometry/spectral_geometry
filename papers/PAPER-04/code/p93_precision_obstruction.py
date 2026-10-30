"""P93 exact rational finite-precision Narain energy collision."""
from fractions import Fraction as F
from itertools import product
def energy(a,c,z):
 m1,m2,n1,n2=z
 return F(m1*m1,a)+F(m2*m2,c)+a*n1*n1+c*n2*n2
def nearest(x,q):
 y=x/q+F(1,2)
 return y.numerator//y.denominator
def main():
 a=F(2);c=F(22,7);q=F(1,100)
 for den in (100000,1000000,10000000):
  cp=c+F(1,den)
  assert c>a and a*c>1 and cp>a and a*cp>1
  assert {c/a,a*c}!={cp/a,a*cp}
  vectors=list(product(range(-2,3),repeat=4))
  mismatch=[z for z in vectors if nearest(energy(a,c,z),q)!=nearest(energy(a,cp,z),q)]
  assert not mismatch
  assert energy(a,c,(0,0,0,1))!=energy(a,cp,(0,0,0,1))
  print(f'denominator={den} vectors={len(vectors)} mismatches={len(mismatch)} inequivalent_reduced_moduli=True')
 print('PASS')
if __name__=='__main__':main()
