#!/usr/bin/env python3
"""Exhaustively distinguish strict and original proper-GCD masking counts."""
from math import gcd
from verify import k_formula

def full_D_proper_H(p,e):
    if p==3:
        return sum(2*3**(e-t-1) for t in range(e) if 1+2*t<e)
    return sum((p-1)*p**(e-t-1) for t in range(1,e) if 2*t<e)

def full_H_proper_D(p,e):
    total=0
    for t in range(1,e):
        n=e-t
        if 2*t>=e:
            total+=p**(2*n)-p**(2*n-2)-(p-1)*p**(n-1)
        elif p!=3 and p%3==1:
            m=e-2*t
            total+=2*(p-1)*p**(2*n-m-1)
        elif p==3 and 2*t+1==e:
            total+=2*(3**(2*n-2)-3**(n-1))
    return total

def brute(p,e):
    N=p**e
    strict=original=d_full=h_full=0
    for x in range(N):
        for y in range(N):
            D=x-y;H=x*x+x*y+y*y
            if D*H%N:continue
            gD=gcd(D,N);gH=gcd(H,N)
            strict+=(gD<N and gH<N)
            original+=(1<gD<N or 1<gH<N)
            d_full+=(gD==N and 1<gH<N)
            h_full+=(gH==N and 1<gD<N)
    return strict,original,d_full,h_full

def test():
    cases=[(3,1),(3,2),(3,3),(3,4),(3,5),
           (5,1),(5,2),(5,3),(5,4),
           (7,2),(7,3),(11,2),(11,3),(13,2)]
    for p,e in cases:
        strict=k_formula(p,e)
        d=full_D_proper_H(p,e)
        h=full_H_proper_D(p,e)
        predicted=(strict,strict+d+h,d,h)
        actual=brute(p,e)
        assert predicted==actual,(p,e,predicted,actual)
        print(f'p={p} e={e} N={p**e} strict={strict} original={strict+d+h} PASS')
    print(f'PASS: {len(cases)} exact bridge cases')

if __name__=='__main__':test()
