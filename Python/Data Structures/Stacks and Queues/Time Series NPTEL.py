from collections import deque
def Time_Series(arr):
    stack = deque()
    TS=[]

    for i in range(len(arr)):
        done = False
        h=0
        while not (len(stack)==0 or done):
            if arr[i]>=arr[stack[-1]]:
                stack.pop()
            else:
                done = True

        if len(stack) == 0:
            h=0
        else:
            h=stack[-1]

        TS.append(i-h-1 if i-h-1>=0 else 0)
        stack.append(i)

    return TS


l = [7,5,6,8,3]
print(Time_Series(l))

