'''
-> My Intuition:-
    -> Use 2 stacks one for NGE and 2nd for NGE2
    -> Well but couldn't come up with robust algo

-> Below code:-
    -> Uses 2 stacks.
        -> 1st stack : stores the indices of the elem whose nge1 is found but nge2 is yet to be found.
        -> 2nd stack : stores the indices of the elem whose nge1 is ont found
    -> Now compare each elem of the array
        -> if the elem is greater than the top of stack 1
            -> pop all indices and set res[popped indices] = elem
                -> as the elem is the 2nd nge of the popped elem
        -> if the elem is greater than top of 2nd stack
            -> traditional nge1 finding process
            -> now append the popped elem of from the abv process to stack1 by def of stacks
    -> Since each elem is popped and pushed onto stacks at most once
        -> T(n) = O(n)
        -> S(n) = O(n)
'''


class Solution:
    def secondGreaterElement(self, nums: list[int]) -> list[int]:
        nge2 = [-1] * len(nums)
        st1,st2 = [],[]

        for i,elem in enumerate(nums):
            while st1 and nums[st1[-1]] < elem:
                nge2[st1.pop()] = elem

            temp = []
            while st2 and nums[st2[-1]] < elem:
                temp.append(st2.pop())

            st1.extend(temp[::-1])
            st2.append(i)

        return nge2

sol = Solution()
print(sol.secondGreaterElement([1,2,4,3]))
print(sol.secondGreaterElement([2,4,0,9,6]))

from collections import deque
class Solution_deque_based():
    def secondGreaterElement(self, nums: list[int]) -> list[int]:
        nge2 = [-1] * len(nums)
        st1 = deque()
        st2 = deque()


        for i,elem in enumerate(nums):
            while st1 and nums[st1[-1]] < elem:
                nge2[st1.pop()] = elem

            temp_st = deque()
            while st2 and nums[st2[-1]] < elem:
                temp_st.append(st2.pop())

            while temp_st:
                st1.append(temp_st.pop())

            st2.append(i)

        return nge2

sol = Solution_deque_based()
print(sol.secondGreaterElement([1,2,4,3]))
print(sol.secondGreaterElement([2,4,0,9,6]))
print(sol.secondGreaterElement([11,13,15,12,0,15,12,11,9]))
