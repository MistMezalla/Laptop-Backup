# T(n) = O(log(log n))
class Solution1:
    def kth_smallest_elems(self,nums1: list[int],nums2: list[int],k: int):
        lo,hi = min(nums1[0],nums2[0]),max(nums1[-1],nums2[-1])

        while hi - lo > 1:
            mid = (hi + lo) // 2

            cnt1 = self.elem_less(nums1,mid)
            cnt2 = self.elem_less(nums2,mid)

            if cnt1 + cnt2 < k:
                lo = mid + 1
            else:
                hi = mid

        kth_lowest = None
        if self.elem_less(nums1,lo) + self.elem_less(nums2,lo) == k:
            kth_lowest = lo
        else:
            kth_lowest = hi

        cnt1 = self.elem_less(nums1,kth_lowest)
        cnt2 = self.elem_less(nums2,kth_lowest)
        res = []
        i = j = 0

        while len(res) < k:
            if i < cnt1 and (j == cnt2 or nums1[i] <= nums2[j]):
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1

        return res

    def elem_less(self,nums,val):
        lo,hi = 0,len(nums)

        while hi - lo > 1:
            mid = (hi + lo) // 2

            if nums[mid] <= val:
                lo = mid + 1
            else:
                hi = mid

        if nums[lo] > val:
            return lo
        return hi

sol = Solution1()
print(sol.kth_smallest_elems([1, 3, 5, 7], [2, 8], 3))

# T(n) = O(log(n))
class Solution2:
    def kth_smallest_elems(self, nums1: list[int], nums2: list[int], k: int):
        if len(nums1) > len(nums2):
            return self.kth_smallest_elems(nums2, nums1, k)

        lo, hi = 0, len(nums1)

        while hi - lo > -1:
            mid1 = (hi + lo) // 2
            mid2 = k - mid1

            if mid2 < 0: # left part is too big
                hi = mid1 - 1
                continue
            if mid2 > len(nums2): #right part is too small
                lo = mid1 + 1
                continue

            l1 = nums1[mid1 - 1] if mid1 > 0 else float('-inf')
            l2 = nums2[mid2 - 1] if mid2 > 0 else float('-inf')
            r1 = nums1[mid1] if mid1 < len(nums1) else float('inf')
            r2 = nums2[mid2] if mid2 < len(nums2) else float('inf')

            if l1 <= r2 and l2 <= r1:
                return max(l1, l2)
            elif l1 > r2:
                hi = mid1 - 1
            else:
                lo = mid1 + 1

        return -1  # This line should never be reached if inputs are valid

sol = Solution2()
print(sol.kth_smallest_elems([1, 3, 5, 7], [2, 6, 8], 6))
