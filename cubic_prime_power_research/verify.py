#!/usr/bin/env python3
"""Exact arithmetic checks of cubic collision masking; Python standard library only."""
from math import gcd
from itertools import combinations, product

def strict(x,y,N):
    D=x-y;H=x*x+x*y+y*y
    return D*H%N==0 and gcd(D,N)<N and gcd(H,N)<N

def k_formula(p,e):
    if p==3:
        a=0
        for t in range(1,(e-1)//2+1):
            if 3*t>=e:
                n=e-t;a+=6*3**(2*n-2)
        for t in range((e-2)//2+1):
            n=e-t;L=max(1,e-3*t-1)
            if L<n:a+=2*(3**(2*n-L-1)-3**(n-1))
        return a
    d=int(p%3==1);a=0
    for t in range(1,(e-1)//2+1):
        n=e-t;m=e-2*t;L=e-3*t
        if L<=0:
            a+=p**(2*n)-p**(2*n-2)-(p-1)*p**(n-1)-2*d*(p-1)*p**(2*n-m-1)
        else:
            a+=(p-1)*(p**(2*n-L-1)-p**(n-1))
            a+=2*d*(p-1)*(p**(2*n-L-1)-p**(2*n-m-1))
    return a

def prime_power_checks():
    cases=[(3,2),(3,3),(3,4),(3,5),(3,6),(5,2),(5,3),(5,4),(5,5),(7,2),(7,3),(7,4),(11,3),(13,3)]
    for p,e in cases:
        N=p**e;actual=sum(strict(x,y,N) for x in range(N) for y in range(N))
        expected=k_formula(p,e)
        assert actual==expected,(p,e,actual,expected)
        print('p=%d e=%d N=%d strict=%d PASS'%(p,e,N,actual))
    return len(cases)

def factors(N):
    ans=[];n=N
    for p in range(2,n+1):
        if p*p>n:break
        if n%p==0:
            ans.append(p)
            while n%p==0:n//=p
    if n>1:ans.append(n)
    return ans

def local_options(a,p):
    if a%p==0:return [(11,0)]
    if p%3==2:return [(10,a%p)]
    roots=[w for w in range(2,p) if pow(w,3,p)==1]
    assert len(roots)==2
    return [(10,a%p)]+[(1,w*a%p) for w in roots]

def crt(remainders,ps):
    N=1
    for p in ps:N*=p
    b=sum(v*(N//p)*pow(N//p,-1,p) for v,p in zip(remainders,ps))%N
    return b or N

def partners(a,ps):
    out=[]
    for choices in product(*(local_options(a,p) for p in ps)):
        if len({t for t,_ in choices})>1:
            out.append(crt([v for _,v in choices],ps))
    assert len(out)==len(set(out))
    return out

def b_formula(s,ps):
    r=len(ps);out=0
    for bit in range(1<<r):
        S=[i for i in range(r) if bit>>i&1]
        T=[i for i in range(r) if not bit>>i&1]
        if not S:
            m=1
            for p in ps:m*=1+2*(p%3==1)
            m-=1+(2**r if all(p%3==1 for p in ps) else 0)
        elif len(S)==r:m=0
        else:
            m=1
            for i in T:m*=1+2*(ps[i]%3==1)
        d=1
        for i in S:d*=ps[i]
        c=0
        for j in range(len(T)+1):
            for subset in combinations(T,j):
                dt=d
                for i in subset:dt*=ps[i]
                c+=(-1)**j*(s//dt)
        out+=m*c
    return 2*out

def squarefree_checks():
    total=0
    for ps,ss in [([5,7],[0,4,9,10,20,34]),([5,7,11],[0,4,9,20,50,100]),([5,7,11,13],[0,4,9,20,40])]:
        N=1
        for p in ps:N*=p
        for s in ss:
            brute=2*sum(len(partners(a,ps)) for a in range(1,s+1))
            formula=b_formula(s,ps)
            assert brute==formula,(ps,s,brute,formula)
            if N<=385:
                raw=2*sum((lambda d,h:d*h%N==0 and (1<gcd(d,N)<N or 1<gcd(h,N)<N))(a-b,a*a+a*b+b*b) for a in range(1,s+1) for b in range(1,N+1))
                assert raw==formula,(ps,s,raw,formula)
            total+=1
    def original(x,y,N):
        d=x-y;h=x*x+x*y+y*y
        return x!=y and d*h%N==0 and (1<gcd(d,N)<N or 1<gcd(h,N)<N)
    assert sum(original(x,y,35) for x in range(1,9) for y in range(1,9))==0
    assert sum(original(x,y,35) for x in range(1,10) for y in range(1,10))==2
    return total

if __name__=='__main__':
    print('Prime-power cases:',prime_power_checks())
    print('Square-free coefficient cases:',squarefree_checks())
    print('Mixed-prime N=35 threshold: X=9 PASS')
