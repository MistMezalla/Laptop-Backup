'''
-> My sol:-
    -> Tried for oneliner algo but cldn't find an exclusive cond to distinguish bet power of 2 and power of 4

-> Below Algo:-
    -> Found a pattern that in the binary representation of power of 4's:-
        -> 1 occur at odd positions always
    -> hence multiplying(&) by 01010101010101010101010101010101 = 0x55555555
'''
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n & n-1 == 0 and n & 0x55555555
