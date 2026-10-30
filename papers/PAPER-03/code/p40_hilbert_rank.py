from math import comb
def compositions(total, parts):
    if parts==1:
        yield (total,)
    else:
        for k in range(total+1):
            for tail in compositions(total-k,parts-1):
                yield (k,)+tail
pairs=((0,0),(0,1),(1,0),(1,1),(0,2),(2,0),(2,2),(1,2),(2,1),(2,2))
for n in (1,2,3,4,7):
    expected=comb(n+2,2)**2
    source=comb(n+9,9)
    if n<=4:
        seen=set()
        for powers in compositions(n,10):
            left=tuple(sum(powers[k] for k,(a,b) in enumerate(pairs) if a==i) for i in range(3))
            right=tuple(sum(powers[k] for k,(a,b) in enumerate(pairs) if b==j) for j in range(3))
            seen.add((left,right))
        assert len(seen)==expected
    print(f'n={n}: source={source}, image_rank={expected}, kernel={source-expected}')
print('PASS: exact rank formula, independently enumerated n=1..4')
