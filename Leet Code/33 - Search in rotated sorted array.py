'''
-> The solution is wrong as O(log n) was asked but the solution below is O(n)
-> All divide and conquer or bin searches mimic are not O(logn) always as it is the case in this example
'''
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def found(lo,hi):
            if lo > hi:
                return -1

            if lo == hi:
                if nums[lo] == target:
                    return lo
                else:
                    return -1


            mid = (lo + hi)//2

            if nums[mid] == target:
                return mid

            found_left = found(lo,mid-1)
            found_right = found(mid+1,hi)

            if found_left != -1:
                return found_left
            if found_right != -1:
                return found_right

            return -1

        return found(0,len(nums)-1)


sol = Solution()
print(sol.search([6,7,0,1,2,3,4,5],6))
