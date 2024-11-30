class Solution:
    def minChanges(self, s: str) -> int:
        cnt_arr = []

        curr_cnt = 1
        curr_ch = s[0]

        for i in range(1,len(s)):
            if s[i] == curr_ch:
                curr_cnt +=1

            else:
                cnt_arr.append(curr_cnt)
                curr_ch = s[i]
                curr_cnt = 1

        cnt_arr.append(curr_cnt)

        res = 0
        is_Odd = False
        for cnt in cnt_arr:
            if not is_Odd and cnt & 1:
                is_Odd = True
                continue

            if is_Odd and cnt % 2 == 0:
                res += 1

            elif is_Odd and cnt % 2 != 0:
                is_Odd = False
                res += 1

        return res

sol = Solution()
print(sol.minChanges("110001100111"))
print(sol.minChanges("1100011110011000110001110000"))
print(sol.minChanges("1001"))
print(sol.minChanges("10"))
print(sol.minChanges("0000"))



