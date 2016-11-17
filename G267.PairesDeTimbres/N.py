def N(a, b):
    if b < a:
        a, b = b, a
    A = [0] * a
    idxMax = 0
    for k in range(1, a):
        i = (b * k) % a
        A[i] = math.floor((b * k) / a)
        if A[i] > A[idxMax]:
            idxMax = i
    n = A[idxMax]
    return n * a - (a - 1) + idxMax - 1
