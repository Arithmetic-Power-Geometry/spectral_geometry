from fractions import Fraction as F
from itertools import product
from collections import Counter
from math import isqrt
def energy(z,c):
 m1,m2,n1,n2=z
 return F(m1*m1,2)+F(m2*m2,1)/c+2*n1*n1+c*n2*n2
def spectrum(c,T):
 # For 3<=c<=4: E>=m1^2/2+m2^2/4+2*n1^2+3*n2^2.
 assert F(3)<=c<=F(4)
 bounds=[isqrt(2*T.numerator//T.denominator)+1,isqrt(4*T.numerator//T.denominator)+1,isqrt(T.numerator//T.denominator)+1,isqrt(T.numerator//T.denominator)+1]
 out=Counter()
 for z in product(*(range(-k,k+1) for k in bounds)):
  e=energy(z,c)
  if e<=T:out[e]+=1
 return out
def quantize(s,q):
 out=Counter()
 for e,m in s.items():
  x=e/q+F(1,2)
  out[x.numerator//x.denominator]+=m
 return out
if __name__=='__main__':
 c=F(22,7);cp=c+F(1,100000)
 for T,n in [(F(2),19),(F(4),83),(F(8),325),(F(12),703)]:
  s,t=spectrum(c,T),spectrum(cp,T)
  assert sum(s.values())==sum(t.values())==n and s!=t
  for q in [F(1,10),F(1,100),F(1,1000),F(1,10000)]:
   assert quantize(s,q)==quantize(t,q)
  assert quantize(s,F(1,100000))!=quantize(t,F(1,100000))
  print('T',T,'states',n,'q=1e-4 same; q=1e-5 different')
 print('PASS')
