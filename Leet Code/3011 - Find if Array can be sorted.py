class Solution:
    def canSortArray(self, nums: list[int]) -> bool:
        grp_min_max = []
        curr_min = nums[0]
        curr_max = nums[0]
        grp_bit_cnt = self.set_bit_counter(nums[0])
        for num in nums:
            curr_bit_cnt = self.set_bit_counter(num)

            if curr_bit_cnt == grp_bit_cnt:
                curr_min = min(curr_min,num)
                curr_max = max(curr_max,num)

            elif curr_bit_cnt != grp_bit_cnt:
                grp_min_max.append((curr_min,curr_max))
                curr_min = num
                curr_max = num
                grp_bit_cnt = curr_bit_cnt

        grp_min_max.append((curr_min,curr_max))

        for i in range(len(grp_min_max)-1):
            if grp_min_max[i][1] > grp_min_max[i+1][0]:
                return False

        return True

    def set_bit_counter(self, n: int) -> int:
        return bin(n).count('1')


# Test cases
sol = Solution()
print(sol.canSortArray([2,8,4,16,17,20,30,29]))
print(sol.canSortArray([8,4,2,30,15]))
print(sol.canSortArray([1,2,3,4,5]))
print(sol.canSortArray([3,16,8,4,2]))
print(sol.canSortArray([2,8,4,16,3,17,48,9]))