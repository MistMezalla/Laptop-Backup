import heapq
class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        hsh = {}

        for ind, sc in enumerate(score):
            hsh[sc] = ind

        # Create a max heap by negating the values
        max_heap = [-x for x in score]
        heapq.heapify(max_heap)

        res = [""] * len(score)
        rank = 1
        while max_heap:
            actual_score = -heapq.heappop(max_heap)

            if rank == 1:
                res[hsh[actual_score]] = "Gold Medal"
            elif rank == 2:
                res[hsh[actual_score]] = "Silver Medal"
            elif rank == 3:
                res[hsh[actual_score]] = "Bronze Medal"
            else:
                res[hsh[actual_score]] = str(rank)

            rank += 1

        return res

sol = Solution()
print(sol.findRelativeRanks([10]))
