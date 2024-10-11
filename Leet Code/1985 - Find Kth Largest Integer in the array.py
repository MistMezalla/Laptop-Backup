class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:
        nums_int = [int(x) for x in nums]
        nums_int.sort(reverse=True)

        return str(nums_int[k-1])

class Solution_in_string_only:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:
        return self.kth_smallest_int(nums,0,len(nums)-1,len(nums)-k)

    def kth_smallest_int(self,nums,left,right,pos):
        if pos < left or pos > right:
            return None

        if left>=right:
            return nums[left]

        pivot = self.find_pivot(nums,left,right)
        lo = left
        i = left
        hi = right

        while i<=hi:
            if self.lt(nums[i],pivot):
                nums[lo],nums[i] = nums[i],nums[lo]
                lo += 1
                i += 1
            elif self.gt(nums[i],pivot):
                nums[i],nums[hi] = nums[hi],nums[i]
                hi -= 1
            else:
                i += 1

        if lo > pos:
            return self.kth_smallest_int(nums,left,lo-1,pos)
        elif hi < pos:
            return self.kth_smallest_int(nums,hi + 1,right,pos)
        else:
            return nums[pos]

    def find_pivot(self,nums,left,right):
        if right - left + 1 <= 5:
            part = nums[left:right + 1]
            part = self.sort_arr(part)
            return part[len(part)//2]

        median = []
        for i in range(left,right+1,5):
            part = nums[left:min(left+5,right+1)]
            self.sort_arr(part)
            median.append(part[len(part)//2])

        return self.find_pivot(median,0,len(median) - 1)

    def sort_arr(self,part):
        part = [int(num) for num in part]
        part.sort()
        return [str(num) for num in part]


    def lt(self,n1: str,n2: str):
        if len(n1) > len(n2):
            return False
        elif len(n1) < len(n2):
            return True
        else:
            i = 0

            while i < len(n1):
                if n1[i] > n2[i]:
                    return False
                elif n1[i] < n2[i]:
                    return True
                i+=1

            return False #WLOG: both are equal

    def gt(self,n1: str,n2: str):
        if len(n1) > len(n2):
            return True
        elif len(n1) < len(n2):
            return False
        else:
            i = 0

            while i < len(n1):
                if n1[i] > n2[i]:
                    return True
                elif n1[i] < n2[i]:
                    return False
                i+=1

            return False #WLOG: both are equal


sol = Solution_in_string_only()
print(sol.kthLargestNumber(["423","521","2","42"],2))
print(sol.kthLargestNumber(nums = ["6","7","3","10"], k = 4))
print(sol.kthLargestNumber(nums = ["2","21","12","1"], k = 1))
print(sol.kthLargestNumber(nums = ["0","0"], k = 2))
nums = [2,5,2,-1,-3,-2,-1,1,0,0,2,3,4,5]
print(sorted(nums,reverse=True))
nums = [str(num) for num in nums]
print(sol.kthLargestNumber(nums,8))


