class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        if sum(arr) % k != 0:
            return False

        rem = [0] * k

        for num in arr:
            rem[num%k] += 1

        if rem[0] % 2 != 0:
            return False

        for i in range(1,len(rem)):
            if rem[i] != rem[k-i] or (rem[i] + rem[k-i]) % 2 != 0:
                return False

        return True

sol = Solution()
print(sol.canArrange([1,1,1,1,1,1,1,1,2,2],3))



