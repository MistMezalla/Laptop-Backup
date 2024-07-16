'''
-> If tried to solve with Avl Tree implementation then not the optimal solution
-> Intuition:-
    -> Create sorted arr out of the nodes of the bst
    -> do bin search on the arr and find the root and its left and right child recursively
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        def in_order(node):
            if node:
                in_order(node.left)
                arr.append(node)
                in_order(node.right)

        def Build_bal_Bst(l,r):
            if l > r:
                return None

            mid = (l+r)//2
            node = arr[mid]
            node.left = Build_bal_Bst(l,mid-1)
            node.right = Build_bal_Bst(mid+1,r)

            return node

        in_order(root)
        return Build_bal_Bst(0,len(arr)-1)

def print_in_order(node):
    if node:
        print_in_order(node.left)
        print(node.val, end=' ')
        print_in_order(node.right)

def insert_into_bst(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root

root = None
elements = [1,None,2,None,3,None,4,None,None]
for el in elements:
    if el is not None:
        root = insert_into_bst(root, el)

sol = Solution()
new_root = sol.balanceBST(root)
print_in_order(new_root)
print()


