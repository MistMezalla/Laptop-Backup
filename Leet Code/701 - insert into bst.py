from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
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
                    node.right = add_node(node.right,data)

            return node

        if root is None:
            return TreeNode(val)

        return add_node(root,val)



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

root1 = None
elements1 = [40,20,60,10,30,50,70]
for el in elements1:
    if el is not None:
        root1 = insert_into_bst(root1, el)

sol = Solution()
new_root = sol.insertIntoBST(root1,25)
print_in_order(new_root)





