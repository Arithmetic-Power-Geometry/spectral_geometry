from collections import Counter
from functools import lru_cache
from p26_kernel_certificate import fibres,delta,image

def optimal_partition(coeffs):
    n=len(coeffs); full=(1<<n)-1
    sums=[0]*(full+1)
    for mask in range(1,full+1):
        bit=mask&-mask; i=bit.bit_length()-1
        sums[mask]=sums[mask^bit]+coeffs[i]
    @lru_cache(None)
    def solve(mask):
        if mask==0:return (0,())
        pivot=mask&-mask; best=(-1,())
        sub=mask
        while sub:
            if sub&pivot and sums[sub]==0:
                k,parts=solve(mask^sub)
                if 1+k>best[0]:best=(1+k,(sub,)+parts)
            sub=(sub-1)&mask
        return best
    return solve(full)

witness=[]; hist=Counter(); total_blocks=0
for key,terms in sorted(fibres.items()):
    terms=sorted(terms); coeffs=[c for _,c in terms]
    count,parts=optimal_partition(coeffs)
    total_blocks+=count; hist[(len(terms),count)]+=1
    for mask in parts:
        group=[terms[i] for i in range(len(terms)) if mask>>i&1]
        assert sum(c for _,c in group)==0
        pivot=group[0][0]
        for exp,c in group[1:]:
            witness.append((c,exp,pivot))
assert len(witness)==454 and total_blocks==302
recon=Counter()
for c,a,b in witness:
    assert image(a)==image(b)
    recon[a]+=c;recon[b]-=c
assert {e:c for e,c in recon.items() if c}==dict(delta)
print('PASS 454-term explicit witness; 302 blocks; 143 fibres; exact reconstruction')
print('distribution',sorted(hist.items()))
if __name__=='__main__':
    import json
    with open('p29_witness_454.json','w') as f:
        json.dump([{'coefficient':c,'positive_exponent':list(a),'negative_exponent':list(b)} for c,a,b in witness],f,indent=1)
