from typing import Optional
from collections import deque
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = deque()
        ptr = head
        while ptr:
            while stack and stack[-1].val < ptr.val:
                stack.pop()
            stack.append(ptr)
            ptr = ptr.next

        prev = None
        while stack:
            ptr = stack.pop()
            ptr.next = prev
            prev = ptr

        return ptr

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

nums = [3,1,2,5,4]
head = build_linked_list(nums)
sol = Solution()
new_head = sol.removeNodes(head)
print_linked_list(new_head)
print()




