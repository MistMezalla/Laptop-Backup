'''
-> My Intuition:-
    -> well took into acc all possible constraints except
        -> by my approach i assigned the min diff to bricks by def
        -> hence these min diff are not obliged to occur at very start and there my arise the case where ladders have
        finished but due to abundance of bricks will have to opt for diff which is not avl in set to moe forward
        -> hence my sol can produce under val in such cases

-> Below Intuition:-
    -> For diff that are +ve
        -> we use brick by def if suff
        -> if bricks not suff
            -> we see if heap is empty and top of max heap replaceable by curr diff thereby swapping ladder for this
            movement with brick used for min heap top
            -> if abv case fails then no choice but to use ladder
            -> if ladder finished then break
'''
import heapq


class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        max_heap = []

        i = 0
        while i < len(heights) - 1:
            diff = heights[i+1] - heights[i]

            if diff > 0:
                if bricks >= diff:
                    bricks -= diff
                    heapq.heappush(max_heap,-diff)
                elif ladders > 0:
                    if max_heap and -max_heap[0] > diff:
                        bricks += -heapq.heappop(max_heap) - diff
                        heapq.heappush(max_heap,-diff)
                    ladders-=1
                else:
                    break
            i+=1

        return i

sol = Solution()
print(sol.furthestBuilding(heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1))
print(sol.furthestBuilding( heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2))
print(sol.furthestBuilding(heights = [14,3,19,3], bricks = 17, ladders = 0))
print(sol.furthestBuilding(heights = [1, 5, 1], bricks = 3, ladders = 0))
print(sol.furthestBuilding(heights = [253710, 459585, 71981, 223232, 977918, 148680, 123527, 250812, 260416, 554767],bricks = 3367,ladders = 3
))
print(sol.furthestBuilding([1,6,14,15],bricks=5,ladders=1))