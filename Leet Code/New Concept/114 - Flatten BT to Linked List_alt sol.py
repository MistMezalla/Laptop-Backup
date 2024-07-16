'''
-> Intuition:-
    -> Instead of using stack just use temp ptrs to serve the purpose
'''
from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        curr = root
        while curr:
            if curr.left:
                prev = curr.left
                while prev.right:
                    prev = prev.right
                prev.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right

def create_tree_from_list(values: list[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    index = 1
    while queue and index < len(values):
        node = queue.popleft()
        if index < len(values) and values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1
    return root

# Helper function to convert the flattened tree to a list
def flattened_tree_to_list(root: Optional[TreeNode]) -> list[int]:
    result = []
    while root:
        result.append(root.val)
        root = root.right
    return result

# Function to run a single test case
def run_single_test_case(input_tree: list[Optional[int]], expected_output: list[int]):
    solution = Solution()
    root = create_tree_from_list(input_tree)
    solution.flatten(root)
    output = flattened_tree_to_list(root)
    print(f"Input Tree: {input_tree}")
    print(f"Expected Output: {expected_output}")
    print(f"Output: {output}")
    assert output == expected_output, f"Test case failed: expected {expected_output}, got {output}"
    print("Test case passed!")

# Example usage
input_tree = [1, 2, 5, 3, 4, None, 6]
expected_output = [1, 2, 3, 4, 5, 6]
run_single_test_case(input_tree, expected_output)



