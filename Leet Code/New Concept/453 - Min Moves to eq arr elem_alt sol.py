'''
-> This sol:-
    -> Simple math eq is involved:-
        -> Sum + m * (n-1) = x * n ; where
            -> m = min # moves
            -> Sum = sum(nums)
            -> n = len(nums)
            -> x = final val where all nums elem wil be eq
        -> m = x - min_num

        -> Solving abv 2 eqns we get: m = Sum - n * min_num

    -> O(n) , O(1)

-> Structured Logic Behind My Algo:-
    -> Well I just applied T&E and tried every possible algo for 3 to 4 good test cases generated by me.
    -> However for the algo that worked in my code below is the reason or rough proof of why the algo will work

    -> Reason:-
        -> reverse the logic by thinking of decreasing the largest elements to match the smallest element, which is
        equivalent in terms of the number of moves.
        -> the formula = (nums[i+1] - nums[i]) * (len(nums) - 1 - i) :  tracks how much each element needs to be
        reduced so that all elements match the smallest element in the sorted array
            -> (nums[i+1] - nums[i]):
                -> moves required to make the element nums[i+1] smaller by that amount.
            -> (len(nums) - 1 - i):
                -> Elements to the right of i all need to be "moved" the same number of times because they all need to
                be incremented together in order to catch up with the current smallest element.
                -> In other words, by reverse logic rem n-1-i elem must be decreased by nums[i+1]-nums[i] times
'''
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        return sum(nums) - min(nums) * len(nums)

sol = Solution()
print(sol.minMoves([3,1,8,14,15]))
print(sol.minMoves([3,1,2]))