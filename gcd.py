'''
Euclidean Algorithm
let r = a mod b, so gcd(a, b) = gcd(b, r)
'''

def gcd(a, b):
    if b == 0:
        return a
    if a == 0:
        return b
    return gcd(b, a%b)

# Testcase

print(gcd(4, 8))
print(gcd(8, 4))
print(gcd(2, 17))
print(gcd(11111102, 1111))
print(gcd(1231, 112727271))
