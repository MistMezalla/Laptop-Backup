def Merge_Sort(A: list[int], p: int, r: int):
    if p>=r:
        return

    q=(p+r)//2
    Merge_Sort(A,p,q)
    Merge_Sort(A,q+1,r)
    Merge(A,p,q,r)

    return A

def Merge(A: list[int], p: int, q: int,r: int):
    m = q-p+1
    n = r-q

    L = []
    R = []

    for i in range(m):
        L.append(A[p+i])
    for j in range(n):
        R.append(A[q+1+j])

    i=j=0
    k=p

    while(i<m and j<n):
        if L[i] <= R[j]:
            A[k] = L[i]
            k+=1
            i+=1
        else:
            A[k] = R[j]
            k += 1
            j += 1

    while i<m:
        A[k] = L[i]
        k += 1
        i += 1

    while j<m:
        A[k] = R[j]
        k += 1
        j += 1

    return A

def Bin_Search(A: list[int], x: int):
    b = 0
    e = len(A)-1

    while(b<=e):
        m=(b+e)//2

        if A[m] == x:
            return m
        else:
            if A[m] < x:
                b=m+1
            else:
                e=m-1

    return 0.1

def Solution(S: list[int], x: int):
    Merge_Sort(S,0,len(S)-1)
    Aux_S = S.copy()
    for i in range(len(S)):
        find=x-S[i]
        print(S)
        print(Aux_S)
        if (Bin_Search(Aux_S,S[i]) == 0 or Bin_Search(Aux_S,S[i])):
            Aux_S.pop(Bin_Search(Aux_S,S[i]))
            print(Aux_S)
        else:
            return False
        if (Bin_Search(Aux_S,find) != 0.1):
            return True

    return False

print(Solution([3,4,1,2],0))