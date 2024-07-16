def Binary_Search(A: list[int], x: int):
    beg = 0
    end = len(A) - 1

    while beg <= end:
        mid = (beg+end) // 2

        if A[mid] == x:
            return x
        else:
            if A[mid] < x:
                beg = mid + 1
            else:
                end = mid - 1
    return None


print(Binary_Search([1,2,3,4,5,6,7,8,9],0))