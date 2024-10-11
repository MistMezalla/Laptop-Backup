'''
-> Question Conditions:-
    -> The question is to find the max and min in O(1.5n - 2) time
-> Intuition (by Sir)
    -> pairwise cmp
    -> lost the cmp to be added to reduce size of min search
'''

class My_Solution():
    def find_Min_Max(self,arr: list[int]):
        min_arr = []
        for i in range(len(arr),2):
            if i+1 >= len(arr):
                print("hi")
            else:
                if arr[i] <= arr[i+1]:
                    min_arr.append(arr[i])
                else:
                    min_arr.append(arr[i+1])

'''
-> My Solution was not of any use 
-> too derailing
'''
'''
Revised = 1
Resolved = 0
'''
class Solution():
    def find_min_max(self,arr: list[int]):
        max_arr,min_arr = None,None
        n = len(arr)

        if n & 1 : # odd
            max_arr,min_arr = arr[0],arr[0]
            i = 1
        else:
            if arr[0] <= arr[1]:
                max_arr = arr[1]
                min_arr = arr[0]
            else:
                max_arr,min_arr = arr[0],arr[1]
            i = 2

        while i < n-1:
            if arr[i] <= arr[i+1]:
                curr_min = arr[i]
                curr_max = arr[i+1]
            else:
                curr_min = arr[i+1]
                curr_max = arr[i]

            if curr_min <= min_arr:
                min_arr = curr_min

            if curr_max >= max_arr:
                max_arr = curr_max

            i+=2

        return max_arr,min_arr

sol = Solution()
print(sol.find_min_max([8,3,2,1,6,9,10]))