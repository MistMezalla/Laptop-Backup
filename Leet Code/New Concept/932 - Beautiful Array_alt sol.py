'''
-> My Intuition:-(Fail)
    -> Dividing array into 2 halves based on the mid_pt
    -> And solve the Problem by sorting and swapping at base cases and then simply merge the 2 sol halves
    -> Problem condition: i<j<k and 2*[k] == [i] + [j] => for any indices i and j there shldn't exist a mean of two
    in between indices

-> This Code's Intuition:-
    -> Dividing on the basis of even and odd indices
    -> then simply merge the left and right sol

    -> The reason why dividing on the basis of even and odd indices worked is that
        -> On very first division: Left half => Odd numbers & Right half => Even numbers
        -> mean of odd numbers is even which is in right half => Problem Condition passed
        -> mean of even numbers is even
            -> However recursive DnC of even part sep the even part into 2 smaller parts where mean of two numbers
            exist in other part
            Ex: On first div, even part: [2,4,6,8]. On 2nd div, [2,6] and [4,8]
            Here mean of (2 and 6) i.e 4 is in right part and mean of (4 and 8) i.e. 6 is in left part
'''

class Solution:
    def beautifulArray(self, n: int) -> list[int]:
        arr = [i for i in range(1,n+1)]
        return self.array_beautifier(arr)

    def array_beautifier(self,arr):
        if len(arr) <= 1:
            return arr

        odd_half = self.array_beautifier(arr[::2])
        even_half = self.array_beautifier(arr[1::2])

        odd_half.extend(even_half)

        return odd_half

sol = Solution()
print(sol.beautifulArray(5))
print(sol.beautifulArray(4))
print(sol.beautifulArray(3))
print(sol.beautifulArray(6))

