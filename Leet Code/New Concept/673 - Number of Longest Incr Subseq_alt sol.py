'''
-> First learn dp to solve such problems
-> Secondly, we are asked to find incr subseq and not 'conti' incr subseq
'''

'''
Revise = 2
Resolve = 1
'''
class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        lengths = [1]*n
        cnt = [1]*n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        cnt[i] = cnt[j]
                    elif lengths[j] + 1 == lengths[i]:
                        cnt[i] += cnt[j]

        longest = max(lengths)

        return sum(cnt[i] for i in range(n) if lengths[i] == longest)

sol = Solution()
print(sol.findNumberOfLIS([2,6,8,3,5,7]))
print(sol.findNumberOfLIS([7,7,7,7,7,7]))
print(sol.findNumberOfLIS([1,3,5,4,7]))
print(sol.findNumberOfLIS([3,23,25,5,7,27,8,9,10]))
print(sol.findNumberOfLIS([10,20,11,21,24,12,14,27,17,29,18,19]))
print(sol.findNumberOfLIS([2,1,3,9,7,8]))
