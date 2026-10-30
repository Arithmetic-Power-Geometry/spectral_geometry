from collections import Counter
from itertools import product
# G=I_2, B=0; E=||m||^2+||n||^2, spin=m dot n.
states=[]
for v in product(range(-2,3),repeat=4):
    m=v[:2];n=v[2:];e=sum(x*x for x in v)
    if e<=2:states.append((v,e,sum(m[i]*n[i] for i in range(2))))
c=Counter((e,s) for _,e,s in states)
pair=Counter()
for v,e,s in states:
    for w,f,t in states:pair[(e,s,f,t)]+=1
assert all(pair[(e,s,f,t)]==c[(e,s)]*c[(f,t)] for e,s in c for f,t in c)
assert len(states)==33 and len(pair)==25 and len(states)**2==1089
print("PASS",len(states),len(pair),len(states)**2,sorted(c.items()))
