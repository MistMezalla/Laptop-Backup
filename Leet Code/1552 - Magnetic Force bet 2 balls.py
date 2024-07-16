class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        def can_place(force: int):
            balls_ct = m
            last_pos = -1

            for i in range(len(position)):
                if (position[i] - last_pos >= force or last_pos == -1):
                    last_pos = position[i]
                    balls_ct-=1
                if balls_ct == 0:
                    break

            return balls_ct==0


        position.sort()
        lo = 0
        hi = position[-1]

        while (hi - lo) > 1:
            mid = (hi + lo)//2

            if can_place(mid):
                lo = mid
            else:
                hi = mid - 1

        if can_place(hi):
            return hi
        else:
            return lo


sol = Solution()
print(sol.maxDistance([79,74,57,22],4))
print(sol.maxDistance([5,4,3,2,1,1000000000],2))
print(sol.maxDistance([5,4,3,2,1,1000000000],4))
print(sol.maxDistance([1,2,3,4,7],3))


