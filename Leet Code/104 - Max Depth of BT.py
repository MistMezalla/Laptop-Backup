from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0

        def depth(node, curr_depth):
            if not node:
                return

            nonlocal max_depth
            max_depth = max(max_depth, curr_depth)

            depth(node.left, curr_depth + 1)
            depth(node.right, curr_depth + 1)

        depth(root, 1)
        return max_depth


# Helper function to build a tree from a list of values
def build_tree_from_list(values):
    if not values:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in values]

    for i in range(len(nodes)):
        if nodes[i] is not None:
            left_index = 2 * i + 1
            right_index = 2 * i + 2

            if left_index < len(nodes):
                nodes[i].left = nodes[left_index]
            if right_index < len(nodes):
                nodes[i].right = nodes[right_index]

    return nodes[0]  # Return the root node


# Testing function for maxDepth
def test_max_depth():
    # Example tree: [3, 9, 20, None, None, 15, 7]
    values = [3, 9, 20, None, None, 15, 7]
    root = build_tree_from_list(values)

    # Initialize the solution and call maxDepth
    solution = Solution()
    result = solution.maxDepth(root)

    # Print the result
    print(f"Maximum depth of the tree: {result}")


# Run the test function
test_max_depth()
