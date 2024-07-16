class Solution:
    def slowestKey(self, releaseTimes: list[int], keysPressed: str) -> str:


        max_val =releaseTimes[0]
        max_st = keysPressed[0]
        for i in range (1 ,len(keysPressed)):
            if releaseTimes[i]-releaseTimes[i-1] > max_val:
                max_st = keysPressed[i]
                max_val = releaseTimes[i]-releaseTimes[i-1]
            elif releaseTimes[i]-releaseTimes[i-1] == max_val:
                if keysPressed[i] >= max_st:
                    max_st = keysPressed[i]
                max_val = releaseTimes[i] - releaseTimes[i - 1]



        return max_st

sol = Solution()
print(sol.slowestKey([12,23,36,46,62],"spuda"))



