class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)

        if n1 > n2:
            self.findMedianSortedArrays(nums2, nums1)

        lo = 0
        hi = n1
        left = (n1 + n2 + 1) // 2

        while hi - lo > -1:
            mid1 = (hi + lo) // 2
            mid2 = left - mid1

            l1 = l2 = float("-inf")
            r1 = r2 = float("inf")

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
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2
            elif l1 > r2:
                hi = mid1 - 1
            elif l2 > r1:
                lo = mid1 + 1

        return 0


sol = Solution()
print(sol.findMedianSortedArrays([2],[]))

