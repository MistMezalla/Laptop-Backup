'''
-> The intuition was almost thought except the concept of tail pointer
'''
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head is None:
            return None
        return self._sortedListToBST(head,None)

    def _sortedListToBST(self, head: Optional[ListNode], tail: Optional[ListNode]) -> Optional[TreeNode]:
        if head == tail:
            return None

        fast = head
        slow = head

        while fast != tail and fast.next != tail:
            fast = fast.next.next
            slow = slow.next

        node = TreeNode(slow.val)
        node.left = self._sortedListToBST(head,slow)
        node.right = self._sortedListToBST(slow.next,tail)

        return node

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

def build_linked_list(nums):
    head = ListNode(nums[0])

    node = head
    for i in range(1,len(nums)):
        node.next = ListNode(nums[i])
        node = node.next

    return head

def print_linked_list(head: Optional[ListNode]):
    while head:
        print(head.val,end = ' ')
        head = head.next

arr1 = [-10,-3,0,5,9]
list1 = build_linked_list(arr1)

sol = Solution()
new_root = sol.sortedListToBST(list1)
print_in_order(new_root)
print()

