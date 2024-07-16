def Bubble_Sort(num: list[int]):
    swap = 1
    for i in range(len(num)-1):
        if(swap):
            swap = 0
            for j in range(len(num)-1,i,-1):
                if num[j] < num[j-1]:
                    num[j],num[j-1]=num[j-1],num[j]
                    swap = 1

    return num

print(Bubble_Sort([1,2,3,4,5]))