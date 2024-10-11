class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        while n:
            if n > 1 and n % 3 != 0:
                return False

            n //= 3

        return True

# without rec:-
class Solution_alt:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 3**19 % n == 0





