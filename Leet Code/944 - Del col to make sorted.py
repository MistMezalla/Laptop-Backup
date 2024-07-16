class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        num = 0
        for i in range(len(strs[0])):
            faulty = False
            for j in range(len(strs)-1):
                if strs[j][i] > strs[j+1][i]:
                    faulty = True
                    break
            if faulty:
                num+=1

        return num





