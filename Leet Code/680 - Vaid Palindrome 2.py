class Solution1:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        s= list(s)

        rem = False
        ind = None
        char_rem = None
        while left<= right:
            if s[left] != s[right]:
                if rem == True:
                    return False

                ind = left
                char_rem = s[left]
                s.pop(left)
                left=ind+1

                if s!=s[::-1]:
                    left-=1
                    s.insert(ind,char_rem)
                    ind = right
                    s.pop(right)
                    right = ind-1


                if s!=s[::-1]:
                    return False

            else:
                left+=1
                right-=1



        return True

class Solution2:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        print(s, s[::-1])
        print(s == s[::-1])
        ind = None
        rem = False
        while left <= right:
            if s[left] != s[right]:
                if rem == True:
                    return False

                if s[left + 1] == s[right]:
                    ind = left
                    left += 1
                elif s[left] == s[right - 1]:
                    ind = right
                    right -= 1
                rem = True
            else:
                left += 1
                right -= 1

        return True


sol = Solution1()
print(sol.validPalindrome(
    "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))



sol = Solution2()
print(sol.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))

