import heapq
class Solution:
    def halveArray(self, nums: list[int]) -> int:
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)

        target = sum(nums)/2
        op = 0
        while target>0:
            elem = -heapq.heappop(max_heap) / 2
            target -= elem
            heapq.heappush(max_heap,-elem)
            op += 1

        return op

sol = Solution()
print(sol.halveArray(nums = [5,19,8,1]))
print(sol.halveArray(nums = [3,8,20]))
print(sol.halveArray([100]))




