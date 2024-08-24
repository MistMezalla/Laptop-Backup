'''
-> This is a very good qns that uses the concept of Sliding Window.
-> Dry Run the program to see how we eff slide the window and compute the max len for each window.
'''
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        i = j = 0
        res = 0
        cnt_T = cnt_F = 0

        while j < len(answerKey):
            if answerKey[j] == 'T':
                cnt_T += 1
            else:
                cnt_F += 1

            while min(cnt_T,cnt_F) > k:
                if answerKey[i] == 'T':
                    cnt_T -= 1
                else:
                    cnt_F -= 1
                i+=1

            res = max(res,j-i+1)
            j+=1

        return res

sol = Solution()
print(sol.maxConsecutiveAnswers("TTTFTFTT",1))