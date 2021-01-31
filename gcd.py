def gcd(a, b):
	if b == 0:
		return a
	gcd(b, a%b)

print(gcd(28, 14))
