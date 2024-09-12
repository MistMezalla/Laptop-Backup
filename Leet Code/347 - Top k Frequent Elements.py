class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hsh = dict()

        for num in nums:
            if num not in hsh:
                hsh[num] = 1
            else:
                hsh[num] += 1

        res = list(hsh.items())
        # for key,val in hsh:
        #     res.append((key,val))
        #
        res.sort(key = lambda x: x[1],reverse = True)

        return [res[i][0] for i in range(k)]

sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,2,2,2,2,2,3,3,3,3,3],2))


