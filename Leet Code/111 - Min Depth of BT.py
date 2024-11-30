from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def depth(node):
            if not node:
                return 0

            left_depth = depth(node.left)
            right_depth = depth(node.right)

            if left_depth == 0:
                return right_depth + 1
            elif right_depth == 0:
                return left_depth + 1
            else:
                return min(left_depth,right_depth) + 1


        return depth(root)


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


# Testing function for minDepth
def test_min_depth():
    # Example tree: [1, 2, 5, 3, None, 6, 7, 4, None, None, None, None, 8]
    values = [1, 2, 5, 3, None, 6, 7, None, None, None, None, None, 8]
    root = build_tree_from_list(values)

    # Initialize the solution and call minDepth
    solution = Solution()
    result = solution.minDepth(root)

    # Print the result
    print(f"Minimum depth of the tree: {result}")


# Run the test function
test_min_depth()
