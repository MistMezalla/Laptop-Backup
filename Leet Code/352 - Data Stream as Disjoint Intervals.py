from sortedcontainers import SortedSet
class SummaryRanges:

    def __init__(self):
        self.sorted_set = SortedSet()

    def addNum(self, value: int) -> None:
        self.sorted_set.add(value)

    def getIntervals(self) -> list[list[int]]:
        intervals=[]

        i = 0
        while i < len(self.sorted_set):
            interval = [self.sorted_set[i], self.sorted_set[i]]

            while i + 1 < len(self.sorted_set) and self.sorted_set[i + 1] == self.sorted_set[i] + 1:
                interval[1] = self.sorted_set[i + 1]
                i += 1

            intervals.append(interval)
            i += 1

        return intervals

def test_summary_ranges(operations, values):
    # Initialize the SummaryRanges object
    obj = SummaryRanges()
    result = []

    for i in range(len(operations)):
        if operations[i] == "SummaryRanges":
            # Create a new SummaryRanges object (already done above)
            result.append(None)
        elif operations[i] == "addNum":
            # Call addNum with the provided value
            obj.addNum(values[i][0])
            result.append(None)
        elif operations[i] == "getIntervals":
            # Call getIntervals and append the result
            result.append(obj.getIntervals())

    # Output the results
    return result


# Example test case
operations1 = ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum",
              "getIntervals", "addNum", "getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals"]
values1 = [[], [1], [], [3], [], [7], [], [2], [], [6], [],[5],[],[12],[],[10],[]]

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

output2 = test_summary_ranges(operations2,values2)

for op, res in zip(operations2, output2):
    if res is not None:
        print(f"{op}: {res}")


