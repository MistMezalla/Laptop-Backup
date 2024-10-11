'''
-> My code:-
    -> tried the logic given below but cldn't refine it properly to come up with the sol

-> Below code(improvised by me):-
    -> adds the necessary intervals
    -> converts the selected intervals to set to avoid duplicate intervals so created by logic of the code
'''
class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()

        cover = []
        left = -1
        right = -1

        for st,end in intervals:
            if st > left and end > right:
                left = st

            right = max(right,end)
            if cover and st == cover[-1][0]:
                cover.pop()

            if left == st and right == end:
                cover.append((left,right))

        return len(cover)

sol = Solution()
print(sol.removeCoveredIntervals([[0,10],[5,12]]))
print(sol.removeCoveredIntervals([[1,8],[3,6],[2,8]]))
print(sol.removeCoveredIntervals([[1,2],[1,4],[3,4]]))
