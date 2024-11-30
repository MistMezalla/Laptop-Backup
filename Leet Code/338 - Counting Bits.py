class Solution:
    def countBits(self, n: int) -> list[int]:
        if n == 0:
            return [0]
        elif n == 1:
            return [0,1]
        curr_pow = 1
        res = [0,1]
        for i in range(2,n+1):
            factor = i // curr_pow

            if factor > 1:
                curr_pow *= 2

            res.append(res[i-curr_pow] + 1)

        return res

sol = Solution()
print(sol.countBits(17))


