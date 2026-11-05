from itertools import product
from math import gcd
from sympy import primitive_root

def local(p,a):
 if a%p==0:return [('11',0)]
 z=[('10',a%p)]
 if p%3==1:
  w=pow(int(primitive_root(p)),(p-1)//3,p)
  z.extend([('01',a*w%p),('01',a*w*w%p)])
 return z

def crt(vals,ps):
 N=1
 for p in ps:N*=p
 return sum(v*(N//p)*pow(N//p,-1,p) for v,p in zip(vals,ps))%N or N

def check(ps,s,k):
 N=1
 for p in ps:N*=p
 A=B=C=0
 for a in range(1,N+1):
  z=zc=0
  for choice in product(*(local(p,a) for p in ps)):
   if len(set(c[0] for c in choice))==1:continue
   z+=1
   if a<=s and crt([c[1] for c in choice],ps)<=s:zc+=1
  A+=z;B+=2*z*(a<=s);C+=zc
 X=k*N+s
 E=sum(1 for x in range(1,X+1) if 1<gcd(3*x*x,N)<N)
 M=k*k*A+k*B+C-E
 direct=sum(1 for x in range(1,X+1) for y in range(1,X+1) if x!=y and (x**3-y**3)%N==0 and (1<gcd(x-y,N)<N or 1<gcd(x*x+x*y+y*y,N)<N))
 assert M==direct,(ps,s,k,M,direct)
 return N,A,B,C,E,M

if __name__=='__main__':
 cases=[((5,7),10,0),((5,7),10,1),((7,13),20,0),((5,11),12,1),((5,7,11),12,0),((5,7,11),12,1),((5,7,11),12,2),((5,7,13),15,1),((5,7,11,13),15,0)]
 print('primes,N,s,k,A,B,C,E,M,verification')
 for ps,s,k in cases:
  print('-'.join(map(str,ps)),*check(ps,s,k),'PASS',sep=',')
 for ps in [(5,7),(7,13),(5,7,11),(5,7,13),(5,7,11,13)]:
  r=len(ps);N=1
  for p in ps:N*=p
  cap=3**r-2**r-1
  for a in range(1,N):
   n=sum(len(set(c[0] for c in choice))>1 for choice in product(*(local(p,a) for p in ps)))
   assert n<=cap,(ps,a,n,cap)
  print('candidate bound PASS',ps,cap)
