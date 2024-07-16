from collections import deque
stack = deque()

l = [4,5,2,25,7,8]

def NGE(arr):
    nge = [-1]*len(arr)
    for i in range(len(arr)):
        while (len(stack) != 0 and arr[i] >= arr[stack[-1]]):
            nge[stack[-1]] = arr[i]
            stack.pop()
        stack.append(i)

    return nge

print(NGE(l))