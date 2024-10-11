'''
Revised = 1
Resolved = 1
'''
class Solution:
    def cnt_inversions(self, arr: list[int], p: int, r: int):
        if p >= r:
            return 0

        q = (p + r) // 2
        left_cnt = self.cnt_inversions(arr, p, q)
        right_cnt = self.cnt_inversions(arr, q + 1, r)
        return left_cnt + right_cnt + self.MnC(arr, p, q, r)

    def MnC(self, arr: list[int], p: int, q: int, r: int):
        i = p
        j = q + 1
        res = []
        cnt = 0

        while i <= q and j <= r:
            if arr[j] < arr[i]:
                cnt += (q - i + 1)
                res.append(arr[j])
                j += 1
            else:
                res.append(arr[i])
                i += 1

        while i <= q:
            res.append(arr[i])
            i += 1

        while j <= r:
            res.append(arr[j])
            j += 1

        # Copy the sorted elements back to the original array
        for k in range(len(res)):
            arr[p + k] = res[k]

        return cnt

sol = Solution()
print(sol.cnt_inversions([1, 3, 5, 4, 2], 0, 4))
print(sol.cnt_inversions([1, 2, 3, 4, 5],0,4))
print(sol.cnt_inversions([5,4,3,2,1],0,4))
print(sol.cnt_inversions([2, 2, 2, 2, 2],0,4))
print(sol.cnt_inversions([1, 3, 2, 4, 5],0,4))
print(sol.cnt_inversions([8, 4, 2, 1],0,3))
