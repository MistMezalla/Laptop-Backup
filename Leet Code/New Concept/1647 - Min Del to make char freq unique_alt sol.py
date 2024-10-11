'''
-> My code:-
    -> Time = O(n)
    -> Space = O(n)
    -> Uses the sys to del the duplicate elem in order

-> Below sol:-
    -> T(n) = O(n)
    -> Space = O(1)
    -> Uses the concept of deleting the duplicate entry until iteratively until the entry turns into unique val
'''

from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        # hash = {}
        #
        # for chr in s:
        #     if chr in hash:
        #         hash[chr] += 1
        #
        #     else:
        #         hash[chr] = 1

        '''
        -> Well the Counter based implementation for abv commented part is faster based on the constant factor
        though both implementation are O(n),O(n) based
        -> Counter is implemented in 'C language' and used some low level memory management manipulations to reduce
        the constant associated with this implementation.
        '''

        cntr = Counter(s)
        del_cnt = 0
        freq_set = set()
        for freq in cntr.values():
            while freq > 0 and freq in freq_set:
                freq -= 1
                del_cnt += 1

            freq_set.add(freq)

        return del_cnt

sol = Solution()
print(sol.minDeletions("aaabbbcc"))
print(sol.minDeletions("aaaaabbbbcccddddeeefffffgggggg"))
print(sol.minDeletions("aaaaceb"))