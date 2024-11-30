from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> list[list[int]]:
        paths = []

        def gen_paths(node,path,path_val):
            if not node:
                return

            path_val += node.val
            path.append(node.val)

            if node.left:
                gen_paths(node.left,path,path_val)
            if node.right:
                gen_paths(node.right,path,path_val)

            if not node.left and not node.right:
                if targetSum == path_val:
                    paths.append(path[:])

            path.pop()


        gen_paths(root,[],0)

        return paths


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


def test_path_sum():
    # Test case: tree with path sums that add to targetSum = 22
    values = []
    targetSum = 22

    root = build_tree(values)

    solution = Solution()
    result = solution.pathSum(root, targetSum)

    print(f"All root-to-leaf paths with sum {targetSum}: {result}")


# Run the test
test_path_sum()
