from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        
        def in_order(node):
            if not node:
                return False

            complement = k - node.val

            if complement in seen:
                return True
            seen.add(node.val)

            return in_order(node.left) or in_order(node.right)

        return in_order(root)





def build_bst_from_list(values):
    """Helper function to build a BST from a list of values."""
    if not values:
        return None

    def insert_into_bst(root, val):
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = insert_into_bst(root.left, val)
        else:
            root.right = insert_into_bst(root.right, val)
        return root

    root = None
    for value in values:
        root = insert_into_bst(root, value)
    return root


def test_findTarget():
    """Test function for the findTarget method."""
    # Example test case
    values = [5]  # BST values
    root = build_bst_from_list(values)  # Build BST

    solution = Solution()

    k = 10  # Example target sum
    result = solution.findTarget(root, k)

    print(f"Does the BST have two nodes that sum to {k}? {result}")


# Run the test function
test_findTarget()
