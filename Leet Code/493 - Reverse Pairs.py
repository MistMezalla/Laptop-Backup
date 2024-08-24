class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        return self._revPairs(nums,0,len(nums)-1)

    def MnC(self,nums,p,q,r):
        res = []
        cnt = 0
        i = p
        j = q+1

        while i<=q and j<=r:
            if nums[i] > nums[j]:
                res.append(nums[j])
                if nums[i] > 2*nums[j]:
                    cnt+=q-i+1
                j+=1
            else:
                res.append(nums[i])
                i+=1

        while i <= q:
            res.append(nums[i])
            i+=1

        while j<= r:
            res.append((nums[j]))
            j+=1

        i = 0
        for i in range(len(res)):
            nums[p+i] = res[i]

        return cnt



    def _revPairs(self,nums,p,r):
        if p>=r:
            return 0

        q = (p+r)//2

        left_cnt = self._revPairs(nums,p,q)
        right_cnt = self._revPairs(nums,q+1,r)

        return left_cnt + right_cnt + self.MnC(nums,p,q,r)

sol = Solution()
print(sol.reversePairs([1,3,2,3,1]))

