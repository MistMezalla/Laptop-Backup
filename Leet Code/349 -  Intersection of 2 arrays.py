class Solution1:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        i = j = 0

        intersection = []
        nums1.sort()
        nums2.sort()

        while i<len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                intersection.append(nums1[i])
                i+=1
                j+=1
            elif  nums1[i] < nums2[j]:
                i+=1
            else:
                j+=1

        return list(set(intersection))

class Solution2:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set(nums1)
        set(nums2)
        return nums1 and nums2

sol1 = Solution1()
print(sol1.intersection([1,2,2,1],[2,2]))

sol2 = Solution2()
print(sol1.intersection([1,2,2,1],[2,2]))

