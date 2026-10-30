from collections import Counter
from itertools import product

def span(rows):
    n = len(rows[0]); out=set()
    for bits in product((0,1),repeat=len(rows)):
        x=0
        for b,r in zip(bits,rows):
            if b:x ^= int(''.join(map(str,r)),2)
        out.add(tuple((x >> (n-1-j))&1 for j in range(n)))
    return sorted(out)

def genus1(code):
    return Counter(sum(w) for w in code)

def genus2(code):
    return Counter(tuple(sum(1 for a,b in zip(u,v) if (a,b)==pattern)
        for pattern in ((0,0),(0,1),(1,0),(1,1))) for u in code for v in code)

def marginal(poly):
    size = __import__('math').isqrt(sum(poly.values()))
    assert size*size == sum(poly.values())
    return Counter({w:sum(mult for (n00,n01,n10,n11),mult in poly.items()
                   if n10+n11==w)//size for w in range(sum(next(iter(poly)))+1)})

if __name__=='__main__':
    C=span([(1,1,0,0),(0,0,1,1)])
    W1=genus1(C);W2=genus2(C)
    assert len(C)==4 and sum(W1.values())==4 and sum(W2.values())==16
    assert W1==Counter({0:1,2:2,4:1})
    assert marginal(W2)==Counter({0:1,2:2,4:1})
    assert all(sum(k)==4 for k in W2)
    print('PASS: toy binary code size=4; genus-one',dict(sorted(W1.items())),
          'genus-two ordered pairs=16; coefficient labels=',len(W2))
    print('NOTE: toy code is NOT a published isospectral CFT pair')
