"""Exact symbolic certificate for fixed-energy Narain observation obstruction."""
import sympy as sp
b=sp.symbols('b', real=True)
G=sp.Matrix([[2,sp.Rational(1,3)],[sp.Rational(1,3),3]])
J=sp.Matrix([[0,1],[-1,0]])
Gi=G.inv()
assert G.det()>0 and G[0,0]>0
for m1 in range(-2,3):
 for m2 in range(-2,3):
  for n1 in range(-2,3):
   for n2 in range(-2,3):
    m=sp.Matrix([m1,m2]);n=sp.Matrix([n1,n2]);x=m+b*J*n
    E=sp.expand((x.T*Gi*x)[0]+(n.T*G*n)[0])
    coeff=sp.expand(E).coeff(b,2)
    if n1==n2==0:
     assert coeff==0 and not E.has(b)
    else:
     assert coeff>0
print('PASS: 625 exact charge polynomials; all nonzero winding coefficients positive')
