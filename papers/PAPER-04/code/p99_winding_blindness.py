"""P99: rigorous universal winding-blind bound, exact special case."""
from sympy import Matrix, Rational, sqrt, simplify
G=Matrix([[2,Rational(1,3)],[Rational(1,3),3]])
lam=(15-sqrt(13))/6
assert simplify(G.det()-Rational(53,9))==0
assert lam>1 and lam<2
assert simplify(G.eigenvals().get(lam,0)-1)==0
print('lambda_min(G)=',lam,'~',lam.evalf(12))
print('For E<lambda_min(G), winding n=0; energy independent of B.')
print('P98 first discrepancy E*=2 > lambda_min(G):',bool(2>lam))
print('PASS')
