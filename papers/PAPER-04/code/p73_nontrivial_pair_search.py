from fractions import Fraction as F
from itertools import combinations,product
from collections import Counter
from p72_spin_search import spectra,first
L=F(3)
models=[]
for a,d,h,b in product([F(2),F(3)],[F(2),F(3)],[F(0),F(1,3)],[F(0),F(1,5),F(1,3),F(2,5)]):
 s,_,_=spectra(a,d,h,b,L)
 models.append(((a,d,h,b),s))
counts=Counter();examples=[]
for (p,x),(q,y) in combinations(models,2):
 en=first(x,y,False);sp=first(x,y,True)
 if en is None and sp is None:kind='both_equal_through_cutoff'
 elif en is None:kind='spin_only_through_cutoff'
 elif sp is not None and sp<en:kind='spin_earlier'
 elif sp==en:kind='same_threshold'
 else:kind='other'
 counts[kind]+=1
 if kind in ('spin_only_through_cutoff','spin_earlier'):examples.append((p,q,en,sp))
assert sum(counts.values())==496
assert counts['spin_only_through_cutoff']==3
assert counts['spin_earlier']==0
print('models',len(models),'pairs',sum(counts.values()),'cutoff',L)
print('counts',counts)
print('examples',examples)
