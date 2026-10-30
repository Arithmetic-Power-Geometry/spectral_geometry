import sympy as s
y0,y1,z0,z1,t=s.symbols('y0 y1 z0 z1 t')
D=y0-y1
transformed=s.expand(D.subs({y0:z0,y1:z1-z0},simultaneous=True))
assert transformed==2*z0-z1
assert s.expand(D.subs({y0:t,y1:t}))==0
assert s.expand(transformed.subs({z0:t,z1:2*t}))==0
assert s.expand(t-2*t)!=0
print('PASS: coordinate dependence of fixed-support equal-image binomial certificates')
