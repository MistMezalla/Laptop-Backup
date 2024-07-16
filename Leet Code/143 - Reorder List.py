from typing import Optional
from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = deque()

        node = head
        while node:
            stack.append(node)
            node = node.next

        curr = head
        prev = head
        while curr!=stack[-1] and prev != stack[-1]:
            prev = curr
            curr = curr.next

            node = stack.pop()
            prev.next = node
            node.next = curr

        curr.next = None

        return head

def build_linked_list(nums):
    if not nums:
        return None
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

nums = [1]
head = build_linked_list(nums)
sol = Solution()
new_head = sol.reorderList(head)
print_linked_list(new_head)

