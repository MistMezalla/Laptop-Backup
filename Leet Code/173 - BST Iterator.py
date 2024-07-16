from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        stack = deque()
        self.iterator = deque() #queue

        while root or stack:
            while root:
                stack.append(root)
                root= root.left
            root = stack.pop()
            self.iterator.append(root)
            root = root.right

    def next(self) -> int:
        return self.iterator.popleft().val if self.iterator else None

    def hasNext(self) -> bool:
        return True if self.iterator else False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()