def Selection_Sort(A: list[int]):
    for i in range(len(A)-1):
        min_pos = i
        for j in range(i+1, len(A)):
            if A[min_pos] >= A[j]:
                min_pos = j

        temp = A[i]
        A[i] = A[min_pos]
        A[min_pos] = temp

    return A

def Sel_Sort(A: list[[int]]):
    for i in range(len(A)-1):
        m = min(A[i:len(A)])
        A.remove(m)
        A.insert(i, m)

    return A

print(Selection_Sort([2,6,8,4]))
print(Sel_Sort([3,4,1,2]))