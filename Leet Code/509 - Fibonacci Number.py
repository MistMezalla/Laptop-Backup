class Solution:
    def fib(self, n: int) -> int:
        # # bottom_up
        # fib = {}
        # for k in range(n+1):
        #     if k == 0:
        #         f = 0
        #
        #     elif k == 1:
        #         f = 1
        #
        #     else:
        #         f = fib[k-1] + fib[k-2]
        #
        #     fib[k] = f
        #
        # return fib[n]

        # top_down
        memo = {}
        def fibo(m):
            if m == 0:
                f = 0
            elif m == 1:
                f = 1
            elif m in memo:
                return memo[m]
            else:
                f = fibo(m-1) + fibo(m-2)

            memo[m] = f
            return f

        return fibo(n)

sol = Solution()
print(sol.fib(0))
print(sol.fib(1))
print(sol.fib(2))
print(sol.fib(3))
print(sol.fib(4))
print(sol.fib(5))
print(sol.fib(6))