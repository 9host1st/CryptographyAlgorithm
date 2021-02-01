'''
Shanks Algorithm
Calculate x of g^x = h (mod N)
'''

# This file was *autogenerated* from the file shanks.sage
from sage.all_cmdline import *   # import sage library

_sage_const_1 = Integer(1); _sage_const_71 = Integer(71); _sage_const_116 = Integer(116); _sage_const_3571 = Integer(3571); _sage_const_156 = Integer(156); _sage_const_11 = Integer(11); _sage_const_593 = Integer(593); _sage_const_650 = Integer(650); _sage_const_2213 = Integer(2213); _sage_const_21 = Integer(21)
def shanks(g, h, N):
	e = _sage_const_1 
	N_order = Mod(g, N).multiplicative_order()
	n = _sage_const_1  + floor(sqrt(N_order))
	A = [e]
	B = [h % N]
	for i in range(_sage_const_1 , n + _sage_const_1 ):
		A.append(power_mod(g, i, N))
	for i in range(_sage_const_1 , n + _sage_const_1 ):
		B.append((h*power_mod(g, -i * n, N)) % N)

	for i in range(n + _sage_const_1 ):
		for j in range(n + _sage_const_1 ):
			if(A[i] == B[j]):
				return i + j * n

x1 = (shanks(_sage_const_11 , _sage_const_21 , _sage_const_71 ))
x2 = (shanks(_sage_const_156 , _sage_const_116 , _sage_const_593 ))
x3 = (shanks(_sage_const_650 , _sage_const_2213 , _sage_const_3571 ))

assert pow(_sage_const_11 , x1, _sage_const_71 ) == _sage_const_21 
assert pow(_sage_const_156 , x2, _sage_const_593 ) == _sage_const_116 
assert pow(_sage_const_650 , x3, _sage_const_3571 ) == _sage_const_2213 
