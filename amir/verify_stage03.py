from fractions import Fraction

def formula(p,e):
 d=int(p%3==1);out=0
 for t in range(1,(e-1)//2+1):
  m=e-t;h=e-2*t;L=max(0,e-3*t);phi=(p-1)*p**(m-1)
  if L:z=phi*(p**(m-L)-1+2*d*(p**(m-L)-p**(m-h)))
  else:z=p**(2*m)-p**(2*m-2)-phi-2*d*phi*p**(m-h)
  out+=z
 return out

def direct(p,e):
 n=p**e;out=0
 for x in range(n):
  for y in range(n):
   D=x-y;H=x*x+x*y+y*y
   out+=(D*H%n==0 and D%n!=0 and H%n!=0)
 return out

def coefficient_count(p,e):
 q=Fraction(1,p);delta=int(p%3==1)
 C=1-q*q-(1+2*delta)*(1-q)*q
 prob=Fraction(0)
 for t in range(e):
  a,b=t,2*t
  if a<e and b<e and a+b>=e:prob+=q**(2*t)*C
  for j in range(1,e+1):
   w=(1-q)**2*q**j*q**(2*t)
   if t+j<e and 2*t<e and 3*t+j>=e:prob+=w
   if t<e and 2*t+j<e and 3*t+j>=e:prob+=2*delta*w
 ans=prob*p**(2*e)
 assert ans.denominator==1,(p,e,ans)
 return int(ans)

if __name__=='__main__':
 print('p,e,formula,coefficient,direct')
 n_direct=0
 for p,e in [(5,2),(5,3),(7,3),(5,4),(7,4),(5,5),(7,5),(13,3),(13,4)]:
  f=formula(p,e);c=coefficient_count(p,e)
  z=direct(p,e) if p**e<=625 else None
  n_direct+=int(z is not None)
  assert f==c and (z is None or f==z),(p,e,f,c,z)
  print(f'{p},{e},{f},{c},{z if z is not None else "not-run"}')
 print(f'PASS: 9 coefficient checks, {n_direct} direct checks')
