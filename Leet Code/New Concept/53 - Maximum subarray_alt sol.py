'''
-> The followup part is solved here with diff approaches,i.e, to solve using 'Divide and Conquer'
'''

'''
-> Solution 1 makes use of 'Walrus op'
->The walrus operator allows you to write more concise code by combining the assignment and the expression in a 
single line. 
-> With walrus op:
    -> right_sum = max(right_sum, cur_sum := cur_sum + A[i])
-> Without walrus op:
    -> cur_sum = cur_sum + A[i]
       right_sum = max(left_sum, cur_sum)
'''

'''
Resolve = 1
Revise = 2
'''
class Solution1:
    def maxSubArray(self, nums: list[int]) -> int:
        def MSA(arr,left,right):
            if left > right:
                return float('-inf')

            mid = (left+right)//2
            left_sum = right_sum = curr_sum = 0

            for i in range(mid-1,left-1,-1): #max suffix sum calculation
                left_sum = max(left_sum,curr_sum := curr_sum+arr[i])

            curr_sum = 0
            for i in range(mid+1 ,right+1): #max prefix sum calc
                right_sum = max(right_sum,curr_sum := curr_sum+arr[i])

            return max(MSA(arr,left,mid-1),MSA(arr,mid+1,right),left_sum + arr[mid] + right_sum)

        return MSA(nums,0,len(nums)-1)


sol1 = Solution1()
print(sol1.maxSubArray([-1,-2,-3,-4]))
print(sol1.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(sol1.maxSubArray([1]))
print(sol1.maxSubArray([5,4,-1,7,8]))
print(sol1.maxSubArray([-5,-4,-1,-7,-8]))

''''
-> T(n) = 2.T(n/2) + O(n) => T(n) = O(nlogn); where O(n) is due to calculation of pf_sum and suff_sum in each 
conquer step
'''

'''
-> This code makes use of concept of shallow cpying elem in diff form by using [*nums]
'''
'''
Resolve = 1
Revise = 2
'''
class Solution2:
    def maxSubArray(self, nums: list[int]) -> int:
        pre,suff= [*nums],[*nums]

        for i in range(1,len(nums)):
            pre[i] += max(0,pre[i-1])

        for i in range(len(nums)-2,-1,-1):
            suff[i] += max(0,suff[i+1])

        def MSA(arr,left,right):
            if left == right:
                return arr[left]

            mid = (left+right)//2

            return max(MSA(arr,left,mid),MSA(arr,mid+1,right),pre[mid] + suff[mid+1])

        return MSA(nums,0,len(nums)-1)

sol2 = Solution2()
print(sol2.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(sol2.maxSubArray([1]))
print(sol2.maxSubArray([5,4,-1,7,8]))
print(sol2.maxSubArray([-5,-4,-1,-7,-8]))

'''
-> T(n) = 2T(n/2) + O(1) => T(n) = O(n)
'''

'''
Resolve = 1
Revise  = 2
'''
class Solution3():
    def maxSubArray(self, nums: list[int]) -> int:
        total = 0
        res = nums[0]

        for num in nums:
            if total < 0:
                total = 0

            total += num
            res = max(res,total)

        return res



