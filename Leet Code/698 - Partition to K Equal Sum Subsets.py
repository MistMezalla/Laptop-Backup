'''
-> Solve this qn after making ur hands dirty with backtracking
'''
class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False

        nums.sort(reverse=True)
        visited = [0] * len(nums)

        part_sum = sum(nums)//k

        if nums[0] > part_sum:
            return False

        def gen_parts(rem,curr_sum,st):
            if rem == 0:
                return True

            if curr_sum == part_sum:
                return gen_parts(rem - 1,0,0)

            for i in range(st,len(nums)):
                if not visited[i] and curr_sum + nums[i] <= part_sum:
                    visited[i] = 1
                    if gen_parts(rem,curr_sum+nums[i],i+1):
                        return True
                    visited[i] = 0

            return False

        return gen_parts(k,0,0)

sol = Solution()
print(sol.canPartitionKSubsets([4,3,2,3,5,2,1],4))
print(sol.canPartitionKSubsets([4,7,2,3,2,1,1],4))