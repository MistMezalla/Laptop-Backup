from math import ceil

class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        d = {}
        for i in range(len(answers)):
            if answers[i] in d:
                d[answers[i]] += 1
            else:
                d[answers[i]] = 1

        sum = 0
        for key in d:
            sum += ceil(d[key]/(key+1))*(key+1)

        return sum

my_sol=Solution()
print(my_sol.numRabbits([0,1,0,2,0,1,0,2,1,1]))
