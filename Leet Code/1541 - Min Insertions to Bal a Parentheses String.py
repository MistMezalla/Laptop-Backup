class Solution:
    def minInsertions(self, s: str) -> int:
        mismatched =[]

        i = 0
        while i < len(s):
            # if i < len(s) - 1 and s[i] == s[i+1] == ")":
            #     if mismatched and mismatched[-1] == "(":
            #         mismatched.pop()
            #         i+=2
            #     else:
            #         mismatched.append(s[i])
            #         i+=1
            # else:
            #     mismatched.append(s[i])
            #     i+=1

            if s[i] == ")":
                if mismatched and mismatched[-1] == "(":
                    if i < len(s) - 1 and s[i+1] == ")":
                        mismatched.pop()
                        i+=2
                    else:
                        mismatched.append(s[i])
                        i+=1
                elif len(mismatched) >= 2 and mismatched[-1] == ")" and mismatched[-2] == "(":
                    mismatched.pop()
                    mismatched.pop()
                    i+=1
                else:
                    mismatched.append(s[i])
                    i+=1
            else:
                mismatched.append(s[i])
                i+=1


        i = 0
        res = 0
        while i < len(mismatched):
            if mismatched[i] == ")":
                if i < len(mismatched) - 1 and mismatched[i+1] == ")":
                    res += 1
                    i+=2
                else:
                    res+=2
                    i+=1
            elif mismatched[i] == "(" :
                if i < len(mismatched) - 1 and mismatched[i+1] == ")":
                    res+= 1
                    i+=2
                else:
                    res += 2
                    i+=1

        return res

sol = Solution()
print(sol.minInsertions(s ="))())("))
print(sol.minInsertions("(()()))(()))))))"))
print(sol.minInsertions("(()))(()))()())))"))
print(sol.minInsertions("())(()))"))
print(sol.minInsertions("(()))(()))()()))))"))
print(sol.minInsertions("(()))()))"))