class Solution:
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        priority_events = []

        for st,end,val in events:
            priority_events.append((st,end,val,val/end))

        priority_events.sort(key=lambda x: x[3], reverse=True)

        end_pt = priority_events[0][1]
        st_pt = priority_events[0][0]
        res_val= priority_events[0][2]

        for i in range(1,len(priority_events)):
            curr_end = priority_events[i][1]
            curr_st = priority_events[i][0]
            curr_val = priority_events[i][2]

            if curr_st > end_pt:
                return res_val + curr_val

            elif curr_end < st_pt:
                return res_val + curr_val


sol = Solution()
#fails for this test case
print(sol.maxTwoEvents(events = [[1,3,2],[4,5,2],[2,4,3]]))







