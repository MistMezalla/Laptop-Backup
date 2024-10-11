from sortedcontainers import SortedList
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = [1] * (n+1)

        for i in range(1,n+1):
            fact[i] = fact[i-1] * i

        sorted_list = SortedList(range(1,n+1))

        k-= 1
        res = []

        for i in range(1,n+1):
            ind = k // fact[n-i]
            k -= ind * fact[n-i]
            res.append(str(sorted_list[ind]))
            del sorted_list[ind]

        return "".join(res)

sol = Solution()
print(sol.getPermutation(5,1))