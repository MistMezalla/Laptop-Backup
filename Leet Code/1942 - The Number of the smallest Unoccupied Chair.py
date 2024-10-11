import heapq
class Solution:
    def smallestChair(self, times: list[list[int]], targetFriend: int) -> int:
        min_heap = []
        hash_friend_number = {}
        for i,time in enumerate(times):
            hash_friend_number[time[0]] = i

        times.sort(key = lambda x: x[0])
        curr_chr = -1
        min_chr_avl = list(range(len(times)))
        heapq.heapify(min_chr_avl)
        for st,end in times:
            while min_heap and min_heap[0][0] <= st:
                temp_chr = heapq.heappop(min_heap)[1]
                heapq.heappush(min_chr_avl,temp_chr)

            curr_chr = heapq.heappop(min_chr_avl)
            heapq.heappush(min_heap,(end,curr_chr))

            if hash_friend_number[st] == targetFriend:
                return curr_chr

sol = Solution()
print(sol.smallestChair(times = [[1,4],[2,3],[4,6]], targetFriend = 1))
print(sol.smallestChair(times = [[3,10],[1,5],[2,6]], targetFriend = 0))
print(sol.smallestChair([[7,10],[1,5],[2,8]],0))
print(sol.smallestChair([[33889,98676],[80071,89737],[44118,52565],[52992,84310],[78492,88209],[21695,67063],[84622,95452],[98048,98856],[98411,99433],[55333,56548],[65375,88566],[55011,62821],[48548,48656],[87396,94825],[55273,81868],[75629,91467]],6))

print(sol.smallestChair([[4,9],[3,10],[1,5],[6,7],[8,11],[7,12]],4))
print(sol.smallestChair([[3,10],[4,5],[1,7],[8,9],[9,11],[10,12]],3))



