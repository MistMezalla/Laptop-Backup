'''
-> My Intuition:-
    -> To find tentative window via min heap
    -> Minimise the size of the tentative window by the means of sliding window

-> Below Sol:-
    -> gives a less complicated implementation of my intuition while using the basics of my logic viz:-
        -> tentative window building using min heap
        -> window sliding: using
            -> the qn conditions
            -> and until the size of the min heap drops below k
'''
import heapq
class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        min_heap = []
        curr_max = float('-inf')
        for i in range(len(nums)):
            heapq.heappush(min_heap,(nums[i][0],i,0))
            curr_max = max(curr_max,nums[i][0])

        smallest_range = [float('-inf'),float("inf")]
        while min_heap:
            curr_min, list_ind, ind = heapq.heappop(min_heap)

            if curr_max - curr_min < smallest_range[1] - smallest_range[0] or (curr_min < smallest_range[0] and
            curr_max - curr_min == smallest_range[1] - smallest_range[0]):
                smallest_range = [curr_min,curr_max]

            if ind + 1 < len(nums[list_ind]):
                heapq.heappush(nums[list_ind][ind+1],list_ind,ind + 1)
                curr_max = max(curr_max,nums[list_ind][ind+1])

            else:
                break #coz now the heap will fall down by len == k => that the range will not 'cover' atleast one
                      # elem from each of the k lists

        return smallest_range

