'''
-> See the editorial of this question to look for the theory and related expln for all the approaches given
'''

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Left and Right Traversals(or preorder and rev preorder traversals)
class Solution_1:
    def treeQueries(self, root: Optional[TreeNode], queries: list[int]) -> list[int]:
        curr_max_height = 0
        node_height_after_rem = {}

        def left_to_right(node,curr_height):
            if not node:
                return

            nonlocal curr_max_height
            node_height_after_rem[node.val] = curr_max_height

            curr_max_height = max(curr_max_height,curr_height)

            left_to_right(node.left,curr_height + 1)
            left_to_right(node.right,curr_height + 1)


        def right_to_left(node,curr_height):
            if not node:
                return

            nonlocal curr_max_height
            node_height_after_rem[node.val] = max(node_height_after_rem[node.val],curr_max_height)

            curr_max_height = max(curr_height,curr_max_height)

            right_to_left(node.right,curr_height + 1)
            right_to_left(node.left,curr_height + 1)

        left_to_right(root,0)
        curr_max_height = 0
        right_to_left(root,0)

        return [node_height_after_rem[q] for q in queries]
        #return [node_height_after_rem.get(TreeNode(q), -1) for q in queries]

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

# Testing function for treeQueries
def test_tree_queries():
    # Build a sample tree, e.g., [1, 2, 3, 4, 5, None, 6, None, None, 7, 8]
    values = [1, 2, 3, 4, 5, None, 6, None, None, 7, 8]
    root = build_tree_from_list(values)
    queries = [1, 4, 5, 6, 7]  # Sample query nodes

    # Initialize the solution and call treeQueries
    solution = Solution_1()
    result = solution.treeQueries(root, queries)

    # Print the result
    print(f"Results for queries {queries}: {result}")

# Run the test function
test_tree_queries()