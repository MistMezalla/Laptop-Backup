'''
-> The followup cond: Solve without rec or interation => O(1) , O(1) sol req.

-> Property:-
    -> For power of 2's say n:-
        -> n & n-1 = 0
    -> else:-
        -> 0

    -> Reason(when n is power of two):-
        -> n is of form : 1000(say)
        -> n-1 is of form: 0111(for the abv n)
        -> Thus n & n-1 = 0000

-> FAQ:-
    -> Why my sol = O(logn), O(1) and below sol = O(1), O(1)
        -> The ans is that the iterative loop will run for logn times to perform bitwise left shift
        -> The n & n-1 is computed all at once
            ->  It can be deemed O(logn) for large i/p set which no the case here.

'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & n-1
