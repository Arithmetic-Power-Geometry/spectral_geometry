import sympy as S, collections
x=S.symbols('t'); G=['XZZXI','IXZZX','XIXZZ','ZXIXZ']; n=5
A=[sum((c in 'XY')<<i for i,c in enumerate(g)) for g in G]
B=[sum((c in 'ZY')<<i for i,c in enumerate(g)) for g in G]
st={(0,0)}
for a,b in zip(A,B):st|={(p^a,q^b) for p,q in list(st)}
def sy(z):return sum(((z&a).bit_count()%2)<<i for i,a in enumerate(A))
def ky(z):return min((p<<5)+(z^q) for p,q in st)
M=collections.defaultdict(lambda:S.Integer(0))
for z in range(32):
 p=S.Integer(1)
 for i in range(5):
  v=x if i<2 else 2*x
  p*=v if z>>i&1 else 1-v
 M[sy(z),ky(z)]+=p
by=collections.defaultdict(list)
for (s,k),v in M.items():by[s].append((k,S.expand(v)))
assert len(by)==16 and S.expand(sum(M.values()))==1
D={}; switches=[]; polys={}
for s,vals in sorted(by.items()):
 a,b=vals
 def nom(k):return sum(S.Rational(1,10)**z.bit_count()*S.Rational(9,10)**(5-z.bit_count()) for z in range(32) if sy(z)==s and ky(z)==k)
 if nom(a[0])<nom(b[0]):a,b=b,a
 D[s]=a[0]
 g=S.factor(a[1]-b[1]);polys[s]=g
 for (lo,hi),mult in S.polys.polytools.intervals(S.Poly(g,x),eps=S.Rational(1,10**14)):
  if lo>0 and hi<S.Rational(1,2):switches.append((float((lo+hi)/2),s,lo,hi))
print('SWITCHES',len(switches))
for t,s,l,h in sorted(switches):print(s,repr(t),S.factor(polys[s]))
thresholds=[]
for t,s,l,h in sorted(switches):
 if not thresholds or abs(t-thresholds[-1][0])>1e-10:thresholds.append((t,l,h))
print('DISTINCT',len(thresholds))
Pnom=S.factor(sum(v for (s,k),v in M.items() if D[s]==k));print('NOM',Pnom)
# independent exact ML value computed as average of sum masses and absolute gap
Pml=S.expand((sum(M.values())+sum(S.Abs(polys[s]) for s in by))/2)
print('ML',Pml)
for i in range(len(thresholds)+1):
 left=0 if i==0 else thresholds[i-1][0]
 right=.5 if i==len(thresholds) else thresholds[i][0]
 mid=S.Rational(str((left+right)/2))
 q=S.factor((sum(M.values())+sum((1 if polys[s].subs(x,mid)>=0 else -1)*polys[s] for s in by))/2)
 assert S.simplify(q.subs(x,mid)-sum(max(v.subs(x,mid) for _,v in by[s]) for s in by))==0
 print('REGION',i, left,right,'P=',q)
print('PASS')
