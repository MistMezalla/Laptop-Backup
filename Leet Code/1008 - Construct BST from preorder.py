'''
-> Time complexity O(n**2)
-> Simply ignored abt it
'''
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])

        def add_node(node,data):
            if data <= node.val:
                if node.left is None:
                    node.left = TreeNode(data)
                else:
                    node.left = add_node(node.left,data)
            else:
                if node.right is None:
                    node.right = TreeNode(data)
                else:
                    node.right = add_node(node.right, data)

            return node

        for i in range(1, len(preorder)):
            add_node(root, preorder[i])

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
sol = Solution()
new_root = sol.bstFromPreorder(preorder)
print_in_order(new_root)
print()




