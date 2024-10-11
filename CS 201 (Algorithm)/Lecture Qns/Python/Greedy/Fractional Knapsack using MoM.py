'''
-> Hint:- (by sir)
    -> check if upper half is all valid to be included
        -> then work on the lower half recursively
    -> else work recursively on upper half
'''
class Solution:
    def knapsack_fractional(self, weights, profits, capacity):
        n = len(weights)
        ratios = [(profits[i] / weights[i], weights[i], profits[i]) for i in range(n)]

        median_ratio = self.find_median_ratio(ratios)

        high_ratio_items = []
        low_ratio_items = []

        for ratio, weight, profit in ratios:
            if ratio >= median_ratio:
                high_ratio_items.append((ratio, weight, profit))
            else:
                low_ratio_items.append((ratio, weight, profit))

        high_ratio_items.sort(reverse=True, key=lambda x: x[0])
        low_ratio_items.sort(reverse=True, key=lambda x: x[0])

        total_profit = 0.0
        remaining_capacity = capacity

        for ratio, weight, profit in high_ratio_items:
            if remaining_capacity >= weight:
                total_profit += profit
                remaining_capacity -= weight
            else:
                total_profit += profit * (remaining_capacity / weight)
                break

        for ratio, weight, profit in low_ratio_items:
            if remaining_capacity >= weight:
                total_profit += profit
                remaining_capacity -= weight
            else:
                total_profit += profit * (remaining_capacity / weight)
                break

        return total_profit

    def find_median_ratio(self, items):
        ratios = [item[0] for item in items]
        median_index = len(ratios) // 2
        median_ratio = self.find_kth_smallest(ratios, median_index)
        return median_ratio

    def find_kth_smallest(self, nums, k):
        if len(nums) == 1:
            return nums[0]
        return self.partition(nums, 0, len(nums) - 1, k)

    def partition(self, nums, p, r, pos):
        if p >= r:
            return nums[p]
        pivot = self.find_pivot(nums, p, r)
        left, right = p, r
        i = p

        while i <= right:
            if nums[i] < pivot:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
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

    def find_pivot(self, nums, p, r):
        if r - p + 1 <= 5:
            nums = nums[p:r + 1]
            nums.sort()
            return nums[len(nums) // 2]

        medians = []
        for i in range(p, r + 1, 5):
            part = nums[i:min(i + 5, r + 1)]
            part.sort()
            medians.append(part[len(part) // 2])

        return self.find_kth_smallest(medians, len(medians) // 2)

class Solution_alt:
    def knapsack_fractional(self, weights, profits, capacity):
        n = len(weights)
        ratios = [(profits[i] / weights[i], weights[i], profits[i]) for i in range(n)]

        median_ratio = self.find_median_ratio(ratios)

        high_ratio_items = []
        low_ratio_items = []

        for ratio, weight, profit in ratios:
            if ratio >= median_ratio:
                high_ratio_items.append((ratio, weight, profit))
            else:
                low_ratio_items.append((ratio, weight, profit))

        if sum(x[1] for x in high_ratio_items) < capacity:
            return sum(x[2] for x in high_ratio_items) + self.knapsack_fractional([x[1] for x in low_ratio_items],[x[2] for x in low_ratio_items], capacity - sum(x[1] for x in high_ratio_items))

        elif sum(x[1] for x in high_ratio_items) > capacity:
            return self.knapsack_fractional([x[1] for x in high_ratio_items],[x[2] for x in high_ratio_items], capacity - sum(x[1] for x in high_ratio_items))

        else:
            return sum(x[2] for x in high_ratio_items)


    def find_median_ratio(self, items):
        ratios = [item[0] for item in items]
        median_index = len(ratios) // 2
        median_ratio = self.find_kth_smallest(ratios, median_index)
        return median_ratio

    def find_kth_smallest(self, nums, k):
        if len(nums) == 1:
            return nums[0]
        return self.partition(nums, 0, len(nums) - 1, k)

    def partition(self, nums, p, r, pos):
        if p >= r:
            return nums[p]
        pivot = self.find_pivot(nums, p, r)
        left, right = p, r
        i = p

        while i <= right:
            if nums[i] < pivot:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
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

    def find_pivot(self, nums, p, r):
        if r - p + 1 <= 5:
            nums = nums[p:r + 1]
            nums.sort()
            return nums[len(nums) // 2]

        medians = []
        for i in range(p, r + 1, 5):
            part = nums[i:min(i + 5, r + 1)]
            part.sort()
            medians.append(part[len(part) // 2])

        return self.find_kth_smallest(medians, len(medians) // 2)

# Example usage
weights = [2, 3, 4, 5]
profits = [40, 50, 60, 70]
capacity = 5

items8 = [[5000, 50], [10000, 70], [20000, 70]]
w = [50,70,70]
p = [5000,10000,20000]
c = 100

sol = Solution()
print(sol.knapsack_fractional(weights, profits, capacity))
print(sol.knapsack_fractional(w,p,c))

sol_alt = Solution_alt()
print(sol_alt.knapsack_fractional(weights,profits,capacity))
print(sol_alt.knapsack_fractional(w,p,c))
