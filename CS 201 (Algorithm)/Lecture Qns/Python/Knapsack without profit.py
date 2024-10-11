class Solution():
    def knapscak_without_profit_bottom_up(self,sizes,limit):
        # the below method creates references of (limit+1) times where ref are made of [-1]*len(sizes)
        #memo = [[-1]*(len(sizes))]*(limit+1)
        memo = [[-1]*len(sizes) for _ in range(limit+1)]

        for i in range(len(memo)):
            memo[i][-1] = sizes[-1] if sizes[-1] <= i else 0

        for j in range(len(memo[0]) - 2,-1,-1):
            for i in range(len(memo)):
                res1 = 0
                res2 = memo[i][j+1]
                if i >= sizes[j]:
                    res1 = memo[i-sizes[j]][j+1] + sizes[j]

                memo[i][j] = max(res2,res1)

        return memo[limit][0]

    def knapsack_without_profit_top_down(self,sizes,limit):
        memo = [[-1]*len(sizes) for _ in range(limit+1)]

        def rec_helper(lim,st):
            if st == len(sizes) or lim == 0:
                return 0

            elif memo[lim][st] != - 1:
                return memo[lim][st]

            else:
                res1 = 0
                res2 = rec_helper(lim,st+1)
                if lim>=sizes[st]:
                    res1 = rec_helper(lim - sizes[st],st+1) + sizes[st]

                memo[lim][st] = max(res1,res2)

                return memo[lim][st]

        return rec_helper(limit,0)
        #return memo[limit][0]

sol = Solution()
print(sol.knapscak_without_profit_bottom_up([1,3,5,4],8))
print(sol.knapsack_without_profit_top_down([1,3,5,4],8))

