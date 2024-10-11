from collections import Counter
class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        n = len(skill)//2
        if sum(skill) % n != 0:
            return -1

        req_skill = sum(skill)//n
        hash = {i+1:0 for i in range(req_skill)}
        # hash = [0 for i in range(req_skill + 1)]
        chem = 0

        for sk in skill:
            if sk not in hash:
                return -1
            # if sk > req_skill:
            #     return -1
            hash[sk] += 1

        for sk in skill:
            # if sk not in hash or req_skill-sk not in hash:
            #     return -1

            if sk == req_skill - sk and hash[sk] % 2 != 0:
                return -1

            if hash[sk] != hash[req_skill - sk]:
                return -1

            chem += sk * (req_skill - sk)

        return chem//2

sol = Solution()
print(sol.dividePlayers(skill = [3,2,5,1,3,4]))
print(sol.dividePlayers([2,1,3,3,4,3,1,7]))
print(sol.dividePlayers([7,3,4,2,6,1,5,4]))
print(sol.dividePlayers([10,14,16,15,9,4,4,4]))



