'''
-> The below code is accomplished by referring to the algo of finding target sub arrays with req sum from an i/p
array in O(n).
-> Refer Supplementary material for the same
'''
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        paths = []
        pf_path_sum = {0:1}
        cnt = 0

        def gen_paths(node,path,path_val):
            if not node:
                return

            nonlocal cnt
            path_val += node.val
            path.append(node.val)

            if path_val - targetSum in pf_path_sum:
                cnt += pf_path_sum[path_val - targetSum]

            pf_path_sum[path_val] = pf_path_sum.get(path_val,0) + 1

            if node.left:
                gen_paths(node.left,path,path_val)

            if node.right:
                gen_paths(node.right,path,path_val)

            # if not node.left and not node.right:
            #     paths.append(path[:])

            path.pop()
            if path_val in pf_path_sum:
                pf_path_sum[path_val] -= 1

        gen_paths(root,[],0)

        return cnt
        # cnt = 0
        # for path in paths:
        #     pf_sum_cnt = {0:1}
        #     curr_sum = 0
        #
        #     for num in path:
        #         curr_sum += num
        #
        #         if curr_sum - targetSum in pf_sum_cnt:
        #             cnt += pf_sum_cnt[curr_sum-targetSum]
        #
        #         pf_sum_cnt[curr_sum] = pf_sum_cnt.get(curr_sum,0) + 1
        #
        #
        # return cnt


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

    return nodes[0]  # Root node


def test_path_sum():
    # Create a sample tree: [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
    values = [10,5,1,3,-4]
    target_sum = 1
    root = build_tree_from_list(values)

    # Initialize the solution and call pathSum
    solution = Solution()
    result = solution.pathSum(root, target_sum)

    # Print result
    print(f"Number of paths with sum {target_sum}: {result}")


# Run the test function
test_path_sum()


