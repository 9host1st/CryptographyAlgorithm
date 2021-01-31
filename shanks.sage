import math
def shanks(g, h, N):
    e = IntegerModRing(N).order()
    n = 1 + int(math.sqrt(N))
    A = [e]
    B = [h]
    for i in range(1, n + 1):
        A.append((g**i) % N)
