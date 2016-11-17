# -*- coding: utf-8 -*-

import pdb
import sys
import math


def exceptionHandler(type, value, tb):
   if hasattr(sys, 'ps1') or not sys.stderr.isatty() or type == SyntaxError:
      # we are in interactive mode or we don't have a tty-like
      # device, so we call the default hook
      sys.__excepthook__(type, value, tb)
   else:
      import traceback
      # we are NOT in interactive mode, print the exception...
      traceback.print_exception(type, value, tb)
      print
      # ...then start the debugger in post-mortem mode.
      pdb.pm()

sys.excepthook = exceptionHandler




"""
Considérons deux timbres de valeurs entières distinctes strictement positives.
Appelons ces valeurs a et b. Alors il existe un entier naturel strictement positif N
tel que tout entier naturel supérieur ou égal à N puisse s'obtenir en ajoutants des timbres de valeur a et/ou b.

Par exemple, avec les valeurs 4 et 7, on peut obtenir toutes valeurs entières à partir de 18.
18 = 4*4 + 2 = 2*4 + 14 = 2*4 + 2*7
Mais il est impossible d'obtenir 17.

A partir de là, Diophante nous demande de trouver 8 paires distinctes dont les valeurs minimales se suivent de 2 en 2.
http://www.diophante.fr/problemes-du-mois/2633-g267-affranchissements-en-diophantie
"""


def strangers(a, b):
    if b < a:
        a, b = b, a
    if b % a == 0:
        return False
    for i in range(2, a - 1):
        if a % i == 0 and b % i == 0:
            return False
    return True


def find_min(a, b):
    """
    Pour trouver le nombre minimal, on suppose d'abord que a < b et que les deux nombres sont premiers entre eux.

    Exemple pour a = 4 et b = 7 :
    Posons n le quotient de la division euclidienne de la valeur considérée par a.
    On a alors les congruences suivantes modulo a :
    0 === a.n
    1 === a(n - 5) + 3b
    2 === a(n - 3) + 2b
    3 === a(n - 1) +  b

    Donc si n est supérieur ou égal à 5, on peut trouver une décomposition en a et b.
    Dans notre exemple, cela signifie qu'il est possible de réaliser tous les nombres à partir de 4*5 = 20.
    Mais on peut encore faire mieux en remarquant que 19 est congru à 3 modulo 4 et que dans ce cas,
    on trouve une solution si n est supérieur ou égal à 1. De même on peut aller jusqu'à 18.
    Donc N = 18.

    On peut facilement en déduire un algorithme que cette fonction implémente.
    """
    if not strangers(a, b):
        return -1
    if b < a:
        a, b = b, a
    # Tableau représentant les (n - A).
    A = [0] * a
    idxMax = 0
    for k in range(1, a):
        i = (b * k) % a
        A[i] = math.floor((b * k) / a)
        if A[i] > A[idxMax]:
            idxMax = i
    n = A[idxMax]
    return n * a - (a - 1) + idxMax


def recurs(candidates, idx, path):
    """
    A est une liste e colonnes. Chaque colonne possède le truple (a, b, N - 1).
    """
    if len(path) > 7:
        # Vérifions si cette chaîne est valide.
        orderedPath = path[:]
        orderedPath.sort(key=lambda x:x[2])
        print(orderedPath)
        return
    for k in range(idx, len(candidates)):
        candidat = candidates[k]
        goodCandidat = True
        if len(path) > 0:
            # Vérifions que ce candidat est crédible.
            a, b, N = candidat
            for selectedCandidat in path:
                aa, bb, NN = selectedCandidat
                diff = abs(N - NN)
                if diff == 0 or diff > 14:
                    goodCandidat = False
                    break
                if aa == a or aa == b or bb == b or bb == a:
                    goodCandidat = False
                    break
        if goodCandidat:
            path.append(candidat)
            recurs(candidates, k + 1, path)
            path.pop()




candidates = []


"""
\noindent\begin{tabular}{r|r|r|r|r|}
& \bf 2 & \bf 3 & \bf 4 & \bf 5 \\
\hline
\bf 3 & 12 \\
\cline{2-3}
\bf 4 & - & 18 \\
\cline{2-4}
\bf 5 & 14 & 20 & 32 \\
\hline
\end{tabular}
"""

print("\\noindent\\begin{tabular}{" + "r|" * 10 + "}")
for b in range(3, 101):
    print("\\cline{2-" + str(b) + "}")
    print("\\bf", b, end='')
    for a in range(2, b):
        N = find_min(a, b)
        if N > 0:
            if N < 100:
                print("&", N, end=' ')
                candidates.append([a, b, N - 1])
            else:
                print("& ** ", end='')
        else:
            print("& -- ", end='')
    print("\\\\")
print("\\end{tabular}")
print()
print("-" * 60)
recurs(candidates, 0, [])
