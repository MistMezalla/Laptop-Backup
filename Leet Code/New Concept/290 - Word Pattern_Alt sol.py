'''
Used Hash set : Property of set that they store only unique elem was taken into account.
'''

class Solution_1:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l = s.split()

        if len(l) != len(pattern):
            return False

        d={}
        Set=set()

        for i in range(len(pattern)):
            if pattern[i] in d:
                if d[pattern[i]] != l[i]:
                    return False
            else:
                if l[i] not in Set:
                    d[pattern[i]] = l[i]
                    Set.add(l[i])
                else:
                    return False

        return True

sol1 = Solution_1()
print(sol1.wordPattern("abba","dog cat fish dog"))

'''
Usage of Set property of unique elem.
Usage of zip_longest method: in tuple sizes of parameters passed in zip function are unequal then deficit
elem of parameter tuple is compensated by 'None'
'''

from itertools import zip_longest

class Solution_2:
    def wordPattern(self, pattern: str, s: str) -> bool:

        s = s.split()

        return (len(set(pattern)) ==
                len(set(s)) ==
                len(set(zip_longest(pattern,s))))
