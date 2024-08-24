class Solution1:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        return self.partition(nums,0,len(nums)-1,k)

    def partition(self,nums,p,r,k):
        if r-p+1 < k:
            return None

        pivot = self.find_pivot(nums,p,r)
        pivot_ind = nums.index(pivot)
        nums[pivot_ind],nums[r] = nums[r],nums[pivot_ind]

        x = nums[r]
        i = p-1
        for j in range(p,r):
            if nums[j] <= x:
                i+=1
                nums[i],nums[j] = nums[j],nums[i]
        i+=1
        nums[i],nums[r] = nums[r],nums[i]

        if r - i +1 == k:
            return x
        elif r-i +1> k:
            return self.partition(nums,i + 1,r,k)
        else:
            return self.partition(nums,p,i - 1,k-(r-i + 1))

    def find_pivot(self,nums,p,r):
        if r-p+1 <= 5:
            nums = nums[p:r+1]
            nums.sort()
            return nums[len(nums)//2]

        medians = []
        for i in range(p,r+1,5):
            part = nums[i:min(i+5,r+1)]
            part.sort()
            medians.append(part[len(part)//2])

        return self.find_pivot(medians,0,len(medians)-1)

sol = Solution1()
print(sol.findKthLargest([1,1,1,1,1,1,1,1],3))
print(sol.findKthLargest([3,2,3,1,2,4,5,5,6],4))
print(sol.findKthLargest([3,2,1,5,6,4],2))
print(sol.findKthLargest([1,2,3,4,5] + [1]*10000 +[-5,-4,-3,-2,-1],10000))

