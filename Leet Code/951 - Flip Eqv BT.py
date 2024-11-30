from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True

        elif not (root1 and root2):
            return False

        elif root1.val != root2.val:
            return False

        else:
            return (self.flipEquiv(root1.left, root2.left) or self.flipEquiv(root1.left, root2.right)) and \
                (self.flipEquiv(root1.right, root2.left) or self.flipEquiv(root1.right, root2.right))


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


def test_flip_equiv():
    # Example trees to test
    values1 = [1,2,3,4,5,6,None,None,None,7,8]
    values2 = [1,3,2,None,6,4,5,None,None,None,None,8,17]

    tree1 = build_tree(values1)
    tree2 = build_tree(values2)

    solution = Solution()
    result = solution.flipEquiv(tree1, tree2)

    print(f"Are the trees flip equivalent? {result}")


# Run the test
test_flip_equiv()
