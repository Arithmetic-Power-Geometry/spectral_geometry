#!/usr/bin/env python3
"""Exact symbolic verification of four-probe inverse; requires sympy."""
import sympy as S
a,c,d,b=S.symbols("a c d b", real=True)
G=S.Matrix([[a,d],[d,c]])
B=S.Matrix([[0,b],[-b,0]])
def energy(G,b,v):
    m=S.Matrix(v[:2]); n=S.Matrix(v[2:])
    B=S.Matrix([[0,b],[-b,0]])
    return S.factor(((m+B*n).T*G.inv()*(m+B*n))[0]+(n.T*G*n)[0])
probes=[(1,0,0,0),(0,1,0,0),(1,1,0,0),(1,0,0,1)]
x,y,z,h=[energy(G,b,v) for v in probes]
A=S.Matrix([[x,(z-x-y)/2],[(z-x-y)/2,y]])
assert S.simplify(A-G.inv())==S.zeros(2)
assert S.simplify(h-x*(1+b)**2-G[1,1])==0
examples=[
(S.Rational(2),S.Rational(3),S.Rational(1,3),S.Rational(1,5)),
(S.Rational(3,2),S.Rational(7,4),S.Rational(1,4),-S.Rational(2,5)),
]
for aa,cc,dd,bb in examples:
    Gi=S.Matrix([[aa,dd],[dd,cc]])
    xx,yy,zz,hh=[energy(Gi,bb,v) for v in probes]
    Ai=S.Matrix([[xx,(zz-xx-yy)/2],[(zz-xx-yy)/2,yy]])
    assert Ai.inv()==Gi
    recovered=S.sqrt(S.factor((hh-Gi[1,1])/xx))-1
    assert S.simplify(recovered-bb)==0
# Negative control outside chosen branch:
G0=S.Matrix([[S.Integer(2),S.Rational(1,3)],[S.Rational(1,3),S.Integer(3)]])
assert all(S.simplify(energy(G0,S.Integer(0),v)-energy(G0,S.Integer(-2),v))==0 for v in probes)
print("PASS: symbolic identities, 2 rational examples, unrestricted-branch collision")
