'''
-> Makes use of 2 pointer concept.
-> No extra concept except string manipulation
-> Catch: in question there is nowhere written that only one swap is to be made to find the res number; however
the test cases where giv in that format to lead in wrong direction.
'''

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        dig = list(str(n))
        i = len(dig)-1

        while i > 0 and dig[i-1] >= dig[i]:
            i-=1

        if i==0:
            return -1

        '''
        -> Once i-1 is found, the next step is to find the smallest digit to the right of i-1 that is greater than 
        dig[i-1]. This digit is located at position j.
        -> We are finding smallest greater elem as we are to find next largest number of the digits of number n.
        '''
        j = len(dig) - 1
        while j > i-1 and dig[i-1] >= dig[j]:
            j-=1

        dig[i-1],dig[j] = dig[j],dig[i-1]

        dig[i:] = dig[i:][::-1]
        n = int("".join(dig))

        if n > 2**31 - 1:
            return -1

        return n

sol = Solution()
print(sol.nextGreaterElement(24354321))