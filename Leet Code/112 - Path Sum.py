from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False


        targetSum -= root.val

        if not root.left and not root.right:
            return targetSum == 0

        # if root.left:
        #     return self.hasPathSum(root.left,targetSum)
        #
        # if root.right:
        #     return self.hasPathSum(root.right,targetSum)

        return self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right,targetSum)


from collections import deque
def build_tree(values):
    """Builds a binary tree from a list of values (None represents missing nodes)."""
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    idx = 1

    while queue and idx < len(values):
        node = queue.popleft()

        if idx < len(values) and values[idx] is not None:
            node.left = TreeNode(values[idx])
            queue.append(node.left)
        idx += 1

        if idx < len(values) and values[idx] is not None:
            node.right = TreeNode(values[idx])
            queue.append(node.right)
        idx += 1

    return root


def test_has_path_sum():
    # Test case: tree with path sum = 22
    values = [5, 4, 8, 11, None, 13, 14, 7, 2, None, None, None, None, None, 1]
    targetSum = 27

    root = build_tree(values)

    solution = Solution()
    result = solution.hasPathSum(root, targetSum)

    print(f"Does the tree have a path sum of {targetSum}? {result}")


# Run the test
test_has_path_sum()