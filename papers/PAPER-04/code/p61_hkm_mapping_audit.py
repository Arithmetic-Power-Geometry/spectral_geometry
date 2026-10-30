from itertools import product
S=range(4)
labels={0:'1',1:'X',2:'Z',3:'Y'}
hkm=[[(0,0)],[(0,3)],[(3,0)],[(3,3)],[(0,1),(0,2)],[(1,0),(2,0)],[(1,1),(2,2)],[(3,1),(3,2)],[(1,3),(2,3)],[(1,2),(2,1)]]
copy=sorted(set(tuple(sorted({(a,b),(b,a)})) for a in S for b in S))
assert len(hkm)==len(copy)==10
assert sorted(x for orbit in hkm for x in orbit)==list(product(S,S))
assert {tuple(sorted(x)) for x in hkm}!={tuple(sorted(x)) for x in copy}
for i,orbit in enumerate(hkm):print('y'+str(i),'/'.join(labels[a]+labels[b] for a,b in orbit))
print('PASS: HKM ten-variable partition differs from copy-swap partition')
