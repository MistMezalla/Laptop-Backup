from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = deque()

        while stack or root:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            k-=1
            if k == 0:
                return root.val
            root = root.right

def print_in_order(node):
    if node:
        print_in_order(node.left)
        print(node.val, end=' ')
        print_in_order(node.right)

def insert_into_bst(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root

root = None
elements = [3,1,4,None,2]
for el in elements:
    if el is not None:
        root = insert_into_bst(root, el)

sol = Solution()
print(sol.kthSmallest(root,1))

print()



