# -*- coding: utf-8 -*-

print("Recherche exhaustive des solutions de Q1:")
print("------------------------------------------------------------")

for n in range(100, 1000):
    n2 = str(n * n)
    for i in range(1, len(n2) - 1):
        b = int(n2[i:])
        a = int(n2[:i])
        if a + b == n:
            print("n={}, n*n={}, {}+{}={}".format(n, n*n, a, n2[i:], n))
            break

print("------------------------------------------------------------")

for n in range(100, 1000):
    n3 = str(n * n * n)
    s = len(n3)
    for i in range(s - 4, s - 2):
        for j in range(i - 4, i - 2):
            if j < 1: continue
            a = n3[:j]
            if len(a) > 3: continue
            b = n3[j:i]
            if len(b) > 3: continue
            c = n3[i:]
            if len(c) > 3: continue
            #print("n={}, n³={}, {}-{}-{}", n, n3, a, b, c)
            if int(a) + int(b) + int(c) == n:
                print("n={}, n*n*n={}, {}+{}+{}={}".format(n, n3, a, b, c, n))
                break
