from fractions import Fraction as F
from itertools import product
G=((F(2),F(0)),(F(0),F(3)))
R=((1,0),(0,-1))
def mul(A,B):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def trans(A):return tuple(zip(*A))
def energy(m,n,b):
 x=(F(m[0])+b*n[1],F(m[1])-b*n[0])
 return x[0]**2/2+x[1]**2/3+2*n[0]**2+3*n[1]**2
assert mul(mul(trans(R),G),R)==G
J=((0,1),(-1,0))
assert mul(mul(trans(R),J),R)==((0,-1),(1,0))
for K in (1,2,3):
 for z in product(range(-K,K+1),repeat=4):
  m=z[:2];n=z[2:];rm=(m[0],-m[1]);rn=(n[0],-n[1])
  assert energy(m,n,F(1,3))==energy(rm,rn,F(-1,3))
  assert sum(m[i]*n[i] for i in range(2))==sum(rm[i]*rn[i] for i in range(2))
 print('K',K,'PASS',(2*K+1)**4,'charges: energy and spin preserved')
print('PASS: explicit GL(2,Z) target-coordinate equivalence')
