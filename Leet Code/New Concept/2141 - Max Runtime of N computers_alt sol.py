'''
-> My intuition:-
    -> To solve the problem using heap(sim to 2335)
    -> But the time complexity was roughly O(k*nlogm) ~= O(n^2logn)

-> Below code Intuition:-
    -> Try to divide the total possible battery life evenly among all n computers
    -> Use
        -> Binary Search
'''

# Why this sol below is Greedy: Max Battery Life allocated to a computer via battery or batteries
'''
-> The core idea of a greedy algorithm is to make locally optimal choices with the hope of finding a global optimum. In this solution:
    -> Locally Optimal Choice: 
        For each battery, you greedily use as much power as possible, up to T units, which is the 
        current candidate time being tested in the binary search.
    -> Global Goal: 
        By doing this for every battery, the algorithm checks whether it’s possible to run all n computers for 
        T units of time. If this greedy allocation works, then you increase T (trying to maximize the running time 
        further). If not, you reduce T.
'''

class Solution:
    def maxRunTime(self, n: int, batteries: list[int]) -> int:
        lo,hi = 0,sum(batteries)//n

        while (hi - lo) > 0:
            mid = (hi + lo + 1)//2

            if self.can_run(n,batteries,mid):
                lo = mid
            else:
                hi = mid - 1

        return lo
    def can_run(self,n,batteries,time):
        total = 0

        for life in batteries:
            total += min(life,time)

        return total >= time * n

sol = Solution()
print(sol.maxRunTime( n = 2, batteries = [3,3,3]))