import sympy as s,numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from collections import defaultdict
T=s.symbols('t'); gens=['XZZXI','IXZZX','XIXZZ','ZXIXZ']; n=5
G=[(sum(1<<i for i,c in enumerate(w) if c in 'XY'),sum(1<<i for i,c in enumerate(w) if c in 'ZY')) for w in gens]
S={(0,0)}
for a,b in G:S|={(x^a,z^b) for x,z in list(S)}
def syn(z):return sum(((z&a).bit_count()%2)<<i for i,(a,b) in enumerate(G))
def key(z):return min((a<<n)+(z^b) for a,b in S)
M=defaultdict(lambda:s.Integer(0))
for z in range(32):
 p=s.Integer(1)
 for i in range(5):
  q=T if i<2 else 2*T;p*=q if z>>i&1 else 1-q
 M[syn(z),key(z)]+=p
by=defaultdict(list)
for (sy,k),p in M.items():by[sy].append((k,s.expand(p)))
base=[];diff=[];keys=[]
for sy in range(16):
 a,b=sorted(by[sy]);keys.append((a[0],b[0]));base.append(a[1]);diff.append(s.expand(b[1]-a[1]))
base=s.expand(sum(base));diff=s.Matrix(diff)
basefun=s.lambdify(T,base,'numpy');diffun=s.lambdify(T,diff,'numpy')
def row(t):return np.array([float(d.subs(T,t)) for d in diff]).reshape(16)
points=list(np.linspace(0,.5,101)); best=None
for it in range(40):
 A=np.array([row(t) for t in points]);b=np.array([float(base.subs(T,t)) for t in points]);
 # maximize z s.t. z - A x <= b
 c=np.r_[np.zeros(16),-1.];C=np.column_stack([-A,np.ones(len(points))]);res=milp(c,integrality=np.r_[np.ones(16),0],bounds=Bounds(np.r_[np.zeros(16),0],np.r_[np.ones(16),1]),constraints=LinearConstraint(C,-np.inf,b),options={'time_limit':60,'mip_rel_gap':1e-10});
 if res.x is None:print('fail',res.message);break
 x=np.rint(res.x[:16]).astype(int);poly=s.expand(base+sum(int(x[i])*diff[i] for i in range(16)))
 der=s.Poly(s.diff(poly,T),T); crit=[0.,.5]
 for (lo,hi),m in s.polys.polytools.intervals(der,eps=s.Rational(1,10**14)):
  v=float((lo+hi)/2)
  if 0<v<.5:crit.append(v)
 vals=[float(poly.subs(T,v)) for v in crit];idx=int(np.argmin(vals));v=crit[idx];lo=vals[idx]
 print(it,'MILP',res.x[-1],'actual',lo,'at',v,'x',''.join(map(str,x)),flush=True)
 best=(x,poly,lo,v,crit)
 if res.x[-1]-lo<1e-9:break
 points.append(v)
print('RESULT',best,'keys',keys)
from itertools import product
fixed=[(i,1 if diff[i].subs(T,s.Rational(1,4))>0 else 0) for i in range(16) if diff[i].subs(T,s.Rational(1,4))!=0]
free=[i for i in range(16) if diff[i].subs(T,s.Rational(1,4))==0]
print('free',free)
rank=[]
for bits in product((0,1),repeat=len(free)):
 xx=np.zeros(16,dtype=int)
 for i,vv in fixed:xx[i]=vv
 for i,vv in zip(free,bits):xx[i]=vv
 p=s.Poly(base+sum(int(xx[i])*diff[i] for i in range(16)),T)
 roots=np.roots([float(a) for a in p.diff().all_coeffs()]);pts=[0,.5]+[float(r.real) for r in roots if abs(r.imag)<1e-8 and 0<r.real<.5]
 m=min(float(p.eval(q)) for q in pts)
 rank.append((m,''.join(map(str,xx)),s.factor(p.as_expr())))
rank.sort(reverse=True)
for a in rank[:8]:print('TOP',a)
print('top count',len(rank),'gap',rank[0][0]-rank[1][0])
from collections import Counter
unique=Counter(str(p) for m,x,p in rank)
print('unique polys',len(unique),'top polys',rank[0][2]);print('candidate derivative',s.factor(s.diff(best[1],T)))
q=s.Rational(749591,1000000)
for pol in set(p for m,x,p in rank):
 if pol==rank[0][2]:continue
 pp=s.Poly(pol,T);roots=np.roots([float(a) for a in pp.diff().all_coeffs()]);pts=[s.Rational(0),s.Rational(1,2)]+[s.Rational(round(float(r.real)*10**9),10**9) for r in roots if abs(r.imag)<1e-8 and 0<r.real<.5]
 mn=min(pp.eval(pt) for pt in pts)
 if not mn<q:print('FAILED',pol,float(mn))
print('all other polynomials witness below',q)
for m,x,p in rank:
 if s.expand(p+(T-1)*(4*T*T-T+1))==0:print('CERT_DETERMINISTIC',x,m);break
