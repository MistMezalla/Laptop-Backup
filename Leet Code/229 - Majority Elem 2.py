class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        res = []
        cnt1 = cnt2 = 0
        elem1 = elem2 = None

        for num in nums:
            if num == elem1:
                cnt1+=1
            elif num == elem2:
                cnt2+=1
            elif cnt1 == 0:
                elem1,cnt1 = num,1
            elif cnt2 == 0:
                elem2,cnt2 = num,1
            else:
                cnt1-=1
                cnt2-=1

        cnt1 = cnt2 = 0
        for num in nums:
            if num == elem1:
                cnt1+=1
            if num == elem2:
                cnt2+=1

        if cnt1 > len(nums)//3:
            res.append(elem1)
        if cnt2>len(nums)//3:
            res.append(elem2)

        return res


sol = Solution()
print(sol.majorityElement([1,2,2,2,3,3,3,4,5]))

