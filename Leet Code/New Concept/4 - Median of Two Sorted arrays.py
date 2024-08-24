'''
-> This qn kind of makes use of 'kth smallest elm in 2 sorted arrays' where the helper function's logic is used in
the partition checking conditions of this algo
-> By replicating or extending the 'kth smallest elm in 2 sorted arrays' solution; T(n) =O(log(m) + log(n)) =O(log(mn))
-> However the below solution is of O(log(m+n))
'''
#Intuition in brief
'''
-> First partition the 2 arrays into left and right parts s.t cnt_left of both arrays ceil(half(len(arr1) + len(arr2))
-> Next check if the partition so made into left and right in both arrays is correct
    ->If not then left part of either of the arrays has smaller number of elem and relatively the other array has
    excess elem.
    -> Hence left part of the pseudo combined array is not strictly less than all elem of right part
    -> As abt the med left part(all elem) <= right part(all elem)
    -> Thus keep repartitioning the arrays until pseudo left is consistent with pseudo right
'''
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)

        if n1 > n2:
            return self.findMedianSortedArrays(nums2,nums1)

        left = (n1+n2+1)//2

        lo = 0
        hi = n1

        while hi - lo > -1:
            mid1 = (hi + lo)//2
            mid2 = left - mid1

            l1 = l2 = float('-inf')
            r1 = r2 = float('inf')

            if mid1 < n1:
                r1 = nums1[mid1]
            if mid1 > 0:
                l1 = nums1[mid1 - 1]
            if mid2 < n2:
                r2 = nums2[mid2]
            if mid2 > 0:
                l2 = nums2[mid2 - 1]

            if l1 <= r2 and l2 <= r1:
                if (n1 + n2) & 1:
                    return max(l1,l2)
                else:
                    return (max(l1,l2)+min(r1,r2))/2
            elif l1 > r2: # right part small or left part is large
                hi = mid1 - 1
            elif l2 > r1:
                lo = mid1 + 1

        return 0 # This implies that i/p arrays were not sorted.

sol = Solution()
print(sol.findMedianSortedArrays([1,2,3],[4,5,6,7,8,9,10]))







