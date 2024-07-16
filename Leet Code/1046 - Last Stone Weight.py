from sortedcontainers import SortedList
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        map = SortedList()

        for elem in stones:
            map.add(elem)

        while len(map)>1:
            x = map[-1]
            y = map[-2]
            map.discard(x)
            map.discard(y)
            x=x-y
            map.add(x)

        return map[0]

sol = Solution()
print((sol.lastStoneWeight([2,8,3,5,2])))
print((sol.lastStoneWeight([10])))
print((sol.lastStoneWeight([2,7,4,1,8,1])))

