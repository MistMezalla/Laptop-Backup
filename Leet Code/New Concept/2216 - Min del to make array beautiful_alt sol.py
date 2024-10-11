'''
-> My code:-
    -> Missed out on the part that len of the modified array shld be even
    -> well the logic of even pair adj was also somewhat wrong as when modified my code to handle even len condn
    the code failed for a test case as my ans lead to over counting.

-> Below code:-
    -> Works on the same principle of Greedy choice:-
        -> Del the very 1st problematic pair to keep the array vaild.
        -> It meticulously takes into account the logic of my prev del(which was not that robust)
    -> In the end if le is odd the  just del the last elem as the prev elem are valid wrt cond of beautiful arr
        -> Why last elem only:-
            -> Coz this improved logic in one pass converts the array into beautiful wrt indices condn
            -> Now del of the last elem won't shift the array as no elem to right of the last elem and elem to the
            left of the array are beautiful by the algo

    -> Intuition(Algo):-
    -> iterate over every pair:-
        -> if a pair is valid skip by 2 places(to check for next pair(condn of even indices))
        -> if not valid skip by one place(as now the right part of the array os shifted to left by one place)
'''

class Solution:
    def minDeletion(self, nums: list[int]) -> int:
        op = 0
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1] and (i - op)%2 == 0: # Here (i-op) is the way to check new index being either
                op += 1                                  # even or odd; op = odd => new index = odd
                                                         #              op = even => new index = even
        return op + (len(nums) - op)%2

sol = Solution()
print(sol.minDeletion(nums = [1,1,2,3,5]))
print(sol.minDeletion(nums = [1,1,2,2,3,3]))
print(sol.minDeletion([2,2,2]))
print(sol.minDeletion([1,1,2,2,3,3,3,7,7]))
print(sol.minDeletion([1,1,4,2,2,5,3,3,3,6]))


