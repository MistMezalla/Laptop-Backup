'''
-> Made the blunder of ignoring the worst case T(n) of Quick sort
    -> considered O(nlogn)
    -> Actually is :- O(n**2)
-> Another Blunder(though not completely my fault):- O(1) space to be used solve
    -> considered O(1) to be the total space
    -> Actually when constraint:- O(1) implies additional space req (in the form of an additional data str) and
    not primary space of the program to be used.
'''
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        slow,fast = head,head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)

        return self.merge(left,right)

    def merge(self,l1,l2):
        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        tail.next = l1 if l1 else l2

        return dummy.next

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

nums = [5,4,1,2,3,8,7,4,6,0]
head = build_linked_list(nums)
sol = Solution()
new_head = sol.sortList(head)
print_linked_list(new_head)

