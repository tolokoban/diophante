# -*- coding: utf-8 -*-

import pdb
import math
import pb2root


"""
http://www.diophante.fr/problemes-du-mois/2641-a1824-amputations-en-serie

Problème 2 ***
Je suis un entier naturel de 11  chiffres qui est un multiple de 4. On
choisit un certain entier k < 12. On supprime mon chiffre u des unités
et on ajoute la  quantité ku au nombre amputé à  10 chiffres. On opère
de la même manière avec le  nombre résultant dont on ampute le chiffre
des unités et  auquel on ajoute le  produit de ce chiffre  par le même
entier k  jusqu’au moment  où l’on  obtient un  nombre premier  qui se
répète indéfiniment. On recommence ces  amputations en série avec cinq
autres valeurs  de k toutes distinctes et  inférieures à  12. A chaque
fois, on obtient un nombre premier qui se répète.Qui suis-je ?
"""


def step(n, k):
    u = n % 10
    return int(k * u + (n - u) / 10)


def process(n, k):
    path = [n]
    while True:
        print(n)
        n = step(n, k)
        if n in path:
            print("Loop! ", len(path))
            break
        path.append(n)


def find_k(n):
    """
    Trouver le k tel que step(n, k) == n.
    S'il n'existe pas ou s'il est supérieur strict à 11, retourner -1.
    """
    u = n % 10
    p = int((n - u) / 10)
    k = (n - p) / u
    if k == math.floor(k):
        if k < 12:
            return int(k)
        else:
            return -2
    return -1


def back(n, k):
    """
    Retourner les nombres m tels que step(m, k) = n.
    """
    solutions = []
    for u in range(0, 10):
        x = n - k * u
        y = x * 10 + u
        if x > 0 and y != n:
            solutions.append(y)
    return solutions


def check(n):
    global loopingPrimes
    if n % 4 != 0:
        return False
    count = 0
    solutions = []
    primes = []
    for k in (2, 3, 4, 6, 7, 8, 9, 10, 11):
        values = []
        x = n
        old = 0
        while x != old:
            values.append(x)
            x = step(x, k)
        if x in loopingPrimes:
            primes.append(x)
            count += 1
            solutions.append("\item [$k = {0}$] : {1}, {2}".format(
                k, ", ".join([str(x) for x in values]), x))
    if count > 5:
        print("\\rule{\\linewidth}{1pt}")
        print("\\begin{description}")
        print("\n".join(solutions))
        print("\\end{description}")
        return True
    return False


def find(path, k):
    n = path[-1]
    if n > 10**10:
        if check(n):
            pass
            #print("k = {0} : ".format(k), path)
    else:
        for y in back(n, k):
            path.append(y)
            find(path, k)
            path.pop()


def print_roots(roots):
    print("\\begin{tabular}{|c|" + "r|" * len(roots) + "}")
    labels = ("$u$", "$k$", "$p$")
    for i in range(3):
        print("\\hline", labels[i], end=' & ')
        print(" & ".join([str(x[i]) for x in roots]), "\\\\")
    print("\\hline")
    print("\\end{tabular}")

roots = pb2root.find_roots()
loopingPrimes = [x[2] for x in roots]

## for u,k,p in roots:
##     if k not in (0, 10):
##         find([p], k)

percent = 100000
count = 0
for candidat in range(10000000000, 11000000000, 4):
    percent -= 4
    if percent == 0:
        percent = 100000
        count += .01
        print(count)
    if check(candidat):
        print("-" * 60)
