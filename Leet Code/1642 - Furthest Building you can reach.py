import heapq
class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        consecutive_dist = []

        for i in range(1,len(heights)):
            if heights[i] - heights[i - 1] > 0:
                consecutive_dist.append(heights[i] - heights[i-1])

        heapq.heapify(consecutive_dist)

        brick_to_be_used = set()

        while consecutive_dist and bricks >= consecutive_dist[0]:
            elem = heapq.heappop(consecutive_dist)
            brick_to_be_used.add(elem)
            bricks -= elem

        prev_height = heights[0]
        cnt = -1
        for height in heights:
            if height<=prev_height:
                cnt += 1
                prev_height = height
            else:
                if (height - prev_height) in brick_to_be_used:
                    cnt+=1
                else:
                    cnt += 1 if ladders > 0 else 0
                    ladders -= 1
                    if ladders < 0:
                        break

                prev_height = height

        return cnt

sol = Solution()
print(sol.furthestBuilding(heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1))
print(sol.furthestBuilding( heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2))
print(sol.furthestBuilding(heights = [14,3,19,3], bricks = 17, ladders = 0))
print(sol.furthestBuilding(heights = [1, 5, 1], bricks = 3, ladders = 0))
print(sol.furthestBuilding(heights = [253710, 459585, 71981, 223232, 977918, 148680, 123527, 250812, 260416, 554767],bricks = 3367,ladders = 3
))
print(sol.furthestBuilding([1,6,14,15],bricks=5,ladders=1))




