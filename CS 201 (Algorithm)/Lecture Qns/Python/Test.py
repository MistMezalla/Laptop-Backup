class Solution:
    def beautifulArray(self, n: int) -> list[int]:
        return self.array_beautifier(list(range(1, n + 1)))

    def array_beautifier(self, arr):
        if len(arr) <= 1:
            return arr

        # Divide the array into two parts: odd indices and even indices
        odd = self.array_beautifier(arr[::2])
        even = self.array_beautifier(arr[1::2])

        # Concatenate odd part first, then even part to form the beautiful array
        return odd + even

sol = Solution()
print(sol.beautifulArray(5))
print(sol.beautifulArray(4))
print(sol.beautifulArray(3))
print(sol.beautifulArray(6))
