import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        if a > 0:
            max_heap.append([-a,'a'])
        if b > 0:
            max_heap.append([-b,'b'])
        if c > 0:
            max_heap.append([-c,'c'])

        heapq.heapify(max_heap)
        res = ""
        while max_heap:
            elem1 = heapq.heappop(max_heap)

            if len(res) >= 2 and res[-1] == res[-2] == elem1[1]:
                if not max_heap:
                    break

                elem2 = heapq.heappop(max_heap)
                res += elem2[1]
                if -elem2[0] > 1:
                    heapq.heappush(max_heap,[elem2[0] + 1,elem2[1]])

                heapq.heappush(max_heap,elem1)

            else:
                res += elem1[1]
                if -elem1[0] > 1:
                    heapq.heappush(max_heap,[elem1[0] + 1,elem1[1]])

        return res

sol = Solution()
print(sol.longestDiverseString(6,5,7))
print(sol.longestDiverseString(2,1,1))


