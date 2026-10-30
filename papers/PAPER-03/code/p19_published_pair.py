from itertools import product
from collections import Counter

# Henriksson-Kakkar-McPeak, JHEP04(2023)011, Eq. (4.19), page 33.
B1=['0100010','1010001','0101111','0010100','0011000','1010001','0110010']
B2=['0100011','1010001','0101111','0010100','0011000','1010001','1110010']

def enumerators(rows):
    B=[[int(x) for x in r] for r in rows]
    n=len(B)
    assert n==7 and all(len(r)==n for r in B)
    assert all(B[i][j]==B[j][i] for i in range(n) for j in range(n))
    C=[]
    for a in product(range(2),repeat=n):
        z=[sum(a[i]*B[i][j] for i in range(n))%2 for j in range(n)]
        C.append(tuple((a[j],z[j]) for j in range(n)))
    w=Counter(tuple(sum(1 for x,z in c if (x,z) in cls)
                    for cls in [{(0,0)},{(1,1)},{(1,0),(0,1)}]) for c in C)
    symbols=list(product(range(2),repeat=2))
    pairs=list(product(symbols,repeat=2))
    w2=Counter(tuple(sum(1 for x,y in zip(c,d) if (x,y)==pair)
                      for pair in pairs) for c in C for d in C)
    return w,w2

if __name__=='__main__':
    w1,t1=enumerators(B1)
    w2,t2=enumerators(B2)
    assert w1==w2 and len(w1)==16 and sum(w1.values())==128
    assert t1!=t2 and sum(t1.values())==sum(t2.values())==128**2
    assert len(t1)==5186 and len(t2)==5246
    diff=[k for k in t1.keys()|t2.keys() if t1[k]!=t2[k]]
    assert len(diff)==7956
    print('PASS genus one:',len(w1),'terms, 128 codewords each')
    print('PASS genus two:',len(t1),len(t2),'terms, differing labels',len(diff))
    print('First lexicographic difference:',next((k,t1[k],t2[k]) for k in sorted(diff)))
