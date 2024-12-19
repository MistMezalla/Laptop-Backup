from collections import deque
class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        stack = deque()

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                prices[stack.pop()] -= prices[i]
            stack.append(i)

        return prices

sol = Solution()
print(sol.finalPrices([8,4,6,2,3]))

