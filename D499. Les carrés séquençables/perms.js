/**
 * Retourner la prochaine permutation du tableau de nombres `perm`.
 * Si les  éléments de  la permutation sont  déjà rangés  dans l'ordre
 * décroissant, retourner `null`.
 */
module.exports = function(perm) {
    // Index du dernier élément.
    var idxEnd = perm.length - 1;
    // Valeur du dernier élément.
    var last = perm[idxEnd];
    // Index de l'élément courant.
    var idxCur = idxEnd - 1;
    // Redescendre jusqu'au  premier dont  la valeur est  inférieure à
    // celle  de  son  successeur.  Par exemple,  dans  [2,1,3,0],  on
    // s'arrête à l'index 1 car 1<3.
    while (idxCur > -1) {
        // Valeur de l'élément courant.
        var val = perm[idxCur];
        // On a trouvé deux éléments consecutifs dont les valeurs sont
        // dans l'ordre croissant.
        if (val < last) break;
        last = val;
        idxCur--;  // Décrémenter idxCur
    }
    if (idxCur < 0) return null;
    // Préparer  un  tableau pour  le  retour  de cette  fonction.  On
    // l'initialise avec les `idxCur` premiers éléments de `perm`. Ces
    // éléments sont rangés par ordre décroissant.
    var out = perm.slice(0, idxCur);
    //
    var idxPivot = idxCur;
    idxCur++;   // Incrémenter `idxCur`.
    // Cette  fois-ci on  remonte  tant que  l'élément  courant a  une
    // valeur supérieure `val`.
    while (idxCur <= idxEnd && perm[idxCur] > val) idxCur++;
    var idxFirst = idxCur - 1;
    out.push( perm[idxFirst] );
    // On se repositionne sur le dernier élément.
    idxCur = idxEnd;
    while (idxCur > idxPivot) {
        if (idxCur == idxFirst) out.push( val );
        else out.push( perm[idxCur] );
        idxCur--;  // Décrémenter `idxCur`.
    }
    return out;
};

/*
def Next(perm):
    idxEnd = len(perm) - 1
    last = perm[idxEnd]
    idxCur = idxEnd - 1
    while idxCur > -1:
        val = perm[idxCur]
        if val < last:
            break
        last = val
        idxCur -= 1
    if idxCur < 0:
        return None
    out = perm[:idxCur]
    idxPivot = idxCur
    idxCur += 1
    while idxCur <= idxEnd and perm[idxCur] > val:
        idxCur += 1
    idxFirst = idxCur - 1
    out.append(perm[idxFirst])
    idxCur = idxEnd
    while idxCur > idxPivot:
        if idxCur == idxFirst:
            out.append(val)
        else:
            out.append(perm[idxCur])
        idxCur -= 1
    return out
*/
