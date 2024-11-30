'''
-> Rec rel:-
    -> dp[i] += dp[i-coin]
        -> dp[i] : stores the number of ways to reach the sum i with given denomination of coins

-> Why rec rel is correct:-
    -> if we know the # ways for sum 'i-coin' then
        -> add the # ways of 'i-coin'(dp[i-coin]) to dp[i] as current coin is an additional way to the sum 'i'
        -> alternatively, the prev ways(sub problems) of summation of some 'i' is eff being used in the abv rec rel
            -> Ex: 2 = 2
                     = 1 1
               This abv number ways can be reused by the means of rec rel for say while computing 5.
'''


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin,amount + 1):
                dp[i] += dp[i-coin]

        return dp[amount]


