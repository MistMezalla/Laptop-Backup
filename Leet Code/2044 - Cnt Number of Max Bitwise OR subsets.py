class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        val = 0
        cnt = 0

        def gen_subsets(st,subset):
            nonlocal val, cnt  # Declaring nonlocal variables to modify outer scope variables
            curr_val = 0
            for i in range(len(subset)):
                curr_val |= subset[i]

            if curr_val > val:
                val = curr_val
                cnt = 1
            elif curr_val == val:
                cnt += 1

            for i in range(st,len(nums)):
                subset.append(nums[i])
                gen_subsets(i+1,subset)
                subset.pop()

        gen_subsets(0,[])
        return cnt

sol = Solution()
print(sol.countMaxOrSubsets([3,1]))

