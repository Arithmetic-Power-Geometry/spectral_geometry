from collections import defaultdict,Counter
from itertools import combinations
CODES={'five_qubit': ['XZZXI','IXZZX','XIXZZ','ZXIXZ'], 'four_qubit_detect':['XXXX','ZZZZ'], 'three_qubit_bitflip':['ZZI','IZZ']}
def enc(s):
 x=z=0
 for i,c in enumerate(s):
  if c in 'XY':x|=1<<i
  if c in 'ZY':z|=1<<i
 return x,z
def mul(a,b):return a[0]^b[0],a[1]^b[1]
def sym(a,b):return ((a[0]&b[1]).bit_count()+(a[1]&b[0]).bit_count())%2
def wt(a):return (a[0]|a[1]).bit_count()
def audit(name,strings,p):
 n=len(strings[0]); g=list(map(enc,strings));assert all(len(s)==n for s in strings)
 assert all(sym(a,b)==0 for a,b in combinations(g,2))
 S={(0,0)}
 for a in g:S|={mul(s,a) for s in tuple(S)}
 assert len(S)==2**len(g)
 N=[];synd={};hist=Counter(); buckets=defaultdict(lambda:defaultdict(float))
 for x in range(1<<n):
  for z in range(1<<n):
   e=(x,z);w=wt(e);q=sum(sym(e,a)<<i for i,a in enumerate(g))
   if q==0:N.append(e)
   key=min(((x^a)<<n)|(z^b) for a,b in S)
   buckets[q][key]+=(p/3)**w*(1-p)**(n-w)
   hist[w]+=1
 assert sum(hist.values())==4**n
 d=min(wt(e) for e in N if e not in S)
 optimal=sum(max(cs.values()) for cs in buckets.values())
 print(name,'n,k,d',n,n-len(g),d,'S',len(S),'N',len(N),'syndromes',len(buckets),'optimal_success',format(optimal,'.12f'),'failure',format(1-optimal,'.12f'))
 return optimal
if __name__=='__main__':
 for p in (0.01,0.05,0.1):
  print('p',p)
  for name,g in CODES.items():audit(name,g,p)
 print('PASS')
