from collections import Counter
from p26_kernel_certificate import fibres,delta
from p27_min_certificate import min_edges

sizes=Counter(map(len,fibres.values()))
total=0;blocks=0;dist=Counter()
for key,terms in fibres.items():
    coeffs=tuple(c for _,c in sorted(terms))
    edges,b=min_edges(coeffs)
    total+=edges;blocks+=b;dist[(len(coeffs),b)]+=1
assert len(fibres)==143 and len(delta)==756
assert blocks==302 and total==454 and total==len(delta)-blocks
assert max(sizes)==16
print('PASS exact minimum',total,'zero-sum blocks',blocks,'fibres',len(fibres))
print('fibre sizes',sorted(sizes.items()))
print('optimal partition distribution',sorted(dist.items()))
