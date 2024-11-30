from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        visited = {}
        parent = {root: None}
        def dfs1(node):
            deepest_node = node
            max_dist = 0
            visited[node] = False
            
            if node.left:
                parent[node.left] = node
                curr_dist,deep_node = dfs1(node.left)
                if curr_dist +1 > max_dist:
                    max_dist = curr_dist + 1
                    deepest_node = deep_node
                    
            if node.right:
                parent[node.right] = node
                curr_dist,deep_node = dfs1(node.right)
                if curr_dist +1 > max_dist:
                    max_dist = curr_dist + 1
                    deepest_node = deep_node            
                
            return max_dist,deepest_node

        def dfs2(node):
            visited[node] = True
            max_dist = 0
            deepest_node = node

            for neighbour in [parent[node],node.left,node.right]:
                if neighbour and not visited[neighbour]:
                    curr_dist,deep_node = dfs2(neighbour)

                    if curr_dist + 1 > max_dist:
                        max_dist = curr_dist + 1
                        deepest_node = deep_node

            return max_dist,deepest_node

        dist,imm_node = dfs1(root)
        max_dist,final_node = dfs2(imm_node)

        return max_dist

