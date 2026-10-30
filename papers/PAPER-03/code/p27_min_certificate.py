from functools import lru_cache

def min_edges(coeffs):
    coeffs=tuple(coeffs)
    assert coeffs and all(x!=0 for x in coeffs) and sum(coeffs)==0
    n=len(coeffs); whole=(1<<n)-1
    zeros={mask for mask in range(1,whole+1) if sum(coeffs[i] for i in range(n) if mask>>i&1)==0}
    @lru_cache(None)
    def blocks(mask):
        if not mask:return 0
        pivot=mask & -mask
        return max(1+blocks(mask^s) for s in zeros if s&pivot and s&mask==s)
    return n-blocks(whole),blocks(whole)

for cs,expected in [((1,-1),1),((1,-1,2,-2),2),((1,1,-2),2),((1,1,-1,-1),2),((1,2,-3,4,-4),3)]:
    val,b=min_edges(cs)
    assert val==expected,(cs,val,b)
    print(cs,'minimum',val,'zero-sum blocks',b)
print('PASS')
