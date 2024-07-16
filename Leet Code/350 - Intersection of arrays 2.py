class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()
        intersection = []

        i = j = 0
        while i<len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                intersection.append(nums1[i])
                i+=1
                j+=1

            elif nums1[i] < nums2[j]:
                i+=1

            else:
                j+=1

        return intersection

sol = Solution()
print(sol.intersect([1,2,2,1],[2,2]))
print(sol.intersect([4,9,5],[9,4,9,8,4]))
