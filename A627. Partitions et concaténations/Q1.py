# -*- coding: utf-8 -*-

print("Recherche exhaustive des solutions de Q1:")

for n in range(100, 1000):
    n2 = str(n * n)
    for i in range(1, len(n2) - 1):
        b = int(n2[i:])
        a = int(n2[:i])
        if a + b == n:
            print("n={}, n*n={}, {}+{}={}".format(n, n*n, a, n2[i:], n))
            break
