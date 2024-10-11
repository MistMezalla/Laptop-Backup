'''
-> Solve this qn after making ur hands dirty with backtracking
'''
import heapq
class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        if sum(nums)%k != 0:
            return False

        part_sum = sum(nums)//k
        parts = [part_sum]*k
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)

        while True:
            if len(max_heap) == 0:
                break
            elem = (-heapq.heappop(max_heap))%part_sum
            if elem == 0:
                elem  = part_sum

            for i in range(len(parts)):
                if elem <= parts[i]:
                    parts[i] -= elem
                    break

        if sum(parts) != 0:
            return False
        return True


sol = Solution()
print(sol.canPartitionKSubsets([4,3,2,3,5,2,1],4))
print(sol.canPartitionKSubsets([4,7,2,3,2,1,1],4))