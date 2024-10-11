'''
Revised = 1
Resolved = 0
'''
class Solution():
    def MnC(self, A: list[int], B: list[int]):
        res = []
        i = j = 0
        cntr = 0

        while i < len(A) and j < len(B):
            if A[i] > B[j]:
                cntr += len(A) - i
                res.append(B[j])
                j += 1
            else:
                res.append(A[i])
                i += 1

        while i < len(A):
            res.append(A[i])
            i += 1

        while j < len(B):
            res.append(B[j])
            j += 1

        return res, cntr

sol = Solution()
print(sol.MnC([3, 6, 9, 10], [1, 2, 4, 7, 18]))
