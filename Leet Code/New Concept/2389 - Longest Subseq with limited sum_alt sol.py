'''
-> In the O(nlogn) solution used the concepts of:-
    -> Prefix Sum
    -> Binary Search
'''

class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        nums.sort()
        def bin_search(val):
            lo = 0
            hi = len(pre_sum) - 1

            while hi - lo > 1:
                mid = (hi + lo)//2

                if pre_sum[mid] <= val:
                    lo = mid
                else:
                    hi = mid - 1

            if pre_sum[hi] <= val:
                return hi
            elif pre_sum[lo] <= val:
                return lo
            else:
                return -1

        ans = []
        pre_sum = []
        curr_sum = 0
        for num in nums:
            curr_sum += num
            pre_sum.append(curr_sum)

        for query in queries:
            ind = bin_search(query)
            ans.append(ind + 1)

        return ans

sol = Solution()
print(sol.answerQueries([5,4,2,1],[3,10,21]))


