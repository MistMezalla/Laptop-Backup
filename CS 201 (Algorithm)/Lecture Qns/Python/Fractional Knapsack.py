class Solution:
    def fractional_knapsack(self, items, capacity):
        items.sort(key=lambda x: x[0] / x[1], reverse=True)
        total_profit = 0
        for profit, size in items:
            if capacity >= size:
                total_profit += profit
                capacity -= size
            else:
                partial_part = profit * (capacity / size)
                total_profit += partial_part
                break
        return total_profit

sol = Solution()

items1 = [(60, 10), (100, 20), (120, 30)]
print(sol.fractional_knapsack(items1, 50))

items2 = [[50, 5], [80, 10], [90, 15]]
print(sol.fractional_knapsack(items2,30))

items3 = [[50, 5], [80, 10], [90, 15]]
print(sol.fractional_knapsack(items3,0))

items4 = [[70, 10]]
print(sol.fractional_knapsack(items4 , 10))

items5 = [[100, 50]]
print(sol.fractional_knapsack(items5,10))

items6 = []
print(sol.fractional_knapsack(items6,50))

items7 = [[100, 50], [200, 60]]
print(sol.fractional_knapsack(items7,30))

items8 = [[5000, 50], [10000, 70], [20000, 70]]
print(sol.fractional_knapsack(items8,100))
