from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> list[int]:
        ans = []

        stack1 = deque()
        stack2 = deque()

        tree1 = root1
        tree2 = root2

        while tree1 or tree2 or stack1 or stack2:
            while tree1:
                stack1.append(tree1)
                tree1 = tree1.left

            while tree2:
                stack2.append(tree2)
                tree2 = tree2.left

            if stack1 and (not stack2 or (stack1 and stack1[-1].val <= stack2[-1].val)):
                tree1 = stack1.pop()
                ans.append(tree1.val)
                tree1 = tree1.right
            elif stack2:
                tree2 = stack2.pop()
                ans.append(tree2.val)
                tree2 = tree2.right

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

root1 = None
elements1 = [1,None,8]
for el in elements1:
    if el is not None:
        root1 = insert_into_bst(root1, el)

root2 = None
elements2 = [8,1]
for el in elements2:
    if el is not None:
        root2 = insert_into_bst(root2, el)

sol = Solution()
print(sol.getAllElements(root1,root2))
