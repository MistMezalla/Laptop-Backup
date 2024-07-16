'''
-> Sim to Qn 33 this is O(n) solution though expected was O(Log n)
'''
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def found(arr):
            if len(arr) == 0:
                return False

            if len(arr) == 1:
                if arr[0] == target:
                    return True
                else:
                    return False



            mid = (0+len(arr)-1)//2

            if arr[mid] == target:
                return True

            left_half = arr[:mid]
            right_half = arr[mid+1:]

            found_left = found(left_half)
            found_right = found(right_half)

            if found_left or found_right:
                return True

            return False

        return found(nums)


sol = Solution()
print(sol.search([6,7,0,0,1,2,3,4,5,6],8))
