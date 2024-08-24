class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: list[list[int]]) -> list[int]:
        pf_sum = [0] * (len(s) + 1)

        i = 0
        cnt_1 = cnt_0 = 0

        for j in range(len(s)):
            if s[j] == '1':
                cnt_1 += 1
            else:
                cnt_0 += 1

            while min(cnt_1,cnt_0)> k:
                if s[i] == '1':
                    cnt_1 -= 1
                else:
                    cnt_0 -= 1
                i += 1

            pf_sum[j + 1] = pf_sum[j] + (j - i + 1)

        ans = []
        for q in queries:
            l, r = q
            if l == 0:
                ans.append(pf_sum[r + 1])
            else:
                ans.append(pf_sum[r+1] - pf_sum[l+1])

        return ans

# Example usage
sol = Solution()
print(sol.countKConstraintSubstrings("00111",1,[[0,4],[1,4]]))
print(sol.countKConstraintSubstrings("01110001",3,[[0,7]]))
print(sol.countKConstraintSubstrings("001110001",3,[[0,8],[1,8]]))
print(sol.countKConstraintSubstrings("10101", 1, [[0, 4]]))
print(sol.countKConstraintSubstrings("0001111", 2, [[0, 6], [1, 6]]))
print(sol.countKConstraintSubstrings("010101", 1, [[0, 5], [1, 4], [2, 3]]))