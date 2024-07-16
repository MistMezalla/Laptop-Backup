def Counting_Sort(arr):
    count = [0] * (max(arr)+1)

    for num in arr:
        count[num] += 1

    pos = 0
    for i in range(len(count)):
        temp = count[i]
        count[i] = pos
        pos += temp



    res = [None for _ in range(len(arr))]
    for num in arr:
        res[count[num]] = num
        count[num] += 1

    return res

def Counting_Sort_alt(arr):
    count = [0] * (max(arr)+1)

    for num in arr:
        count[num] += 1

    for i in range(1,len(count)):
        count[i] += count[i-1]

    res = [None]*len(arr)
    for num in reversed(arr):
        res[count[num]-1] = num
        count[num]-=1

    return res
nums = [2,3,1,0,4,1,2,3,4]
print(Counting_Sort(nums))
print(Counting_Sort_alt(nums))



