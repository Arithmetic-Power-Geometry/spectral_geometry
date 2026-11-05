from fractions import Fraction

def formula(p,e):
 d=int(p%3==1);s=0
 for t in range(1,(e-1)//2+1):
  m=e-t;h=e-2*t;L=max(0,e-3*t);ph=(p-1)*p**(m-1)
  if L>0:v=ph*(p**(m-L)-1+2*d*(p**(m-L)-p**(m-h)))
  else:v=p**(2*m)-p**(2*m-2)-ph-2*d*ph*p**(m-h)
  assert v>=0
  s+=v
 return s

def direct(p,e):
 n=p**e;m=n//p;ans=0
 for a in range(m):
  x=p*a
  for b in range(m):
   y=p*b;D=x-y;H=x*x+x*y+y*y
   ans+=D*H%n==0 and D%n!=0 and H%n!=0
 return ans

def coefficient(p,e):
 q=Fraction(1,p);d=int(p%3==1)
 C=1-q*q-(1+2*d)*(1-q)*q;z=Fraction(0)
 for t in range(e):
  if t<e and 2*t<e and 3*t>=e:z+=q**(2*t)*C
  for j in range(1,e+1):
   w=q**(2*t+j)*(1-q)**2
   if t+j<e and 2*t<e and 3*t+j>=e:z+=w
   if t<e and 2*t+j<e and 3*t+j>=e:z+=2*d*w
 r=z*p**(2*e)
 assert r.denominator==1
 return int(r)

if __name__=='__main__':
 print('p,e,formula,coefficient,direct')
 checked=0;exhaustive=0
 for p in (5,7,11,13):
  for e in range(2,8):
   f=formula(p,e);c=coefficient(p,e)
   assert f==c,(p,e,f,c)
   run=p**(2*(e-1))<=350000
   z=direct(p,e) if run else None
   assert z is None or z==f,(p,e,z,f)
   checked+=1;exhaustive+=int(run)
   print(p,e,f,c,z if run else 'skipped',sep=',')
 print('PASS',checked,'exact formula/series checks;',exhaustive,'direct enumerations')
