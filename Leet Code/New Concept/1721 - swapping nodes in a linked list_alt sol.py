'''
-> In this approach made use of the fact that nodes to be swapped are equidistant fom the end pts on the linked list
'''
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast, slow = head,head

        for i in range (k-1):
            fast = fast.next

        req_pos = fast
        fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next

        slow.val,req_pos.val = req_pos.val,slow.val

        return head
