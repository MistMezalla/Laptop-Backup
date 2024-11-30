class Solution:
    def minimumSteps(self, s: str) -> int:
        cnt_1 = 0
        res = 0
        for ch in s:
            if ch == "1":
                cnt_1 += 1
            else:
                res += cnt_1

        return res
