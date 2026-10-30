"""P49: finite-box parity-completed Narain heat observables, numpy required."""
import numpy as np
from itertools import product
G=np.array([[2.,1/3],[1/3,3.]])
A=np.linalg.inv(G)
K=5
V=np.array(list(product(range(-K,K+1),repeat=4)),dtype=float)
m=V[:,:2]; n=V[:,2:]; s=np.sum(m*n,axis=1)
def evaluate(b,t):
    jn=np.stack([n[:,1],-n[:,0]],axis=1)
    u=m+b*jn
    E=np.einsum('ij,jk,ik->i',u,A,u)+np.einsum('ij,jk,ik->i',n,G,n)
    de=2*np.einsum('ij,jk,ik->i',jn,A,u)
    q=np.exp(-t*E)
    return np.sum(q),np.sum(s*q),-t*np.sum(de*q),-t*np.sum(s*de*q)
for b in [-.2,0.,.2]:
    print('b',b, 'H,O,dH,dO',evaluate(b,2.))
H,O,dH,dO=evaluate(.2,2.)
print('amplitude-b determinant',H*dO-O*dH)
assert abs(evaluate(.2,2.)[0]-evaluate(-.2,2.)[0])<1e-12
assert abs(evaluate(.2,2.)[1]+evaluate(-.2,2.)[1])<1e-12
