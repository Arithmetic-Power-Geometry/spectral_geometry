from math import prod

def phi(p,h): return (p-1)*p**(h-1)
def primitive_cube(p,h):
    roots=3 if p==3 and h>=2 else 1 if p in (2,3) else 3 if p%3==1 else 1
    return roots*phi(p,h)
def primitive_H(p,h):
    if p==3: return 2 if h==1 else 0
    if p==2: return 0
    return 2*phi(p,h) if p%3==1 else 0
def local(p,e):
    a=(e+2)//3; b=(e+1)//2
    T=p**(2*(e-a))+sum(p**(4*t)*primitive_cube(p,e-3*t) for t in range(a))
    D=p**e
    H=p**(2*(e-b))+sum(p**(2*t)*primitive_H(p,e-2*t) for t in range(b))
    I=p**(e-max(0,(e-(1 if p==3 else 0)+1)//2))
    return T,D,H,I
def factor(n):
    out=[];p=2
    while p*p<=n:
        if n%p==0:
            e=0
            while n%p==0:n//=p;e+=1
            out.append((p,e))
        p+=1
    if n>1:out.append((n,1))
    return out
def strict_formula(n):
    z=[local(p,e) for p,e in factor(n)]
    return prod(x[0] for x in z)-prod(x[1] for x in z)-prod(x[2] for x in z)+prod(x[3] for x in z)
def strict_direct(n):
    ans=0
    for x in range(n):
        for y in range(n):
            D=x-y;H=x*x+x*y+y*y
            ans+=(D*H%n==0 and D%n!=0 and H%n!=0)
    return ans
if __name__=='__main__':
    for p in (2,3,5,7,11):
        for e in range(1,5):
            if p**e>300:continue
            n=p**e;T,D,H,I=local(p,e)
            brute=(sum((x**3-y**3)%n==0 for x in range(n) for y in range(n)),
                   n,
                   sum((x*x+x*y+y*y)%n==0 for x in range(n) for y in range(n)),
                   sum((x-y)%n==0 and (x*x+x*y+y*y)%n==0 for x in range(n) for y in range(n)))
            assert (T,D,H,I)==brute,(p,e,(T,D,H,I),brute)
    for n in (6,10,12,15,18,20,21,24,30,35,36,45,50,60,72,75,84,90,100,105,126,175,225,245):
        expected=strict_formula(n);actual=strict_direct(n)
        assert expected==actual,(n,expected,actual)
        print(n,expected,actual,sep=',')
    print('PASS: all local and mixed-composite tests')
