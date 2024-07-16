'''
-> Slightly better approach than mine as all the conditionals my code are handled implicitly in the swap logic
-> Hence faster
'''
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        curr = head
        new_head = ListNode()
        prev = new_head

        while curr and curr.next:
            prev.next = curr.next
            curr.next = prev.next.next
            prev.next.next = curr

            prev = curr
            curr = curr.next

        return new_head.next

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

nums = [5,7,2,1,4]
head = build_linked_list(nums)
sol = Solution()
new_head = sol.swapPairs(head)
print_linked_list(new_head)