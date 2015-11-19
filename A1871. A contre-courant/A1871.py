# -*- coding: utf-8 -*-
import pdb
import math
import json

"""
La première étape consiste à calculer les valeurs de sigma pour chaque entier strictement inférieur à 2015.
"""

# Taille de la plus longue suite trouvée.
best_score = 1

# Nombre de sigmas strictements inférieurs pour les `k` supérieurs.
# Il s'agit d'une  optimisation. En effet, il est inutile  de prendre en
# compte  des `k`  qui ne  peuvent  pas mener  à des  suite de  longueur
# supérieure ou égale à 32.
candidates = []



primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987, 1993, 1997, 1999, 2003, 2011]

sigmas = []

def factor(n):
    """
    Retourner une liste des nombres premiers multiples de `n` avec leurs exposants.
    Par exemple 1960 = 2^3 * 5 + 7^2:
    ``` factor(1960) = ([2, 5, 7], [3, 1, 2]) ```
    Cette liste ne doit pas contenir `n` lui-même. Ainsi :
    ``` factor(653) == ([], []) ```
    """
    # Liste des facteurs (sauf 1 et `n`).
    result_primes = []
    # liste des exposants pour ces facteurs.
    result_exponents = []
    # Dernier facteur trouvé.
    last_factor = 1
    # Valeur du plus grand nombre premier pouvant diviser `n`.
    p_max = math.ceil(math.sqrt(n))
    # Index dans le tableau `primes`.
    p_idx = 0
    # Nombre premier courant.
    p = primes[p_idx]
    # Garder en mémoire la valeur initiale de `n` pour éviter de l'ajouter à `result`.
    m = n
    while p <= p_max and p < m:
        if n % p == 0:
            n = int(n / p)
            if p != last_factor:
                last_factor = p
                result_primes.append(p)
                result_exponents.append(1)
            else:
                # Augementer l'exposant du dernier facteur puisqu'il divise encore `n`.
                result_exponents[-1] += 1
        else:
            p_idx += 1
            p = primes[p_idx]
    if n < m and n > 1:
        result_primes.append(n)
        result_exponents.append(1)
    if len(result_primes) == 0:
        return ([m], [1])
    return (result_primes, result_exponents)


def find_divisors(factors, exponents, divisors, indexes=None):
    """
    Pour enumérer  les diviseurs, il  faut boucler sur les  exposants de
    chaque nombre premier de la  décomposition. Par exemple, 12 = 2^2*3,
    ses diviseurs sont  {2^a * 3^b} pour (a,b) dans  {0,1,2}x{0,1}. Il y
    en a donc 6.
    | 2 | 3 | Div.
    +---+---+------
    | 0 | 0 | 1
    | 0 | 1 | 3
    | 1 | 0 | 2
    | 1 | 1 | 6
    | 2 | 0 | 4
    | 2 | 1 | 12
    Pour calculer ceci, on utilise un algorithme récursif dont l'élément
    principal est la liste `indexes`.  Elle contient les valeurs itérées
    des exposants  pour chaque facteur  premier.  Les branches  de cette
    récursivité  ajoutent  des  éléments  à  `indexes`.  Quand  celui-ci
    possède autant d'éléments  que le nombre de facteurs,  alors on peut
    calculer un diviseur et l'ajouter à `divisors`.
    """
    if indexes == None:
        indexes = []
    index = len(indexes)
    if index == len(factors):
        divisor = 1
        for i in range(len(factors)):
            divisor *= factors[i] ** indexes[i]
        divisors.append(divisor)
    else:
        for i in range(exponents[index] + 1):
            indexes.append(i)
            find_divisors(factors, exponents, divisors, indexes)
            indexes.pop()


def sigma(n):
    """
    Calculer le sigma de `n`. C'est-à-dire  la somme de ses diviseurs (y
    compris 1 et  lui-même).  Ce calcul se base sur  la décomposition de
    `n` en facteurs premiers avec leurs puissances respectives.
    """
    factors, exponents = factor(n)
    divisors = []
    find_divisors(factors, exponents, divisors)
    return sum(divisors)

for n in range(2015):
    sigmas.append(sigma(n))

# Pour chaque `k`, on mémorise la plus longue suite décroissante de sigmas.
best_solutions = [None] * 2015

def solve(n):
    global best_score
    global best_solutions

    best = best_solutions[n]
    if best != None:
        return best[:]
    best = []
    s = sigmas[n]
    for k in range(n + 1, 2015):
        if sigmas[k] < s:
            candidate = solve(k)
            if len(candidate) > len(best):
                best = candidate
    best.append(n)
    best_solutions[n] = best;
    if len(best) >= best_score:
        best_score = len(best)
        disp = best[:]
        disp.reverse()
        print("----------------------------------------", len(disp))
        print("-----> ", disp)
        print("-----> ", [sigmas[k] for k in disp])
    return best[:]


print("Recherche en cours...")
n = 2014
while n > 0:
    solve(n)
    n -= 1
