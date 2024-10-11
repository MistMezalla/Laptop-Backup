class Solution:
    def top_down_fibonacci(self,n: int):
        memo = {}
        def fib(k):
            if k < 2:
                f = 1

            elif k in memo:
                return memo[k]

            else:
                f = fib(k-1) + fib(k-2)

            memo[k] = f

            return f

        return fib(n)

    def bottom_up_fibonacci(self,n):
        fib = {}
        for k in range(n+1):
            if k < 2:
                f = 1

            else:
                f = fib[k-1] + fib[k-2]

            fib[k] = f

        return fib[n]


sol = Solution()
print(sol.top_down_fibonacci(5))
print(sol.bottom_up_fibonacci(0))