def Insertion_Sort_incr(A: list[int]):
    for i in range(1, len(A)):
        j = i-1
        key = A[i]
        while key < A[j] and j > -1:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A

def Insertion_Sort_decr(A: list[int]):
    for i in range(1, len(A)):
        key = A[i]
        j = i-1
        while key > A[j] and j > -1:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key

    return A

def ADD_Bin_int(A: list[int], B: list[int]):
    C = []
    carry = 0
    for i in range(0, len(A)):
        res = A[i] + B[i]
        if res >= 2:
            C.append(res % 2)
            carry = res // 2
        else:
            C.append(res)
    C.append(carry)
    return C

def Insertion_Sort_rec(A: list[int], p: int, r: int):
    if p>=r:
        return
    Insertion_Sort_rec(A,p,r-1)
    Ins_Sort_rec(A,p,r)
    return A


def Ins_Sort_rec(A: list[int], p: int, r: int):
    key = A[r]
    j=r-1
    while j>-1 and key < A[j]:
        A[j+1] = A[j]
        j -= 1
    A[j+1] = key

    return A

print(Insertion_Sort_incr([5, 8, 6, 4]))
print(Insertion_Sort_decr([5, 8, 6, 4]))
print(ADD_Bin_int([1,1,0],[1,0,1]))
print(Insertion_Sort_rec([4,1,2,3],0,3))