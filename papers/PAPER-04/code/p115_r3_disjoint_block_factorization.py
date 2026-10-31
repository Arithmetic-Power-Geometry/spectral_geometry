from fractions import Fraction as F
from itertools import product
from collections import defaultdict
G=['XZZXI','IXZZX','XIXZZ','ZXIXZ']
P={'I':F(90,100),'X':F(1,100),'Y':F(1,100),'Z':F(8,100)}
M={'I':(0,0),'X':(1,0),'Y':(1,1),'Z':(0,1)}
def e(s):
 x=z=0
 for i,c in enumerate(s):
  a,b=M[c];x|=a<<i;z|=b<<i
 return x,z
def sym(a,b):return ((a[0]&b[1]).bit_count()+(a[1]&b[0]).bit_count())%2
g=list(map(e,G));S={(0,0)}
for a,b in g:S|={(x^a,z^b) for x,z in tuple(S)}
def masses(channel):
 out=defaultdict(lambda:defaultdict(F))
 for letters in product('IXYZ',repeat=5):
  x,z=e(letters);sy=sum(sym((x,z),q)<<i for i,q in enumerate(g))
  cos=min(((x^a)<<5)|(z^b) for a,b in S)
  prob=F(1)
  for c in letters:prob*=channel[c]
  out[sy][cos]+=prob
 return out
A=masses(P)
Q={'I':F(83,100),'X':F(4,100),'Y':F(3,100),'Z':F(10,100)}
B=masses(Q)
def success(v):return sum(max(c.values()) for c in v.values())
a,b=success(A),success(B)
combined=sum(max(x*y for x in ca.values() for y in cb.values()) for ca in A.values() for cb in B.values())
assert combined==a*b
assert sum(sum(c.values()) for c in A.values())==1
assert sum(sum(c.values()) for c in B.values())==1
print('PASS: exact disconnected-block ML factorization',a,b,combined)
for m in (1,2,3,4):
 print(m,5*m,4**(5*m),m*4**5,a**m)
