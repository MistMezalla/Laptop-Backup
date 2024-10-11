'''
-> My sol:-
    -> Makes use of stack to keep track of unpaired brackets
    -> then by looking at pattern (see supplementary material)
    -> Found the formula for the ans

-> Below code:-
    -> Improvises on the space by using stack variable(instead of stack)
'''
class Solution:
    def minSwaps(self, s: str) -> int:
        stack = 0

        for ch in s:
            if ch == "[":
                stack += 1

            else:
                stack -= 1 if stack > 0 else 0

        return (stack + 1)//2

