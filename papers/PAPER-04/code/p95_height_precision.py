from fractions import Fraction as F
from itertools import product
from math import isqrt
def E(z,c):
 m1,m2,n1,n2=z
 return F(m1*m1,2)+F(m2*m2,1)/c+2*n1*n1+c*n2*n2
def rnd(x,step):
 y=x/step+F(1,2)
 return y.numerator//y.denominator
for k in (3,7,15,31,63):
 c=F(3*k+1,k);d=F(3*k+4,k+1);H=3*k+4;gap=abs(c-d)
 assert gap==F(1,k*(k+1)) and gap>=F(1,H*H)
 assert all(x.numerator<=H and x.denominator<=H for x in (c,d))
 assert rnd(c,F(1,H*H))!=rnd(d,F(1,H*H))
 print('k',k,'H',H,'gap',gap,'H²gap',H*H*gap)
c=F(22,7);d=c+F(1,100000);delta=abs(d-c)
for T in (2,4,8,12):
 bounds=[isqrt(2*T)+1,isqrt(4*T)+1,isqrt(T)+1,isqrt(T)+1]
 count=0
 for z in product(*(range(-b,b+1) for b in bounds)):
  if E(z,c)<=T:
   assert abs(E(z,d)-E(z,c))<=F(2*T,3)*delta
   count+=1
 print('T',T,'states',count,'Lipschitz PASS')
 assert count=={2:19,4:83,8:325,12:703}[T]
print('PASS; labelled probe result is not unlabelled spectral reconstruction')
