'''
-> Iterative inorder traversal
'''

from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        stack = deque()
        GST = 0
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.right
            curr = stack.pop()
            curr.val = GST = curr.val + GST
            curr = curr.left


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
elements = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
for el in elements:
    if el is not None:
        root = insert_into_bst(root, el)

sol = Solution()
new_root = sol.bstToGst(root)

print("In-order traversal of the Greater Sum Tree:")
print_in_order(new_root)