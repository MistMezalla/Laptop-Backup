'''
-> My sol:-
    -> T(n) = O(n)
    -> S(n) = O(n)

-> Below sol:-
    -> T(n) = O(n)
    -> S(n) = O(n)

-> My implementation is slow as accessing elem a lot of times
    -> though accessing is O(1) but still has some memory overhead
-> Below sol minimises the freq of access hence optimal in terms of runtime
'''

class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        val_to_rank = {}

        sorted_unique_num = sorted(set(arr))

        for ind,num in enumerate(sorted_unique_num):
            val_to_rank[num] = ind + 1

        for i,num in enumerate(arr):
            arr[i] = val_to_rank[num]

        return arr

sol = Solution()
print(sol.arrayRankTransform([40,20,30,30]))
