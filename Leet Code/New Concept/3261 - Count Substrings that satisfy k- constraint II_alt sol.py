'''
-> Intuition of my code:-
    -> Prefix Sum of valid substrings
    -> Sliding window for substring count
    -> Querying:- Prefix[r+1] - Prefix[l] (Incorrect: leads to over counting of incorrect substrings wrt constraint)

-> Intuition of this code:-
    -> Store indices of left most and right most indices of each substring by the means of bijection(2 list or dict
    to serve the purpose)
    -> Prefix Sum of valid substrings
    -> Sliding Window for substring count
    -> Querying(Most imp point of this code):-
        -> For every lower bound of query find the max valid substr starting from lower bound
        -> number of substr of the max str so found = n(n+1)/2 : n is length of this found substr
        -> For substr that end bet [middle + 1, upper bound]: calc using prefix sum to avoid calc duplicates
'''


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: list[list[int]]) -> list[int]:
        left_to_right = [0]*len(s)
        right_to_left = [0]*len(s)
        cnt = {'0':0,'1':0}
        left = 0

        for right in range(len(s)):
            cnt[s[right]] += 1
            while min(cnt['0'],cnt['1']) > k:
                cnt[s[left]] -= 1
                left += 1
            right_to_left[right] = left

        right = len(s)-1
        cnt = {'0': 0, '1': 0}
        for left in reversed(range(len(s))):
            cnt[s[left]] += 1

            while min(cnt['1'],cnt['0']) > k:
                cnt[s[right]]-= 1
                right -= 1
            left_to_right[left] = right

        pf_sum = [0]*(len(s)+1)
        for i in range(1,len(s)+1):
            right = i-1
            left = right_to_left[right]
            pf_sum[i]  = pf_sum[i-1] + (right- left + 1)

        res = []
        for query in queries:
            l,r = query

            middle = min(r,left_to_right[l])
            length = middle - l + 1
            curr = length * (length+1) // 2
            curr += pf_sum[r+1] - pf_sum[middle+1]
            res.append(curr)

        return res

sol = Solution()
print(sol.countKConstraintSubstrings("001110001",3,[[0,8],[1,8]]))
print(sol.countKConstraintSubstrings("00111",1,[[0,4],[1,4]]))
print(sol.countKConstraintSubstrings("01110001",3,[[0,7]]))
print(sol.countKConstraintSubstrings("10101", 1, [[0, 4]]))
print(sol.countKConstraintSubstrings("0001111", 2, [[0, 6], [1, 6]]))
print(sol.countKConstraintSubstrings("010101", 1, [[0, 5], [1, 4], [2, 3]]))
print(sol.countKConstraintSubstrings("100101",1,[[0, 3], [1, 4], [2, 5]]))





