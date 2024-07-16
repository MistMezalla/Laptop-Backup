from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stack = deque()
        queue = deque()

        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            queue.append(node)
            node = node.right

        root = queue[0]
        node = queue.popleft()
        while queue:
            node.right = queue.popleft()
            node.left = None
            node = node.right

        node.right = node.left = None

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

root1 = None
elements1 = [5,3,6,2,4,None,8,1,None,None,None,7,9]
for el in elements1:
    if el is not None:
        root1 = insert_into_bst(root1, el)

sol = Solution()
new_root = sol.increasingBST(root1)

print_in_order(new_root)



