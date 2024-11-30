class Solution:
    def minimumMountainRemovals(self, nums: list[int]) -> int:
        n = len(nums)

        LIS_len = [1] * n
        LDS_len = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    LIS_len[i] = max(LIS_len[i],LIS_len[j] + 1)

        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if nums[i] > nums[j]:
                    LDS_len[i] = max(LDS_len[i],LDS_len[j] + 1)

        min_rem = float('inf')
        for i in range(n):
            if LDS_len[i] > 1 and LIS_len[i] > 1:
                min_rem = min(min_rem,n - LIS_len[i] - LDS_len[i] + 1)

        return min_rem if min_rem != float('inf') else 0

sol = Solution()
print(sol.minimumMountainRemovals([1,3,3,1]))
print(sol.minimumMountainRemovals([1,3,2,3,1]))
print(sol.minimumMountainRemovals([1,5,7,7,9,9,2,1]))
print(sol.minimumMountainRemovals([1,5,2,1,1]))
