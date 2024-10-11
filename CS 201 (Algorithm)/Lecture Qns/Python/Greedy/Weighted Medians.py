class Solution():
    def weighted_median(self,nums,weights):
        pf_sum = [0] * len(weights)
        tot_weight = sum(weights)


        for i in range(len(weights)):
            pf_sum[i] = weights[i] + (pf_sum[i-1] if i-1 >=0 else 0)

            if pf_sum[i] >= tot_weight//2:
                return self.kth_smallest_elem(nums,i+1)


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

        while i<= right:
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

sol = Solution()
# print(sol.kth_smallest_elem([1,1,1,1,1,1,1,1,1,1],7))
# print(sol.kth_smallest_elem([3,6,1,4,9,2,8,10,7],6))
print(sol.weighted_median([5,3,8],[1,2,1]))

