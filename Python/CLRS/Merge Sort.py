def Merge_Sort(A: list[int], p: int, r: int):
    if p>=r:
        return
    q = (p + r) // 2
    Merge_Sort(A, p, q)
    Merge_Sort(A, q+1, r)
    Merge(A, p, q, r)

    return A

def Merge(A: list[int], p: int, q: int, r: int):
    n_l = q - p + 1
    n_r = r - q

    L = []
    R = []

    for i in range(n_l):
        L.append(A[p + i])

    for j in range(n_r):
        R.append(A[q + 1 + j])

    i = j = 0
    k = p
    while i < n_l and j < n_r:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
            k += 1
        else:
            A[k] = R[j]
            j += 1
            k += 1

    while i < n_l:
        A[k] = L[i]
        i += 1
        k += 1

    while j < n_r:
        A[k] = R[j]
        j += 1
        k += 1

    return A


print(Merge_Sort([4,3,1,2],0,3))