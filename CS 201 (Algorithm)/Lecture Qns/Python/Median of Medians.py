'''
-> The Sol1 is erroneous in sense that it fails for case of duplicates
'''
class Solution1():
    def kth_smallest_elem(self,nums: list[int],k: int):
        return self.partition(nums,0,len(nums)-1,k)

    def partition(self,nums,p,r,k):
        if r - p + 1  < k:
            return None

        pivot_ind = nums.index(self.find_pivot(nums,p,r))

        nums[pivot_ind],nums[r] = nums[r],nums[pivot_ind]

        x = nums[r]
        i = p - 1
        j = p
        while j <= r-1:
            if nums[j] <= x:
                i+=1
                nums[j],nums[i] = nums[i],nums[j]
            j+=1
        nums[i+1],nums[r] = nums[r],nums[i+1]

        i += 1

        if i - p + 1 == k:
            return nums[i]
        elif i - p + 1 > k:
            return self.partition(nums,p,i,k)
        else:
            return self.partition(nums,i+1,r,k - (i - p + 1))

    def find_pivot(self,nums,p,r):
        if r-p+1 <= 5:
            nums[p:r+1].sort()
            return nums[(p+r)//2]

        parts = []
        for i in range(p, r + 1, 5):
            sub_part = nums[i:min(i + 5, r + 1)]
            sub_part.sort()
            parts.append(sub_part[len(sub_part) // 2])

        return self.find_pivot(parts,0,len(parts)-1)

sol1 = Solution1()
#print(sol.partition([1,1,1,1,1,1,1,1,1,1],7)) #Solution 1 will fail this test case
print(sol1.kth_smallest_elem([3,6,1,4,9,2,8,10,7],6))

'''
-> Solution 2 takes into account this problem
'''
class Solution2():
    def kth_smallest_elem(self,nums: list[int],k: int):
        return self.partition(nums,0,len(nums)-1,k-1)

    def partition(self,nums,p,r,pos):
        if pos > r or pos < p:
            return None

        if p>=r:
            return nums[p]

        pivot = self.find_pivot(nums,p,r)
        left = p
        right = r
        i = p

        while i <= right:
            if nums[i] < pivot:
                nums[left],nums[i] = nums[i],nums[left]
                i+=1
                left+=1
            elif nums[i] > pivot:
                nums[right], nums[i] = nums[i], nums[right]
                right-=1
            else:
                i+=1

        if left > pos:
            return self.partition(nums,p,left-1,pos)
        elif right < pos:
            return self.partition(nums,right+1,r,pos)
        else:
            return nums[pos]


    def find_pivot(self,nums,p,r):
        if r-p+1<=5:
            nums = nums[p:r+1]
            nums.sort()
            return nums[len(nums)//2]

        medians = []
        for i in range(p,r+1,5):
            part = nums[i:min(i+5,r+1)]
            part.sort()
            medians.append(part[len(part)//2])

        return self.find_pivot(medians,0,len(medians)-1)

sol2 = Solution2()
print(sol2.kth_smallest_elem([1,1,1,1,1,1,1,1,1,1],7)) #Solution 1 will fail this test case
print(sol2.kth_smallest_elem([3,6,1,4,9,2,8,10,7],6))








