from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = deque()
        if not root:
            return 0
        curr = root
        ans = 0
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if curr.val >= low and curr.val <= high:
                ans += curr.val
            curr = curr.right

        return ans

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
elements = [10,5,15,3,7,13,18,1,None,6]
for el in elements:
    if el is not None:
        root = insert_into_bst(root, el)

sol = Solution()
print(sol.rangeSumBST(root,6,10))
