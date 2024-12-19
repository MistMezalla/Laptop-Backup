class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        banned = set(banned)

        temp_sum = 0
        cnt = 0
        for i in range(1,n+1):
            if i not in banned:
                cnt += 1
                temp_sum += i

            if temp_sum > maxSum:
                return cnt - 1

        return cnt

sol = Solution()
print(sol.maxCount(banned = [1,6,5], n = 5, maxSum = 6))
print(sol.maxCount(banned = [1,2,3,4,5,6,7], n = 8, maxSum = 1))
print(sol.maxCount(banned = [11], n = 7, maxSum = 50))
print(sol.maxCount([4],8,11))