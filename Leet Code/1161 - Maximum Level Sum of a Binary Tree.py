from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        level_sum = []

        queue.append(root)
        while queue:
            curr_sum = 0

            for _ in range(len(queue)):
                node = queue.popleft()
                curr_sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            level_sum.append(curr_sum)


        return level_sum.index(max(level_sum)) + 1


def build_tree(values):
    """Builds a binary tree from a list of values (None represents missing nodes)."""
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    idx = 1

    while queue and idx < len(values):
        node = queue.popleft()

        if values[idx] is not None:
            node.left = TreeNode(values[idx])
            queue.append(node.left)
        idx += 1

        if idx < len(values) and values[idx] is not None:
            node.right = TreeNode(values[idx])
            queue.append(node.right)
        idx += 1

    return root


def print_tree_level_order(root):
    """Prints the tree in level-order (breadth-first search)."""
    if not root:
        print("Empty tree")
        return

    queue = deque([root])
    result = []

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Trim trailing 'None' values to make output cleaner
    while result and result[-1] is None:
        result.pop()

    print(result)


# Test the Solution with a helper function
def test_max_level_sum():
    # Example tree: [1, 7, 0, 7, -8, None, None]
    values = [989,None,10250,98693,-89388,None,None,None,+321270145]

    root = build_tree(values)

    print("Original Tree:")
    print_tree_level_order(root)

    solution = Solution()
    max_level = solution.maxLevelSum(root)

    print(f"Level with maximum sum: {max_level}")


# Run the test
test_max_level_sum()