'''
-> To check the need to merge the pf_sum in the sorted order
'''
class Solution:
    def countRangeSum(self, nums: list[int], lower: int, upper: int) -> int:
        # Prefix sum array
        pf_sum = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            pf_sum[i] = pf_sum[i - 1] + nums[i - 1]

        # Call the divide and conquer function
        return self.DnC_cnt(pf_sum, 0, len(nums) + 1, lower, upper)

    def DnC_cnt(self, pf_sum: list[int], left: int, right: int, lower: int, upper: int) -> int:
        # If there's one or fewer elements, no range sums are possible
        if right - left <= 1:
            return 0

        # Midpoint for dividing the array
        mid = (left + right) // 2

        # Recursive counts in both halves
        count = self.DnC_cnt(pf_sum, left, mid, lower, upper) + self.DnC_cnt(pf_sum, mid, right, lower, upper)

        # Count the valid range sums that cross the midpoint
        j = k = mid
        for i in range(left, mid):
            # Find how many sums in the right half are within [lower, upper]
            while j < right and pf_sum[j] - pf_sum[i] < lower:
                j += 1
            while k < right and pf_sum[k] - pf_sum[i] <= upper:
                k += 1
            count += k - j

        # Merge the two halves while keeping the prefix sum sorted
        merged = []
        l, r = left, mid
        while l < mid and r < right:
            if pf_sum[l] <= pf_sum[r]:
                merged.append(pf_sum[l])
                l += 1
            else:
                merged.append(pf_sum[r])
                r += 1
        merged.extend(pf_sum[l:mid])
        merged.extend(pf_sum[r:right])

        # Update the original array with the merged result
        pf_sum[left:right] = merged

        return count

# Test cases
sol = Solution()
print(sol.countRangeSum([-2, 5, -1], -2, 2))  # Expected output: 3
print(sol.countRangeSum([-2, 5, -3, 1, 0], -3, 3))
print(sol.countRangeSum([5,-2, -3, 1, 0], -3, 3))# Expected output: 5
