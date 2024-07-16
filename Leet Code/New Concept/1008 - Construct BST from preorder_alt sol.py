'''
-> The below sol is of O(n)
-> Solution 1 makes use of 'nonlocal' keyword concept
-> Solution 2 makes use of stack for solving in O(n)
'''
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def bstFromPreorder(self, preorder: list[int]) -> Optional[TreeNode]:
        def builder(lo = float('-inf'),hi = float('inf')):
            nonlocal ind
            if ind == len(preorder):
                return None

            val = preorder[ind]
            if val < lo or val > hi:
                return None

            ind += 1
            node = TreeNode(val)
            node.left = builder(lo,val)
            node.right = builder(val,hi)

            return node

        ind = 0
        return builder()

from collections import deque
class Solution2:
    def bstFromPreorder(self, preorder: list[int]) -> Optional[TreeNode]:
        stack = deque()
        root = TreeNode(preorder[0])
        stack.append(root)

        for value in preorder[1:]:
            node = TreeNode(value)
            if value <= stack[-1].val:
                stack[-1].left = node
            else:
                parent = stack[-1]
                while stack and value > stack[-1].val:
                    parent = stack.pop()
                parent.right = node
            stack.append(node)

        return root

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
elements = [1,None,2,None,3,None,4,None,None]
for el in elements:
    if el is not None:
        root = insert_into_bst(root, el)

preorder = [8,5,1,7,10,12]
sol = Solution2()
new_root = sol.bstFromPreorder(preorder)
print_in_order(new_root)
print()



