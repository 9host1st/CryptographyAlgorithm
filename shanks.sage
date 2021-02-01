'''
Shanks Algorithm
Calculate x of g^x = h (mod N)
'''

def shanks(g, h, N):
	e = 1
	N_order = Mod(g, N).multiplicative_order()
	n = 1 + floor(sqrt(N_order))
	A = [e]
	B = [h % N]
	for i in range(1, n + 1):
		A.append(power_mod(g, i, N))
	for i in range(1, n + 1):
		B.append((h*power_mod(g, -i * n, N)) % N)
	for i in range(n + 1):
		for j in range(n + 1):
			if(A[i] == B[j]):
				return i + j * n

x1 = (shanks(11, 21, 71))
x2 = (shanks(156, 116, 593))
x3 = (shanks(650, 2213, 3571))

assert pow(11, x1, 71) == 21
assert pow(156, x2, 593) == 116
assert pow(650, x3, 3571) == 2213
