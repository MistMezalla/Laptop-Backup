def is_suff_wood(h: int,arr,wood_req):
    wood = 0
    for i in range(len(arr)):
        if arr[i] >= h:
            wood += arr[i] - h

    print(wood>=wood_req)
    return wood>=wood_req

def EKO(wood_req,arr):
    lo = 0
    hi = 10e8

    while (hi - lo)>1:
        mid = (hi+lo)//2

        if is_suff_wood(mid,arr,wood_req):
            lo = mid
        else:
            hi = mid - 1

    if is_suff_wood(hi,arr,wood_req):
        return hi
    else:
        return lo

trees = [15,17,10,20]
print(EKO(7,trees))
