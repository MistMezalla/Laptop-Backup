'''
-> My Code:-
    -> Well the code will work for cases when:-
        -> if the cnt of numbers is to be returned in correspondence to numbers when they are sorted
            -> In that case don't do hashing and other computation, simply return the sorted_num_cnt
        -> If numbers present in the i/p list are all unique
            -> coz the rel ordering of the same numbers is destroyed in the process

-> Below code:-
    -> Improves on the shortcomings of my implementation of rel ordering of same elem
'''

class og_num_ind():
    def __init__(self,val,index):
        self.val = val
        self.ind = index

class Solution:
    def countSmaller(self, nums):
        res = [0] * len(nums)

        num_ind = [og_num_ind(nums[i],i) for i in range(len(nums))]

        self.cnt_smaller(num_ind,0,len(num_ind)-1,res)

        return res
    def cnt_smaller(self,nums,left,right,res):
        if left>=right:
            return

        mid = (left + right)//2
        self.cnt_smaller(nums,left,mid,res)
        self.cnt_smaller(nums,mid+1,right,res)

        self.MnC(nums,left,mid,right,res)

    def MnC(self,nums,left,mid,right,res):
        temp_nums = []
        i = left
        j = mid + 1
        cnt = 0

        while i<=mid and j<=right:
            if nums[i].val > nums[j].val:
                temp_nums.append(nums[j])
                cnt+=1
                j+=1
            else:
                res[nums[i].ind] += cnt
                temp_nums.append(nums[i])
                i += 1

        while i <= mid:
            res[nums[i].ind] += cnt
            temp_nums.append(nums[i])
            i += 1

        while j<=right:
            temp_nums.append(nums[j])
            j += 1

        nums[left:right+1] = temp_nums

sol = Solution()
print(sol.countSmaller([5, 2, 6, 1]))  # Output: [2, 1, 1, 0]
print(sol.countSmaller([-1, -1])) # Output: [0, 0]
print(sol.countSmaller([5,2,5,1]))