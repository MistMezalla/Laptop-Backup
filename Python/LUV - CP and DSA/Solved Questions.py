def EP_14(nums: list[int],l: int, r: int):
    nums[l:r+1]=[]

    from math import gcd

    gc = gcd(nums[0],nums[1])

    for i in range (len(nums)):
        gc = gcd(nums[i], gc)

    return gc

def EP_14_precomputation(nums: list[int],l: int, r: int):
    from math import gcd

    gcd_forward = []
    gcd_forward.append(0)
    for i in range(1,len(nums)):
        gcd_forward.append(gcd(nums[i-1],gcd_forward[i-1]))

    print(gcd_forward)

    gcd_backwards=[]
    #gcd_backwards.append(0)
    '''
    if backwards gcd array is built as done in case of c++ then formation will be of O(n**2). hence not possible 
    '''
    for i in range (len(nums)+1):
        gcd_backwards.append(0)

    for i in range(len(nums) - 1,0,-1):
        gcd_backwards[i]=gcd(nums[i],gcd_backwards[i+1])

    print(gcd_backwards)

    return (gcd(gcd_forward[l-1],gcd_backwards[r+1]))

def EP_15(n: int,m: int):
    arr = []
    for i in range(n+10):
        arr.append(0)

    print()
    for i in range(m):
        a, b, k = map(int, input().split())

        arr[a-1]+=k
        arr[b+1]-=k

    pf = []
    for i in range(0,n+1):
        pf.append(0)
    for i in range(1,n+1):
        pf[i]=pf[i-1]+arr[i]

    return max(pf)

def EP_16(t: int):
    while t:
        N,Q = map(int,input().split())
        st = input()
        t-=1

        arr = [[] for _ in range(26)]
        for i in range(26):
            for j in range(N+1):
                arr[i].append(0)


        for i in range(1,N+1):
            arr[ord(st[i-1])-ord('a')][i]+=1

        for i in range(26):
            for j in range(1,N+1):
                arr[i][j]+=arr[i][j-1]

        while Q:
            Q-=1
            l,r = map(int,input().split())
            print(st[l:r+1])

            oddcnt=0
            flag=1
            for i in range(26):
                if oddcnt>1:
                    flag=0
                    break
                #print(arr[i][r],arr[i][l-1])
                if (arr[i][r]-arr[i][l-1])%2 != 0:
                    oddcnt+=1

            if not flag:
                print(False)
            else:
                print(True)



#print(EP_14([12,9,4,5,7,69,6],2,4))
#print(EP_14_precomputation([36,6,18,4,8,12,14],2,4))
#print(EP_15(5,3))
print(EP_16(1))

