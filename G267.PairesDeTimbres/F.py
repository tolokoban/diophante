def recurs(candidates, idx, path):
    """
    A est une liste e colonnes.
    Chaque colonne possede le truple (a, b, N - 1).
    """
    if len(path) > 7:
        # Verifions si cette chaine est valide.
        orderedPath = path[:]
        orderedPath.sort(key=lambda x:x[2])
        print(orderedPath)
        return
    for k in range(idx, len(candidates)):
        candidat = candidates[k]
        goodCandidat = True
        if len(path) > 0:
            # Verifions que ce candidat est credible.
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
