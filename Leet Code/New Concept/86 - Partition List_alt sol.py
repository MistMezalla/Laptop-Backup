'''
-> The space complexity diff bet "queue" and "dummy" based implementation lies in the fact that
    -> "queue(deque)" will create new node of the "curr node's val" passed while appending into queue
    -> Note:- Notion of passing node and node.val will save space in queue implementation is false; hence O(n) space
    -> In case "dummy" implementation no such new nodes are been created hence O(1) space
'''

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        low_part = ListNode(0)
        higher_part = ListNode(0)
        bef,after = low_part,higher_part

        while head:
            if head.val < x:
                bef.next,bef = head, head
            else:
                after.next,after = head,head

            head = head.next

        after.next = None
        bef.next = higher_part.next



        return low_part.next