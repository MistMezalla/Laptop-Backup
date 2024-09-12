class Solution:
    def beautifulArray(self, n: int) -> list[int]:
        arr = [i for i in range(1,n+1)]
        return self.array_beautifier(arr)

    def array_beautifier(self,arr):
        if len(arr) <= 2:
            arr.sort(reverse = True)
            return arr

        elif len(arr) == 3:
            arr.sort(reverse=True)
            if 2*arr[1] == arr[0] + arr[2]:
                arr[1],arr[2] = arr[2],arr[1]
            return arr

        mid = len(arr)//2

        left_half = arr[:mid + 1]
        right_half = arr[mid + 1:]

        left_sol = self.array_beautifier(left_half)
        right_sol = self.array_beautifier(right_half)

        left_sol.extend(right_sol)

        return left_sol

sol = Solution()
print(sol.beautifulArray(5))
print(sol.beautifulArray(4))
print(sol.beautifulArray(3))
print(sol.beautifulArray(6))