from itertools import combinations
X=tuple('ABCD')
obs={'energy':{'A':0,'B':0,'C':0,'D':0},'spin_1':{'A':0,'B':0,'C':1,'D':1},'spin_2':{'A':0,'B':1,'C':0,'D':1}}
def partition(names):
    cells={}
    for x in X: cells.setdefault(tuple(obs[n][x] for n in names),[]).append(x)
    return tuple(sorted(tuple(v) for v in cells.values()))
def sep_pairs(names):
    return frozenset(p for p in combinations(X,2) if any(obs[n][p[0]]!=obs[n][p[1]] for n in names))
for r in range(4):
    for names in combinations(obs,r):
        print(names,'partition',partition(names),'separated',len(sep_pairs(names)),'of 6')
assert partition(('energy','spin_1','spin_2')) == (('A',),('B',),('C',),('D',))
assert len(sep_pairs(('spin_1',)))==4
assert len(sep_pairs(('spin_2',)))==4
assert len(sep_pairs(('spin_1','spin_2')))==6
print('PASS exact combinatorial assertions')
