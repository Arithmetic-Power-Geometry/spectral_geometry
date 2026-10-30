from collections import Counter
from itertools import product
from p19_published_pair import B1,B2
I=(0,0);Y=(1,1);X=(1,0);Z=(0,1)
classes=[[(I,I)],[(I,Y)],[(Y,I)],[(Y,Y)],[(I,X),(I,Z)],[(X,I),(Z,I)],[(X,X),(Z,Z)],[(Y,X),(Y,Z)],[(X,Y),(Z,Y)],[(X,Z),(Z,X)]]
idx={pair:j for j,cl in enumerate(classes) for pair in cl}
def refined(rows):
    n=len(rows); C=[]
    for a in product((0,1),repeat=n):
        z=[sum(a[i]*int(rows[i][j]) for i in range(n))%2 for j in range(n)]
        C.append(tuple(zip(a,z)))
    return Counter(tuple(sum(idx[(u[i],v[i])]==j for i in range(n)) for j in range(10)) for u in C for v in C)
def pivot(rows,i,j):
    A=[[int(v) for v in row] for row in rows]; assert A[i][j]
    B=[row[:] for row in A]; n=len(A)
    for a in range(n):
        for b in range(n):
            if a!=b and a not in (i,j) and b not in (i,j):
                B[a][b]=A[a][b]^(A[i][a]&A[j][b])^(A[j][a]&A[i][b])
    for a in range(n):
        if a not in (i,j):
            B[i][a]=B[a][i]=A[j][a]
            B[j][a]=B[a][j]=A[i][a]
    assert all(B[a][b]==B[b][a] and (a!=b or B[a][a]==0) for a in range(n) for b in range(n))
    return [''.join(map(str,row)) for row in B]
count=0
for label,rows in [('B1',B1),('B2',B2)]:
    original=refined(rows)
    for i in range(len(rows)):
        for j in range(i+1,len(rows)):
            if rows[i][j]=='1':
                changed=pivot(rows,i,j)
                assert refined(changed)==original,(label,i,j)
                count+=1
    print(label,'single-edge pivots PASS')
assert count==21
print('PASS: all 21 pivots preserve complete refined genus-two enumerator')
