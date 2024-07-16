class Solution(object):
    def checkRecord(self, s: str) -> bool:
        cnt_A = 0

        for i in range(len(s)):
            if s[i] == 'A':
                cnt_A += 1
            elif s[i] == 'L':
                if s[i: i+3] == 'LLL':
                    return False

        if cnt_A > 1:
            return False
        else:
            return True

