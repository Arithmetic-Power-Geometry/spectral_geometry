from fractions import Fraction as F
from itertools import product
p=lambda t:t*t+(1-t)*(1-t)
assert p(F(0))==p(F(1))==1
assert p(F(1,2))==F(1,2)
assert all(p(F(i,100))>=F(1,2) for i in range(101))
q=lambda u,v:(1-u)*(1-v)+u*v
vertices=[q(F(u),F(v)) for u,v in product((0,1),repeat=2)]
for i,j in product(range(11),repeat=2):
 x=q(F(i,10),F(j,10))
 assert min(vertices)<=x<=max(vertices)
print('PASS: shared-parameter interior minimum; independent-parameter vertex bounds')
