"""P102-QEC: independent exact [[5,1,3]] code verification (Python 3)."""
from itertools import product, combinations
from collections import Counter
G=['XZZXI','IXZZX','XIXZZ','ZXIXZ'];n=5
def encode(s):
 x=z=0
 for i,c in enumerate(s):
  if c in 'XY':x|=1<<i
  if c in 'ZY':z|=1<<i
 return (x,z)
def sym(a,b):return ((a[0]&b[1]).bit_count()+(a[1]&b[0]).bit_count())%2
def mul(a,b):return(a[0]^b[0],a[1]^b[1])
def wt(a):return(a[0]|a[1]).bit_count()
g=list(map(encode,G));assert all(sym(a,b)==0 for a,b in combinations(g,2))
st={(0,0)}
for v in g:st|={mul(x,v) for x in tuple(st)}
assert len(st)==16
norm=[(x,z) for x in range(32) for z in range(32) if all(sym((x,z),v)==0 for v in g)]
logical=[v for v in norm if v not in st]
assert len(norm)==64 and len(logical)==48
assert min(map(wt,logical))==3
errors=[(0,0)]+[encode('I'*i+c+'I'*(4-i)) for i in range(5) for c in 'XYZ']
def syndrome(e):return sum(sym(e,v)<<i for i,v in enumerate(g))
assert sorted(syndrome(e) for e in errors)==list(range(16))
assert all((syndrome(mul(a,b))!=0 or mul(a,b) in st) for a,b in product(errors,repeat=2))
print('stabilizers',len(st),'normalizer',len(norm),'nontrivial logicals',len(logical),'distance',min(map(wt,logical)))
print('stabilizer weights',dict(sorted(Counter(map(wt,st)).items())))
print('distinct syndromes',len({syndrome(e) for e in errors}),'pair tests',len(errors)**2)
print('guaranteed correction probability p=0.01:',(1-.01)**5+5*.01*(1-.01)**4)
print('PASS')
