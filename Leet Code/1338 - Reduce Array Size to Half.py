import heapq
class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        hsh = {}

        for num in arr:
            if num not in hsh:
                hsh[num] = 1
            else:
                hsh[num] += 1

        max_heap = [-freq for num,freq in hsh.items()]

        heapq.heapify(max_heap)#,key = lambda x: x[1])

        n = len(arr)
        cnt = 0
        while n > len(arr)//2:
            n += heapq.heappop(max_heap)
            cnt += 1

        return cnt

sol = Solution()
print(sol.minSetSize([100,100,3,7]))
print(sol.minSetSize([0,1]))
print(sol.minSetSize([2,2]))
print(sol.minSetSize([3,3,3,3,5,5,5,2,2,7]))




