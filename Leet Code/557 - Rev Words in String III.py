class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(" ")
        res = []
        for elem in l:
            elem = elem[::-1]
            res.append(elem)


        return " ".join(res)


sol = Solution()
print(sol.reverseWords( "Let's take LeetCode contest"))