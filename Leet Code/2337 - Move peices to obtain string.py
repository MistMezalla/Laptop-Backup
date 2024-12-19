from collections import deque
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        target_queue = deque()
        start_queue = deque()

        for ind,ch in enumerate(start):
            if ch != "_":
                start_queue.append((ch,ind))

        for ind,ch in enumerate(target):
            if ch != "_":
                target_queue.append((ch,ind))

        if len(start_queue) != len(target_queue):
            return False

        while start_queue and target_queue:
            p1,ind1 = start_queue.popleft()
            p2,ind2 = target_queue.popleft()

            if p1 != p2:
                return False

            elif p1 == "L" and ind1 < ind2:
                return False

            elif p2 == "R" and ind1 > ind2:
                return False

        return True

sol = Solution()
print(sol.canChange( start = "_L__R__R_", target = "L______RR"))
print(sol.canChange("_L__R__R_","R___L___R"))

