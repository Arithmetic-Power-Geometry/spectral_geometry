import sys
sys.path.insert(0,'/mnt/data')
import networkx as nx
from sympy import Matrix, ilcm
from functools import reduce
from math import gcd
ns={}
exec(open('/mnt/data/p41_admissible_span.py').read().split('for n in range(2,7):')[0],ns)
polys=ns['polys']
for n in (5,6):
 graphs=[g for g in nx.graph_atlas_g() if len(g)==n]
 data=[polys(g) for g in graphs]
 exps=sorted(set().union(*(w for w,f in data)))
 ims=sorted(set().union(*(f for w,f in data)))
 A=Matrix([[w.get(k,0) for w,f in data] for k in exps])
 B=Matrix([[f.get(k,0) for w,f in data] for k in ims])
 ra,rb=A.rank(),B.rank()
 print(n,len(graphs),ra,rb,ra-rb,flush=True)
 assert (ra,rb)==({5:(14,13),6:(27,23)}[n])
 if n==5:
  for v in B.nullspace():
   if A*v != Matrix.zeros(A.rows,1):
    denom=reduce(ilcm,[x.q for x in v],1)
    coeff=[int(x*denom) for x in v]
    d=reduce(gcd,[abs(x) for x in coeff if x],0)
    coeff=[x//d for x in coeff]
    if next(x for x in coeff if x)<0:coeff=[-x for x in coeff]
    assert B*Matrix(coeff)==Matrix.zeros(B.rows,1)
    witness=A*Matrix(coeff)
    assert witness!=Matrix.zeros(A.rows,1)
    print('certificate',[(i,c) for i,c in enumerate(coeff) if c])
    print('nonzero coefficients',sum(v!=0 for v in witness))
    print('first',next((exps[i],int(v)) for i,v in enumerate(witness) if v))
    break
