'''
-> The solution calculated pairs diff then merged the arrays
-> whereas my approached tried to do it altogether
-> Hence my sol missed some of the rev pairs
'''

class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        return self._revPairs(nums,0,len(nums)-1)

    def _revPairs(self,nums,p,r):
        if p>=r:
            return 0

        q = (p+r)//2

        left_cnt = self._revPairs(nums,p,q)
        right_cnt = self._revPairs(nums,q+1,r)

        return left_cnt + right_cnt + self.MnC(nums,p,q,r)

    def MnC(self,nums,p,q,r):
        res = []
        j = q+1
        cnt = 0

        for i in range(p,q+1):
            while j <= r and nums[i] > 2 * nums[j]:
                j += 1
            cnt += j - (q+1)


        j = q+1
        i = p
        while i<=q and j<=r:
            if nums[i] > nums[j]:
                res.append(nums[j])
                j+=1
            else:
                res.append(nums[i])
                i+=1

        while i<=q:
            res.append(nums[i])
            i+=1

        while j<=r:
            res.append(nums[j])
            j+=1

        i = 0
        for i in range(len(res)):
            nums[p+i] = res[i]

        return cnt

sol = Solution()
print(sol.reversePairs([1,3,2,3,1]))

