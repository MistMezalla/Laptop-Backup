'''
-> Absolutely valid sol(verified by sir)
'''
class Solution:
    def kth_closest_to_median(self, nums: list[int], k: int):
        median = self.find_median(nums)
        # Create an array of absolute differences from the median
        diff = [(abs(num - median), num) for num in nums]
        # Apply scaling to handle float values in counting sort
        diff = self.Counting_Sort(diff)
        # Extract the k closest numbers
        return [num for _, num in diff[:k]]

    def find_median(self, nums: list[int]):
        n = len(nums)
        if n & 1:
            # Odd length, return the middle element
            return self.partition(nums, 0, n - 1, n // 2)
        else:
            # Even length, return the average of the two middle elements
            median1 = self.partition(nums, 0, n - 1, n // 2 - 1)
            median2 = self.partition(nums, 0, n - 1, n // 2)
            return (median1 + median2) / 2

    def partition(self, nums: list[int], p: int, r: int, pos: int):
        if p == r:
            return nums[p]
        pivot = self.find_pivot(nums, p, r)
        left = p
        right = r
        i = p

        while i <= right:
            if nums[i] < pivot:
                nums[left], nums[i] = nums[i], nums[left]
                i += 1
                left += 1
            elif nums[i] > pivot:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            else:
                i += 1

        if pos < left:
            return self.partition(nums, p, left - 1, pos)
        elif pos > right:
            return self.partition(nums, right + 1, r, pos)
        else:
            return nums[pos]

    def find_pivot(self, nums: list[int], p: int, r: int):
        if r - p + 1 <= 5:
            nums = nums[p:r + 1]
            nums.sort()
            return nums[len(nums) // 2]

        medians = []
        for i in range(p, r + 1, 5):
            part = nums[i:min(i + 5, r + 1)]
            part.sort()
            medians.append(part[len(part) // 2])

        return self.find_pivot(medians, 0, len(medians) - 1)

    def Counting_Sort(self, nums):
        # Determine scaling factor for floating-point numbers
        scaling_factor = 10000  # Assuming up to 4 decimal places

        # Convert to scaled integer values
        scaled_nums = [(int(val[0] * scaling_factor), val[1]) for val in nums]

        max_elem = max(scaled_nums, key=lambda x: x[0])[0]
        min_elem = min(scaled_nums, key=lambda x: x[0])[0]

        count = [0] * (max_elem - min_elem + 1)

        for num in scaled_nums:
            count[num[0] - min_elem] += 1

        pos = 0
        for i in range(len(count)):
            temp = count[i]
            count[i] = pos
            pos += temp

        res = [None] * len(nums)
        for num in scaled_nums:
            res[count[num[0] - min_elem]] = num
            count[num[0] - min_elem] += 1

        # Convert back to original scale
        return [(val[0] / scaling_factor, val[1]) for val in res]

# Example usage
sol = Solution()
print(sol.kth_closest_to_median([1,1,1,1,1,1,1,1,1,1], 7))
print(sol.kth_closest_to_median([3,6,1,4,9,2,8,10,7], 6))
