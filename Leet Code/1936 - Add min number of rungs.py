class Solution:
    def addRungs(self, rungs: list[int], dist: int) -> int:
        res = 0

        curr_lvl = 0
        for lvl in rungs:
            if lvl - curr_lvl > dist:
                res += (lvl-curr_lvl-1)//dist

            curr_lvl = lvl

        return res

sol = Solution()
print((sol.addRungs(rungs = [1,3,4,10**8], dist = 1)))
