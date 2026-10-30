from itertools import permutations
from collections import Counter
A='01 02 03 12 23 14 24 34 45 46 05 13 15'.split()
B='01 02 03 12 23 14 24 34 45 46 56'.split()
def automorphisms(edges):
 E={tuple(sorted(map(int,e))) for e in edges}
 deg=Counter(i for e in E for i in e)
 return [p for p in permutations(range(7)) if all(deg[i]==deg[p[i]] for i in range(7)) and {tuple(sorted((p[i],p[j]))) for i,j in E}==E],Counter(deg.values())
def words(edges):
 adj=[0]*7
 for e in edges:
  i,j=map(int,e);adj[i]^=1<<j;adj[j]^=1<<i
 return [tuple(((x>>i)&1)+2*((adj[i]&x).bit_count()%2) for i in range(7)) for x in range(128)]
def fixed(ws,p):
 return sum(all(w[i]==w[p[i]] for i in range(7)) for w in ws)
if __name__=='__main__':
 for name,e,expected,trace in [('A',A,2,{64:1,128:1}),('B',B,4,{32:1,64:2,128:1})]:
  ps,d=automorphisms(e);ws=words(e)
  t=dict(Counter(fixed(ws,p) for p in ps))
  assert len(ps)==expected and t==trace
  print(name,'degrees',sorted(d.items()),'automorphisms',len(ps),'fixed-codeword-traces',sorted(t.items()))
 print('PASS exact 7! graph permutation and codeword fixed-point checks')
