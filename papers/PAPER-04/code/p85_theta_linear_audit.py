import sympy as s
# HKM eqs (3.37)-(3.46): columns Theta33,34,43,44,32,42,23,24,11,22
M=s.Matrix([[1,1,1,1,0,0,0,0,0,0],[1,-1,1,-1,0,0,0,0,0,0],[1,1,-1,-1,0,0,0,0,0,0],[1,-1,-1,1,0,0,0,0,0,0],[0,0,0,0,1,1,0,0,0,0],[0,0,0,0,0,0,1,1,0,0],[0,0,0,0,0,0,0,0,1,1],[0,0,0,0,1,-1,0,0,0,0],[0,0,0,0,0,0,1,-1,0,0],[0,0,0,0,0,0,0,0,-1,1]])
print('rank',M.rank(),'det',M.det());assert M.det()==-128
print('Formal theta substitution is invertible; physical analytic independence NOT established')
