"""P100-QEC: exact binary-symplectic graph-state audit; illustrative controls only."""
from itertools import combinations
from collections import Counter

def gf2_rank(rows,n):
    piv={}
    for x in rows:
        while x:
            k=x.bit_length()-1
            if k in piv:x^=piv[k]
            else:piv[k]=x;break
    return len(piv)

def graph_stabilizers(n,edges):
    adj=[0]*n
    for i,j in edges:
        assert i!=j and 0<=i<n and 0<=j<n
        adj[i]^=1<<j; adj[j]^=1<<i
    return [(1<<i)|(adj[i]<<n) for i in range(n)]

def group(gens):
    elements={0}
    for g in gens:elements|={x^g for x in tuple(elements)}
    return elements

def weight(p,n):
    return ((p&((1<<n)-1))|(p>>n)).bit_count()

def main():
    n=7
    controls={'empty':[], 'path':[(i,i+1) for i in range(n-1)],
              'cycle':[(i,(i+1)%n) for i in range(n)]}
    for name,edges in controls.items():
        gens=graph_stabilizers(n,edges)
        rank=gf2_rank(gens,2*n)
        assert rank==n
        for a,b in combinations(gens,2):
            xa=a&((1<<n)-1);za=a>>n
            xb=b&((1<<n)-1);zb=b>>n
            assert ((xa&zb).bit_count()+(za&xb).bit_count())%2==0
        elements=group(gens)
        assert len(elements)==2**n
        hist=Counter(weight(p,n) for p in elements)
        assert sum(hist.values())==128 and hist[0]==1
        print(name,'rank',rank,'size',len(elements),'logical_qubits',n-rank,
              'weight_enumerator',sorted(hist.items()))
    print('PASS: controls only; no real logical code, distance or decoding claims')
if __name__=='__main__':main()
