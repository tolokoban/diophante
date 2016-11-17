# -*- coding: utf-8 -*-
import math

def is_prime(n):
    if n < 2:
        return False
    q = 2
    m = math.floor(math.sqrt(n))
    while q < m + 1:
        if n % q == 0:
            return False
        q += 1
    return True


def find_roots():
    roots = []
    for k in range(2, 12):
        for u in (1, 3, 5, 7, 9):
            n9 = u * (k - 1)
            if n9 % 9 == 0:
                n = int(n9 / 9)
                p = 10 * n + u
                if is_prime(p):
                    roots.append((u, k, p))
    roots.sort(key=lambda x:x[2])
    return roots
