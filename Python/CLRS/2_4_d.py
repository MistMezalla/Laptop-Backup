def cnt_inversions(A: list[int]):
     arr = A

     if len(arr)<2:
         return arr,0

     mid = len(arr)//2

     left, left_inv = cnt_inversions(arr[:mid])
     right, right_inv = cnt_inversions(arr[mid:])
     merged, split_inv = merge(left,right)

     return merged,left_inv + right_inv + split_inv

def merge(left: list[int], right: list[int]):
    i=j=0
    merged = []
    split_inv = 0

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            split_inv += len(left) - i
            j+=1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, split_inv

arr = [2, 7, 4, 6, 5]
sorted_arr, inversion_count = cnt_inversions(arr[1:5])
print("Sorted subarray:", sorted_arr)
print("Inversion count:", inversion_count)

