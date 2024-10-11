'''
-> My code:-
    -> In the sliding window approaches that I have seen so far I hv not seen method wherein sluding window size is
    kept constant.
    -> Hence my code failed to pass the test case: "cda" "dcda"

-> Below code:-
    -> As stated abv we keep the size of sliding window(fixed) = len(s1)
    -> Now after iterating over entire s2 we see if the sliding window(cntr) == cntr(s2) and thereby ret T or F
'''
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # cntr_s1 = Counter(s1)
        # Window = Counter()
        cntr_s1 = [0] * 26
        Window = [0] * 26

        for ch in s1:
            cntr_s1[ord(ch) - ord('a')] += 1

        for i in range(len(s2)):
            Window[s2[i]] += 1

            if i >= len(s1):
                if Window[s2[i-len(s1)]] == 1:
                    del Window[s2[i-len(s1)]]
                else:
                    Window[s2[i-len(s1)]] -= 1

            if Window == cntr_s1:
                return True

        return False

class Solution_using_list_for_hashing:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        cnt_s1 = [0] * 26
        window = [0] * 26

        for i in range(len(s1)):
            cnt_s1[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1

        for i in range(len(s2) - len(s1)):
            if cnt_s1 == window:
                return True

            window[ord(s2[i]) - ord('a')] -= 1
            window[ord(s2[i+len(s1)]) - ord('a')] += 1

        if cnt_s1 == window:
            return True
        return False
