'''
-> Counting Sort is better in this case(wrt constraints given)
    -> Time : O(n+k)
    -> Space = O(k)
'''
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        return self.Merge_Sort(nums,0,len(nums)-1)

    def Merge_Sort(self,nums,p,r):
        if p>r:
            return
        if p == r:
            return nums

        q = (p+r)//2
        self.Merge_Sort(nums,p,q)
        self.Merge_Sort(nums,q+1,r)
        self.Merge(nums,p,q,r)

        return nums


    def Merge(self,nums: list[int],p,q,r):
        left = nums[p:q+1]
        right = nums[q+1:r+1]

        i = j = 0
        res = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1

        if left:
            res.extend(left[i:])

        if right:
            res.extend(right[j:])

        for i in range(len(res)):
            nums[p+i] = res[i]

        return nums


class Solution1:
    def sortArray(self, nums: list[int]) -> list[int]:
        max_elem = max(nums)
        min_elem = min(nums)
        count = [0]*(max_elem - min_elem + 1)

        for num in nums:
            count[num - min_elem] += 1

        pos = 0
        for i in range(len(count)):
            temp = count[i]
            count[i] = pos
            pos += temp

        res = [None] * len(nums)
        for num in nums:
            res[count[num - min_elem]] = num
            count[num - min_elem] += 1

        return res

sol = Solution1()
print(sol.sortArray([-1, 5,-3]))