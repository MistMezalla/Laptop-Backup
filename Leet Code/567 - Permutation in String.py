from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash = Counter(s1)
        cnt = len(s1)

        st = 0
        while st < len(s2):
            end = st
            while end < len(s2) and s2[end] in hash:
                if hash[s2[end]] != 0:
                    hash[s2[end]] -= 1
                    cnt -= 1
                    if cnt == 0:
                        return True
                else:
                    break
                end += 1

            flag = False
            while st != end:
                hash[s2[st]] += 1
                cnt += 1
                st+=1
                flag = True

            if not flag:
                st += 1

        return False

sol = Solution()
print(sol.checkInclusion(s1 = "bba", s2 = "eidbacbab"))

