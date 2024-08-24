class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices and len(prices) < 2:
            return 0

        min_prices = prices[0]
        max_profit = 0

        for i in range(1,len(prices)):
            curr_profit = prices[i] - min_prices
            if curr_profit >= max_profit:
                max_profit = curr_profit

            if prices[i] <= min_prices:
                min_prices = prices[i]

        return max_profit


