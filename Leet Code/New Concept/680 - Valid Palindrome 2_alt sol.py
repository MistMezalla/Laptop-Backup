'''
-> Every nested loop is not O(n**2)
-> here when if is not executed then O(1) op on each iter
-> for if block "exe only once during the lifetime of the code" has O(n) op
-> summing over: k= else block op and k+1^th if block exe;
                 T(n) = k*O(1) + O(n) = O(n+k) = O(2n) ; worst case => hence O(n)+
'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left , right = 0 ,len(s)-1

        while left<=right:
            if s[left]!=s[right]:
                st_l=s[:left]+s[left+1:]
                st_r=s[:right]+s[right+1:]

                return st_l==st_l[::-1] or st_r == st_r[::-1]

            left+=1
            right-=1

        return True