'''
-> Question has application of DP
-> Hence solve after completing DP
'''
class Solution:
    def distributeCookies(self, cookies: list[int], k: int) -> int:
        lo,hi = max(cookies),sum(cookies)

        def can_distribute(cnt):
            no_child = 1
            curr_cnt = 0

            for cookie in cookies:
                if cookie + curr_cnt > cnt:
                    curr_cnt = cookie
                    no_child += 1

                    if no_child > k:
                        return False
                else:
                    curr_cnt += cookie

            return True

        while hi - lo > 0:
            mid = (hi + lo)//2

            if can_distribute(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo

sol = Solution()
print(sol.distributeCookies(cookies = [8,15,10,20,8], k = 2))
