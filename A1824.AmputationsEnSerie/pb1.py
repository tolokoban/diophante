# -*- coding: utf-8 -*-

import pdb
import sys

"""
http://www.diophante.fr/problemes-du-mois/2641-a1824-amputations-en-serie

Pb1 ** Je  suis un entier naturel  de 6 chiffres. On  supprime l’un de
mes chiffres et le nombre résultant qui ne commence pas par un zéro me
divise. On  continue le  processus en supprimant  un chiffre  à chaque
étape et le nombre résultant qui ne commence jamais par un zéro divise
toujours  celui qui  le précède.On  s’arrête  quand il  reste un  seul
chiffre et  les quotients obtenus  par les cinq  divisions successives
sont tous distincts. Qui suis-je ?
"""


def find(path=[], quotients=[]):
    if len(path) == 6:
        # C'est gagné !
        print("-" * 60)
        for i in range(5):
            print("{0:6} * {1:2} = {2:6}".format(path[i], quotients[i + 1], path[i + 1]))
    elif len(path) == 0:
        quotients.append(1)
        for digit in range(1, 10):
            path.append(str(digit))
            find(path, quotients)
            path.pop()
        quotients.pop()
    else:
        first = 1
        n0 = path[-1]
        num0 = int(n0)
        for pos in range(0, len(path) + 1):
            for digit in range(first, 10):
                n1 = n0[0:pos] + str(digit) + n0[pos:]
                num1 = int(n1)
                if num1 % num0 == 0:
                    q = int(num1 / num0)
                    if q not in quotients:
                        path.append(n1)
                        quotients.append(q)
                        find(path, quotients)
                        quotients.pop()
                        path.pop()
            first = 0


find()
