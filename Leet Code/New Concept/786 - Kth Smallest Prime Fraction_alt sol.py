'''
-> This sol improves upon my logic in follow regards:-
    -> It improves upon the precision part of my logic in the bin search
    -> It meticulously manipulates simple arithmatic of fractions in case of fractions cnt
'''

class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        lo,hi = 0,1
        ans = [0,1]


        while True: #improvement on precision part
            cnt = 0
            j = 1
            m = (hi + lo)/2
            ans[0] = 0
            for i in range(len(arr)):
                while j < len(arr) and arr[i] > m*arr[j]: #improvemant on counting logic
                    j += 1

                cnt += len(arr)-j

                if j == len(arr):
                    break

                # if not ans:
                #     ans.append(arr[i])
                #     ans.append(arr[j])
                #
                # elif ans[0] * arr[j] > ans[1] * arr[i]:
                #     ans[0], ans[1] = arr[i], arr[j]


                if ans[0] * arr[j] < ans[1] * arr[i]: #Another meticulous logic for ans updation
                    ans[0] = arr[i]                   # Here aim is to store the max possible fraction < m in order
                    ans[1] = arr[j]                   # to get the max cnt for a specific m

            if cnt < k:
                lo = m
            elif cnt > k:
                hi = m
            else:
                return ans


sol = Solution()
print(sol.kthSmallestPrimeFraction([1,2,3,5],3))
print(sol.kthSmallestPrimeFraction([1,13,17,59],6))