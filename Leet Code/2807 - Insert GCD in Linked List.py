'''
-> To test the below code we have to create helper functions to build linked list, print linked list
'''
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

from typing import Optional
from math import gcd
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head

        Head = head
        while Head.next:
            gcd_node = ListNode(gcd(Head.val,Head.next.val))
            gcd_node.next = Head.next
            Head.next = gcd_node
            Head = gcd_node.next


        return head

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


nums = [18,6,10,3]
head = build_linked_list(nums)
print_linked_list(head)
print()
sol = Solution()
new_head = sol.insertGreatestCommonDivisors(head)
print_linked_list(new_head)
print()










