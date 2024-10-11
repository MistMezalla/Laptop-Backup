'''
-> My Intuition:-
    -> Greedy ch 1: add to min ratio
        -> fails for test case 2
    -> Greedy ch2: add all to min ratio
        -> fails both test cases
    -> Tried to make use of hint: max change criterion
        -> Cldn't come up with adequate greedy ch for this hint

-> Below code Intuition:-
    -> Greedy ch: add to ratio that will cause max change to sum of ratios
        -> Create a helper function that will literally calc the potential max change upon adding elem to a part ratio

-> Note:-
    -> heaps don't have 'key' parameter for custom behaviour
    -> either make the elem(generally tuple) ordered acc to custom need
    -> or use some dunder such as '__lt__' and so on
        -> plz chk further bef making use of this method
'''

import heapq
class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        def delta(_pass,total):
            return (_pass + 1)/(total + 1) - (_pass)/total

        max_heap = []

        sum_total = 0
        for c in classes:
            sum_total += c[0]/c[1]
            change = delta(c[0],c[1])
            max_heap.append((-change,c[0],c[1]))
        heapq.heapify(max_heap)

        while extraStudents:
            extraStudents-=1

            extra_val,passed,total = heapq.heappop(max_heap)
            sum_total += -extra_val

            heapq.heappush(max_heap,(-delta(passed+1,total+1),passed+1,total+1))

        return sum_total/len(classes)


sol = Solution()
print(sol.maxAverageRatio(classes = [[1,2],[3,5],[2,2]], extraStudents = 2))
print(sol.maxAverageRatio(classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4))


