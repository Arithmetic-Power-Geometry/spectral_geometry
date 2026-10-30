from sympy import Rational, sqrt, I, simplify
D=sqrt(53)
tau=Rational(1,6)+I*D/6
rp=Rational(1,3)+I*D/3
rm=-Rational(1,3)+I*D/3
flip=lambda z:-z.conjugate()
assert simplify(abs(tau)**2-Rational(3,2))==0
assert simplify(abs(rp)**2-6)==0
assert simplify(abs(rm)**2-6)==0
assert all(abs(float(z.as_real_imag()[0]))<.5 and float(abs(z)**2)>1 for z in (tau,rp,rm,flip(tau)))
A={tau,rp};B={tau,rm}
assert A!=B and {flip(z) for z in A}!=B
print('tau=',tau,'rho_plus=',rp,'rho_minus=',rm)
print('norms squared tau,rho=',simplify(abs(tau)**2),simplify(abs(rp)**2))
print('all interior of standard PSL2Z fundamental domain: YES')
print('unordered modular canonical pairs equal:',A==B)
print('simultaneously reflected unordered pairs equal:',{flip(z) for z in A}==B)
print('NOTE: oriented-duality subgroup certificate; worldsheet parity is separately scoped')
