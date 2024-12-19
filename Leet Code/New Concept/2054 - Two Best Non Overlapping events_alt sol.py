'''
-> Attempt 1:- By sorting wrt end time -> fail
-> Attempt 2:- By using fractional knapsack -> fail

-> Correct methods:-
    -> DP
    -> Bin Search
        -> This is improvement over the 'min number of classrooms' logic (sort wrt start time in asc order)
        -> Here instead of popping out only top most elem of the min heap
        -> all the conpatible elem are popped out
    -> Greedy(See supplementary material for better understanding)
        -> Create modified array of both start and end times together
        -> sort asc
        -> now iterate over the modified sorted array to record the ans

'''

class Solution:
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        time = []

        for st,end,val in events:
            time.append((st,1,val))
            time.append((end+1,0,val))

        time.sort()

        res,max_val = 0,0
        for t,flag,val in time:
            if flag == 1:
                res = max(res,val+max_val)

            else:
                max_val = max(max_val,val)

        return res

sol = Solution()
print(sol.maxTwoEvents(events = [[1,3,2],[4,5,2],[2,4,3]]))