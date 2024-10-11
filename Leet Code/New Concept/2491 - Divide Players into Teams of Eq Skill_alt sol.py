'''
-> This code:-
    -> Though O(nlogn), O(1), this implementation is:-
        -> simpler
        -> faster in practice
            -> Coz there is a memory overhead associated in my code
'''
class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()

        req_skill = skill[0] + skill[-1]
        chem = 0
        for i in range(len(skill)//2):
            if skill[i] + skill[-i-1] != req_skill:
                return -1
            chem += skill[i] * skill[-i-1]

        return chem
