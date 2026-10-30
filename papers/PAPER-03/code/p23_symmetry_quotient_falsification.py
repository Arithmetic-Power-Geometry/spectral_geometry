from itertools import product
symbols=list(product((0,1),repeat=2))
offdiag=[(a,b) for i,a in enumerate(symbols) for b in symbols[i+1:]]
assert len(offdiag)==6
for a,b in offdiag:
    assert (('u',a),('v',b)) != (('u',b),('v',a))
print('PASS: all six off-diagonal orbits identify distinct independent-handle products')
print('x_(00,01)=u_00*v_01 differs formally from x_(01,00)=u_01*v_00')
