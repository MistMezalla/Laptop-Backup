class Solution:
    def partitionDisjoint(self, nums: list[int]) -> int:
        left = []
        right = []
        left_max = float('-inf')
        right_max = float('-inf')

        for num in nums:
            if len(left) == 0:
                left.append(num)
                left_max = num
                continue

            if num >= left_max:
                right.append(num)
                right_max = max(right_max,num)

            else:
                left.extend(right)
                left.append(num)
                right.clear()
                left_max = max(right_max,left_max)
                right_max = float('-inf')

        return len(left)

sol = Solution()
print(sol.partitionDisjoint([5,0,3,4,8,6]))
print(sol.partitionDisjoint([5,0,7,8,9,6]))
print(sol.partitionDisjoint([5,5]))
print(sol.partitionDisjoint([90,47,69,10,43,92,31,73,61,97]))
print(sol.partitionDisjoint([32,57,24,19,0,24,49,67,87,87]))

