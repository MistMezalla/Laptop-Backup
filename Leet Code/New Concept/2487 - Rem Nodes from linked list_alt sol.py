'''
-> Basic Intuition lies in using NGE concept
-> However this unconventional method makes use of the fact that rev list and then traversing down the list can solve
the problem in constant space
'''
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr,prev = head,None
        while curr:
            curr.next,prev,curr = prev,curr,curr.next

        curr = prev.next
        prev.next = None # handles the case that the last node of og list will be in the res list always irrespective
                         # of the input size an pattern

        while curr:
            temp = curr.next
            if curr.val >= prev.val: # all the values greater than the last values will be the part of the res
                curr.next = prev
                prev = curr

            curr = temp

        return prev