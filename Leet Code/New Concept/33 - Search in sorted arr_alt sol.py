'''
-> The optimal sol is O(logn)
-> Intuition:-
    -> Search for ascending sorted arr(sub arr)
    -> check if that sub arr has the target value to be found
    -> If not check other half; hence solve by bin search
'''

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lo,hi = 0,len(nums)-1

        while hi - lo >1:
            mid = (hi+lo)//2

            if nums[mid] == target:
                return mid
            elif nums[mid]>=nums[lo]:
                if nums[lo]<=target<=nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid]<=target<=nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        if nums[lo] == target:
            return lo
        if nums[hi] == target:
            return hi
        else:
            return -1

