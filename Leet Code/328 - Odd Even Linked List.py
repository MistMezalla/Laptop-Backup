from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        odd = head
        even = head.next
        st = even

        while even:
            odd.next = odd.next.next
            if odd.next:
                odd = odd.next


            if even.next:
                even.next = even.next.next
            even = even.next


        odd.next = st
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

nums = []
head = build_linked_list(nums)
sol = Solution()
new_head = sol.oddEvenList(head)
print_linked_list(new_head)
