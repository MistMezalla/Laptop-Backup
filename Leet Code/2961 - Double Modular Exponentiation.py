class Solution:
    def getGoodIndices(self, variables: list[list[int]], target: int) -> list[int]:
        good = []
        for ind,values in enumerate(variables):
            ans = pow(pow(values[0],values[1])%10,values[2])%values[3]
            if ans == target:
                good.append(ind)

        return good

sol = Solution()
print(sol.getGoodIndices([[2,3,3,10],[3,3,3,1],[6,1,1,4]],2))
print(sol.getGoodIndices([[39,3,1000,1000]],17))