'''
-> Below logic:-
    -> For accessing nodes pertaining to only a single tree level just use the 'for loop' as demonstrated below code
    -> See below queue growth stages for a complete tree of lvl say 3:-
        -> queue = 8 | 4 7 |10 25 1 3| 5 87 9 16 23 51 48 0

    -> This meticulous method of using for loop will help to save the additional sp complexity or mem overhead
    associated with hashing
'''
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
        queue.append(root)

        lvl_sum = []
        while queue:
            curr_sum = 0
            n = len(queue)

            for _ in range(n):
                node = queue.popleft()

                curr_sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            lvl_sum.append(curr_sum)

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
    k = 2 # You can change the value of k
    result = sol.kthLargestLevelSum(root, k)
    print(f"The {k}th largest level sum is: {result}")


# Run the test
test_kthLargestLevelSum()
