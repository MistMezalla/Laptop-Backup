'''
-> In question it is nowhere written that substrings have to be unique
'''
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        i = j = 0
        cnt = 0
        cnt_1 = cnt_0 = 0

        while j < len(s):
            if s[j] == '1':
                cnt_1 += 1
            else:
                cnt_0 += 1


            while min(cnt_1,cnt_0) > k:
                if s[i] == '1':
                    cnt_1 -= 1
                else:
                    cnt_0 -= 1
                i+= 1

            cnt += j-i+1
            j+=1

        return cnt

sol = Solution()
print(sol.countKConstraintSubstrings('00',1))
