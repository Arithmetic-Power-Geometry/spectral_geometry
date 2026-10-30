from itertools import product
S=range(4)
def classes(f):
    unseen=set(product(S,repeat=2)); out=[]
    while unseen:
        x=min(unseen); orbit={x,f(x)}
        assert f(f(x))==x
        unseen-=orbit;out.append(tuple(sorted(orbit)))
    return out
swap_copies=lambda ab:(ab[1],ab[0])
swap_XZ=lambda ab:({0:0,1:2,2:1,3:3}[ab[0]],{0:0,1:2,2:1,3:3}[ab[1]])
a=classes(swap_copies);b=classes(swap_XZ)
assert len(a)==len(b)==10
assert tuple(sorted(((0,1),(1,0)))) in a
assert tuple(sorted(((0,1),(0,2)))) in b
assert set(a)!=set(b)
print('copy-exchange orbits:',a)
print('X/Z-exchange orbits:',b)
print('PASS: inequivalent 10-class quotients')
