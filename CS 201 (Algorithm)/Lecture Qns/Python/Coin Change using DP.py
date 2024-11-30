#Note:-
'''
-> Well all the dp's are not of 2D form
-> In this case of 2D approach is failure as:-
    -> As we are not interested in prev states
    -> Moreover new states have to be overridden with prev states so as to have min coins(where sum is max)
        -> example :- for coins[5,4] and target 9 => number of coins = 1(for only 5) : wrong ans
                                                  => number of coins = 2(for both 4 and 5) : right ans
'''
class My_Solution:
    def coin_change_bottom_up(self,coins,target):
        dp = [[-1]*len(coins) for _ in range(target + 1)]

        for i in range(target + 1):
            dp[i][0] = i//coins[0]

        for j in range(1,len(coins)):
            for i in range(target+1):
                res1 = float('inf')
                res2 = dp[i][j-1]
                # res3 = i // coins[j]
                if i >= coins[j]:
                    res1 = dp[i-coins[j]][j-1] + 1
                dp[i][j] = min(res1,res2)
                if i%coins[j] == 0:
                    dp[i][j] = min(dp[i][j],i//coins[j])


        return dp[target][-1]
    

sol = My_Solution()
print(sol.coin_change_bottom_up([1,6,4],8))
print(sol.coin_change_bottom_up([1,3,4],9))
print(sol.coin_change_bottom_up(coins = [2, 4] ,target = 7))
print(sol.coin_change_bottom_up([3],10))
print(sol.coin_change_bottom_up([5,10,5],4))


class Solution:
    def coin_change_bottom_up(self,coins,target):
        dp = [float('inf') for _ in range(target + 1)]
        dp[0] = 0

        for coin in coins:
            for i in range(coin,target+1):
                dp[i] = min(dp[i],dp[i-coin]+1)

        return dp[target] if dp[target] != float('inf') else -1

sol = Solution()
print(sol.coin_change_bottom_up([1,6,4],8))
print(sol.coin_change_bottom_up([1,3,4],9))
print(sol.coin_change_bottom_up(coins = [2, 4] ,target = 7))
print(sol.coin_change_bottom_up([3],10))
print(sol.coin_change_bottom_up([5,10,5],4))