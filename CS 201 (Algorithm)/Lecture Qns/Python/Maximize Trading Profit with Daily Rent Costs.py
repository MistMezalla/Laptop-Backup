class Solution():
    def Max_profit(self,prices: list[int],rent: int)->int:
        if not prices and len(prices) < 2:
            return 0

        min_prices = prices[0]
        max_profit = 0
        min_price_day = 0

        for i in range(1,len(prices)):
            curr_profit = prices[i] - min_prices - rent*(i-min_price_day)
            if curr_profit >= max_profit:
                max_profit = curr_profit

            if (prices[i] <= min_prices):
                min_prices = prices[i]
                min_price_day = i

        return max_profit

sol = Solution()
print(sol.Max_profit([70, 100, 140, 40, 60, 90, 120, 30, 60],15))
print(sol.Max_profit([100, 90, 80, 70, 60],5))
print(sol.Max_profit([50, 55, 60, 65, 70],2))
print(sol.Max_profit([70, 120, 80, 40, 90, 130],10))
print(sol.Max_profit([200, 180, 160, 120, 140, 300],20))
print(sol.Max_profit([10, 20, 30, 40, 50],1))
print(sol.Max_profit([100, 150, 80, 200, 300],20))
print(sol.Max_profit([100, 180, 260, 310, 40, 535, 695],50))
