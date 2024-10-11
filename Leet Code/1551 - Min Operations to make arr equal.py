class My_Solution:
    def minOperations(self, n: int) -> int:
        op = 0
        for i in range(n//2 + 1 if n & 1 else n//2):
            op += n - (2 * i + 1)

        return op

sol =  My_Solution()
print(sol.minOperations(3))
print(sol.minOperations(5))
print(sol.minOperations(4))
print(sol.minOperations(2))
print(sol.minOperations(10))
print(sol.minOperations(6))

class Solution():
    def minOperations(self, n: int) -> int:
        return (n//2 + 1)*(n//2) if n & 1 else (n//2)*(n//2) #sum of series even numbers;
                                                             # else sum of series of odd numbers.
    # This is becoz the # op req to reach n from left half numbers only(as 2 numbers to be operated at same time)
    # Thus for n = 5: 1 3 5 7 9 => ops = 4 + 2 + 0 = (2+1)(2) = (n//2 + 1)(n//2)




