from math import isqrt
class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True]*(n+7)

        prime_cnt = 0
        isPrime[0] = isPrime[1] = False
        for i in range(2,isqrt(n)+1):
            if isPrime[i]:
                for j in range(i*i,n,i):
                    isPrime[j]=False

        for i in range(2,n):
            if isPrime[i]:
                prime_cnt+=1
                
        return prime_cnt

sol = Solution()
print(sol.countPrimes(100))
