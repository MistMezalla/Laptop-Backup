'''
-> O(n**2) code
-> Optimal code of O(nlogn)
'''

class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        nums.sort()
        ans = []
        for query in queries:
            curr_sum = 0
            subseq_len = 0
            found = False
            for num in nums:
                if curr_sum + num > query:
                    ans.append(subseq_len)
                    found = True
                    break
                else:
                    curr_sum += num
                    subseq_len += 1

            if not found and curr_sum <= query:
                ans.append(subseq_len)


        return ans

sol = Solution()
print(sol.answerQueries([4,5,2,1],[3,10,21]))
print(sol.answerQueries([2,3,4,5],[1]))

