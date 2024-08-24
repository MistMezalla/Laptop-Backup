'''
-> My sol uses index method which causes problem in case of duplicates which can at worst case make my partition
lopsided. Hence making my sol nothing but a variance of Quick Sort.
-> This sol takes into account the problem caused by the index method and handles the partition without moving the
pivot to the end.
'''
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        return self.partition(nums,0,len(nums)-1,len(nums) - k)

    def partition(self,nums,p,r,k):
        if k > r or k < p:
            return None

        if p>=r:
            return nums[p]

        pivot = self.find_pivot(nums,p,r)
        left = p
        right = r
        i = p

        while i<=right:
            if nums[i] < pivot:
                nums[left],nums[i] = nums[i],nums[left]
                i+=1
                left+=1
            elif nums[i] > pivot:
                nums[right],nums[i] = nums[i],nums[right]
                right-=1
            else:
                i+=1

        if left > k:
            return self.partition(nums,p,left-1,k)
        elif right < k:
            return self.partition(nums,right+1,r,k)
        else:
            return nums[k]

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

sol = Solution()
print(sol.findKthLargest([1, 1, 1, 1, 1, 1, 1, 1], 3))  # Test case with duplicates
print(sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
print(sol.findKthLargest([3, 2, 1, 5, 6, 4], 2))
print(sol.findKthLargest([1, 2, 3, 4, 5] + [1] * 1000000 + [-5, -4, -3, -2, -1], 1000000))