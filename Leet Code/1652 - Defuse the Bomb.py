class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n = len(code)
        circular_pf_sum = [0] * (2 * n)
        ans = []

        if k == 0:
            return [0]*n

        elif k > 0:
            for i in range(1,2 * n):
                circular_pf_sum[i] += circular_pf_sum[(i-1)] + code[(i-1)%n]

            for i in range(n):
                ans.append(circular_pf_sum[i+1+k] - circular_pf_sum[i+1])

        else:
            for i in range(1,2*n):
                circular_pf_sum[i] += circular_pf_sum[i-1] + code[i%n]

            for i in range(n):
                ans.append(circular_pf_sum[n-1+i]-circular_pf_sum[n-1+k+i])

        return ans


sol = Solution()
print(sol.decrypt(code = [5,7,1,4], k = -3))

