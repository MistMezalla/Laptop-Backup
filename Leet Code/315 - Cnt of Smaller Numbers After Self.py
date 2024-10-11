# The Below sol will work if the number in the i/p list are all unique
class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        hsh_num_index = {}
        for ind,num in enumerate(nums):
            hsh_num_index[num] = ind

        res = [0] * len(nums)
        sorted_num_cnt = self.cnt_smaller(nums,0,len(nums)-1)

        for ind,num in enumerate(nums):
            res[hsh_num_index[num]] = sorted_num_cnt[ind]
        return res


    def cnt_smaller(self,nums,left,right):
        if left>= right:
            return [0]

        mid = (left + right)//2

        left_cnt = self.cnt_smaller(nums,left,mid)
        right_cnt = self.cnt_smaller(nums,mid+1,right)
        left_cnt.extend(right_cnt)

        return self.MnC(nums,left,mid,right,left_cnt)

    def MnC(self,nums,left,mid,right,cnt):
        temp_nums = []
        temp_cnt = []
        j = mid + 1

        for i in range(left,mid+1):
            while j <= right and nums[i] > nums[j]:
                j+=1
            cnt[i - left] += j - (mid + 1)

        i = left
        j= mid + 1
        while i <= mid and j<= right:
            if nums[i] < nums[j]:
                temp_nums.append(nums[i])
                temp_cnt.append(cnt[i-left])
                i+=1
            else:
                temp_nums.append(nums[j])
                temp_cnt.append(cnt[j-left])
                j+=1

        if i <= mid:
            temp_nums.extend(nums[i:mid+1])
            temp_cnt.extend(cnt[i-left:mid+1-left])

        if j <= right:
            temp_nums.extend(nums[j:right+1])
            temp_cnt.extend(cnt[j-left:right+1-left])

        nums[left:right+1] = temp_nums
        cnt[left-left:right+1-left] = temp_cnt

        return cnt

sol = Solution()
print(sol.countSmaller([5,2,6,1]))
print(sol.countSmaller([-1,-1]))
print(sol.countSmaller([5,2,5,1]))
#print(sol.countSmaller([26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41]))

