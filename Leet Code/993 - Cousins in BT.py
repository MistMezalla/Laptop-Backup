from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = deque()
        parent = {root.val: None}
        lvl = {root.val: 0}

        queue.append(root)
        while queue:
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
                parent[node.left.val] = node.val
                lvl[node.left.val] = lvl[node.val] + 1

            if node.right:
                queue.append(node.right)
                parent[node.right.val] = node.val
                lvl[node.right.val] = lvl[node.val] + 1



        if lvl[x] == lvl[y] and parent[x] != parent[y]:
            return True
        return False


def test_isCousins():
    # Helper function to insert nodes in level order
    def insertLevelOrder(arr, root, i, n):
        if i < n:
            temp = TreeNode(arr[i])
            root = temp

            # insert left child
            root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)

            # insert right child
            root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n)
        return root

    # Example tree: [1, 2, 3, 4, 5, None, None]
    arr = [1,2,3,None,4,None,5]
    root = None
    root = insertLevelOrder(arr, root, 0, len(arr))

    # Create an instance of the Solution class
    sol = Solution()

    # Test for cousins: x = 4, y = 5 (should return True, as they are cousins)
    x = 4
    y = 5
    result = sol.isCousins(root, x, y)
    print(f"Are nodes {x} and {y} cousins? {result}")


# Run the test
test_isCousins()

