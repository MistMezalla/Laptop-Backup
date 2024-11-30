# Definition for a binary tree node.
from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue = deque()
        parent = {root: None}
        lvl = {root: 0}

        queue.append(root)

        while queue:
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
                parent[node.left] = node
                lvl[node.left] = lvl[node] + 1

            if node.right:
                queue.append(node.right)
                parent[node.right] = node
                lvl[node.right] = lvl[node] + 1


        lvl_nodes = {}

        for key,val in lvl.items():
            if val in lvl_nodes:
                lvl_nodes[val].append(key.val)
            else:
                lvl_nodes[val] = [key.val]

        lvl_sum = []
        for key in lvl_nodes:
            lvl_sum.append(sum(lvl_nodes[key]))

        lvl_sum.sort(reverse=True)
        return lvl_sum[k-1] if k <= len(lvl_sum) else -1


def test_kthLargestLevelSum():
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

    # Example tree: [1, 2, 3, 4, 5, 6, 7]
    arr = [5,8,9,2,1,3,7,4,6]
    root = None
    root = insertLevelOrder(arr, root, 0, len(arr))

    # Test the kthLargestLevelSum function
    sol = Solution()
    k = 5 # You can change the value of k
    result = sol.kthLargestLevelSum(root, k)
    print(f"The {k}th largest level sum is: {result}")


# Run the test
test_kthLargestLevelSum()
