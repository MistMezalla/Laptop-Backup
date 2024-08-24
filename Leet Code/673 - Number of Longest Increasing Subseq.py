class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        seq = [nums[0]]
        num_seq = 0

        def bin_search(x):
            lo = 0
            hi = len(nums) - 1

            while hi - lo > 1:
                mid = (hi + lo) // 2

                if nums[mid] >= x:
                    hi = mid
                else:
                    lo = mid + 1

            if nums[lo] >= x:
                return lo
            else:
                return hi

        new_seq = False
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                seq.append(nums[i])
                new_seq = False
            else:
                seq[bin_search(nums[i])] = nums[i]

                if not new_seq:
                    new_seq = True
                    num_seq += 1

        return num_seq + 1

sol = Solution()
print(sol.findNumberOfLIS([2,6,8,3,5,7]))
print(sol.findNumberOfLIS([7,7,7,7,7,7]))
print(sol.findNumberOfLIS([1,3,5,4,7]))
print(sol.findNumberOfLIS([3,23,25,5,7,27,8,9,10]))
print(sol.findNumberOfLIS([10,20,11,21,24,12,14,27,17,29,18,19]))
print(sol.findNumberOfLIS([2,1,3,9,7,8]))