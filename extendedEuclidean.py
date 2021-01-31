'''
calculate (x, y) of ax + by = gcd(a, b)
return [gcd(a, b), x, y]
'''

def extendedEuclidean(a, b):
    if(a == 0):
        return [b, 0, 1]
    if(b == 0):
        return [a, 1, 0]
    x, y, z = extendedEuclidean(b, a%b)
    return [x, z, y - int(a/b)*z]

print(extendedEuclidean(4, 7))
print(extendedEuclidean(10, 23))
print(extendedEuclidean(14, 30))
