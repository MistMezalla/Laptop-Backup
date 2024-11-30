'''
-> Well this implementation improves(or modifies) the conventional template of Dijkstra algo
-> Modifications:-
    -> maintaining two dist(maps)
        -> one for min
        -> 2nd for 2nd min
    -> freq arr
        -> as a node is popped out at most twice(due to 2nd min condition)
        -> for redundant entries in the min_heap
            -> freq[node] must incr but only freq[node]== 1 or 2 are of use
'''
import heapq
class Solution:
    def secondMinimum(self, n: int, edges: list[list[int]], time: int, change: int) -> int:
        adj_list = {key:[] for key in range(1,n+1)}

        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        # as the cities are '1' indexed
        d1 = {key:float('inf') for key in range(1,n+1)}
        d2 = {key: float("inf") for key in range(1,n+1)}
        freq = [0] * (n+1)

        d1[0] = 0
        min_heap = [(0,1)] #(dist1 or dist2,node)

        while min_heap:
            curr_time,node = heapq.heappop(min_heap)
            freq[node] += 1

            if freq[node] == 2 and node == n:
                return curr_time

            if (curr_time//change) & 1:
                curr_time = change * ((curr_time // change) + 1) + time

            else:
                curr_time += time

            for neighbour in adj_list[node]:
                if freq[neighbour] == 2:
                    continue

                if curr_time < d1[neighbour]:
                    d2[neighbour] = d1[neighbour]
                    d1[neighbour] = curr_time
                    heapq.heappush(min_heap,(curr_time,neighbour))

                elif curr_time < d2[neighbour] and curr_time != d1[neighbour]:
                    d2[neighbour] = curr_time
                    heapq.heappush(min_heap,(curr_time,neighbour))

        return 0 # if there doesn't exist the 2nd min path then this st will be triggered else the abv return will
                # be the ans for this algo

sol = Solution()
print(sol.secondMinimum( n = 5, edges = [[1,2],[1,3],[1,4],[3,4],[4,5]], time = 3, change = 5))
print(sol.secondMinimum( n = 5, edges = [[1,2],[1,3],[1,4],[3,4],[4,5]], time = 3, change = 2))

'''
-> Well the below implementation is of modified bfs
    -> using bfs as edge length == time for all edges
    
-> Modification:-
    -> same def of dist1, dist1 and freq
    -> instead of using visited array for the sake to avoid revisiting the visited edge we are making use of 
    combination if distance arrays dist1 and dist2 as follows:-
        -> if both the values viz d1[node] and d2[node] == -1 then the we don't visit the node
        -> else we visit the node as in this context we are asked to find the 2nd min path
'''
from collections import deque
class Solution:
    def secondMinimum(self, n: int, edges: list[list[int]], time: int, change: int) -> int:
        adj_list = {key: [] for key in range(1, n + 1)}

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        # as the cities are '1' indexed
        d1 = {key: -1 for key in range(1, n + 1)}
        d2 = {key: -1 for key in range(1, n + 1)}

        queue = deque([(1,1)]) #node,freq
        d1[0] = 0
        while queue:
            node,freq = queue.popleft()

            curr_time = d1[node] if freq == 1 else d2[node]

            if (curr_time//change) & 1:
                curr_time = change * (curr_time // change + 1) + time
            else:
                curr_time += time

            for neighbour in adj_list[node]:
                if d1[neighbour] == -1:
                    d1[neighbour] = curr_time
                    queue.append((neighbour,1))

                elif d2[neighbour] == -1 and d1[neighbour] != curr_time:
                    if neighbour == n:
                        return curr_time
                    d2[neighbour] = curr_time
                    queue.append((neighbour,2))

        return 0


