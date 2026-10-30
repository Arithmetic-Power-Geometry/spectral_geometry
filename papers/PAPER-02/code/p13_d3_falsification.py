#!/usr/bin/env python3
from fractions import Fraction as F
from collections import Counter
from itertools import product
from sympy import Matrix,Rational
G=Matrix([[2,Rational(1,4),0],[Rational(1,4),2,Rational(1,4)],[0,Rational(1,4),2]])
A=G.inv()
def rat(x):return F(int(x.p),int(x.q)) if hasattr(x,"p") else F(int(x))
g=[[rat(G[i,j]) for j in range(3)] for i in range(3)]
a=[[rat(A[i,j]) for j in range(3)] for i in range(3)]
def quad(x,q):return sum(x[i]*q[i][j]*x[j] for i in range(3) for j in range(3))
def fingerprint(b,c,H):
 B=[[F(0),b,F(0)],[-b,F(0),c],[F(0),-c,F(0)]]
 out=Counter()
 for n in product(range(-2,3),repeat=3):
  ne=quad(n,g)
  if ne>H:continue
  shift=[sum(B[i][j]*n[j] for j in range(3)) for i in range(3)]
  for m in product(range(-4,5),repeat=3):
   x=[m[i]+shift[i] for i in range(3)]
   e=ne+quad(x,a)
   if e<=H:out[e]+=1
 return out
for H,levels,states in [(F(2),10,27),(F(4),104,281)]:
 x=fingerprint(F(1,5),F(1,7),H)
 y=fingerprint(F(-1,5),F(-1,7),H)
 z=fingerprint(F(0),F(0),H)
 assert x==y and len(x)==levels and sum(x.values())==states
 diff=sorted(e for e in x.keys()|z.keys() if x[e]!=z[e])
 assert diff and diff[0]==2
 print("PASS",H,levels,states,"first difference",diff[0])
