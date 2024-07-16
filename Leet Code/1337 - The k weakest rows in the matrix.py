class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        def num_soldiers(lvl,lo,hi):
            while hi - lo > 1:
                mid = (hi+lo)//2

                if mat[lvl][mid] == 1:
                    lo = mid
                else:
                    hi = mid - 1

            if mat[lvl][hi] == 1:
                return hi + 1
            if mat[lvl][lo] == 1:
                return lo + 1
            else:
                return 0

        soldiers_per_lvl = []
        for lvl in range(len(mat)):
            soldiers_per_lvl.append((lvl,num_soldiers(lvl,0, len(mat[lvl])-1)))

        soldiers_per_lvl.sort(key = lambda x: x[1])

        return [soldiers_per_lvl[i][0] for i in range(k)]

sol = Solution()
print(sol.kWeakestRows(mat =
[[1,1,0,0,0],
 [1,1,1,1,0],
 [0,0,0,0,0],
 [0,0,0,0,0],
 [1,1,1,1,1]],
k = 3))
