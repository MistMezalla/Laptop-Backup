'''
-> My sol:-
    -> This sol is correct but slow:
    -> getIntervals = O(nlogn) and != O(n)
        -> as accessing an elem = O(logn) and != O(1)

-> Below sol is fast rel as:
    -> in the addNum method only:-
        -> intervals are made(to be consistent wrt follow up, else by my method repeated merges wld take place)
        -> finding unique num add : O(n)
        -> interval merging : O(n)
'''


class SummaryRanges:
    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        for interval in self.intervals:
            if interval[0] <= value <= interval[1]:
                return

        i = 0
        new_interval = [value,value]
        while i < len(self.intervals):

            if self.intervals[i][1] + 1 < value:
                i+=1

            elif self.intervals[i][0] - 1 > value:
                break

            else:
                new_interval[0] = min(new_interval[0],self.intervals[i][0])
                new_interval[1] = max(new_interval[1],self.intervals[i][1])
                self.intervals.pop(i)
                continue

        self.intervals.insert(i,new_interval)

    def getIntervals(self) -> list[list[int]]:
        return self.intervals

def test_summary_ranges(operations, values):
    obj = SummaryRanges()
    result = []

    for i in range(len(operations)):
        if operations[i] == "SummaryRanges":
            result.append(None)
        elif operations[i] == "addNum":
            obj.addNum(values[i][0])
            result.append(None)
        elif operations[i] == "getIntervals":
            result.append(obj.getIntervals())

    return result


# Example test case
operations1 = ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]#, "addNum",
              #"getIntervals", "addNum", "getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals"]
values1 = [[], [1], [], [3], [], [2], [] ]#,[7], [], [6], [],[5],[],[12],[],[10],[]]

# Call the test helper
output1 = test_summary_ranges(operations1, values1)

# Print the results
for op, res in zip(operations1, output1):
    if res is not None:
        print(f"{op}: {res}")

operations2 = ["SummaryRanges","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum",
               "getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum",
               "getIntervals","addNum","getIntervals","addNum","getIntervals"]
values2 = [[],[6],[],[6],[],[0],[],[4],[],[8],[],[7],[],[6],[],[4],[],[7],[],[5],[]]

output2 = test_summary_ranges(operations2, values2)

for op, res in zip(operations2, output2):
    if res is not None:
        print(f"{op}: {res}")
