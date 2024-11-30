from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque()
        level_sums = []

        queue.append(root)
        while queue:
            n = len(queue)
            curr_sum = 0
            for _ in range(n):
                node = queue.popleft()
                curr_sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            level_sums.append(curr_sum)

        lvl = 1
        root.val = 0
        queue.append(root)
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                sibling_sum = (node.left.val if node.left else 0) + (node.right.val if node.right else 0)

                if node.left:
                    node.left.val = level_sums[lvl] - sibling_sum
                    queue.append(node.left)

                if node.right:
                    node.right.val = level_sums[lvl] - sibling_sum
                    queue.append(node.right)

            lvl += 1

        return root


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


# Test the solution with a helper function
def test_replace_value_in_tree():
    # Example tree: [1, 2, 3, 4, 5, None, 6]
    values = [5,4,9,1,10,None,7]

    root = build_tree(values)

    print("Original Tree:")
    print_tree_level_order(root)

    solution = Solution()
    modified_root = solution.replaceValueInTree(root)

    print("Modified Tree:")
    print_tree_level_order(modified_root)


# Run the test
test_replace_value_in_tree()
