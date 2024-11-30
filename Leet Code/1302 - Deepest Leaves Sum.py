from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()

        queue.append(root)

        last_lvl_sum = 0
        while queue:
            n = len(queue)
            curr_sum = 0

            for _ in range(n):
                node = queue.popleft()
                curr_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            last_lvl_sum = curr_sum

        return last_lvl_sum

