class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash = {}
        Set = set()

        for i in range(len(s)):
            if s[i] in hash:
                if hash[s[i]] != t[i]:
                    return False

            else:
                if t[i] in Set:
                    return False
                else:
                    hash[s[i]] = t[i]
                    Set.add(t[i])

        return True
