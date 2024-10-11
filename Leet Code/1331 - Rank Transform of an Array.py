class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        if not arr:
            return []

        hash_tuple = [(num,ind) for ind,num in enumerate(arr)]
        hash_tuple.sort(key = lambda x: x[0])

        rank = [0] * len(arr)
        r = 1
        for i in range(len(hash_tuple)-1):
            if hash_tuple[i][0] != hash_tuple[i+1][0]:
                rank[hash_tuple[i][1]] = r
                r+=1
            else:
                rank[hash_tuple[i][1]] = r

        rank[hash_tuple[-1][1]] = r

        return rank

sol = Solution()
print(sol.arrayRankTransform([40,20,30,30]))


