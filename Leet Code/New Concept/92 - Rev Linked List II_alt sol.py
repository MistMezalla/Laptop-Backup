'''
-> One pass implies that a node is visited at most one time.
-> One pass has no relation to the direction of traversal and list complete traversal

-> Pointer manipulation involves the concept of correctness of loop invariant to some extent,i.e, on each iteration
the intermediate list condition is valid ans and not the case where the valid ans is generated upon the completion
of loop only.
'''
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0,head)
        prev = dummy

        for _ in range(left-1):
            prev = prev.next

        curr = prev.next
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next