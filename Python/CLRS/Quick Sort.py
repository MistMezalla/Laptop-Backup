def CLRS():
    def Quick_Sort(arr: list[int],p: int,r: int):
        if p>r:
            return
        q=Partition(arr,p,r)
        Quick_Sort(arr,p,q-1)
        Quick_Sort(arr,q+1,r)
        return arr


    def Partition(arr: list[int],p: int,r: int):
        x = arr[r]
        i = p-1
        j = p
        while j<=r-1:
            if arr[j]<=x:
                i+=1
                arr[i],arr[j]=arr[j],arr[i]
            j+=1
        arr[i+1],arr[r]=arr[r],arr[i+1]

        return i+1

    l = [3,4,2,1,7,6,8,12]
    Quick_Sort(l,0,len(l)-1)
    print(l)

