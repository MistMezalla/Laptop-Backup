from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev= head, None

        while curr:
            curr.next,prev,curr = prev, curr, curr.next

        head = prev
        curr = prev
        prev = None

        carry = 0
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

            data = prev.val
            prev.val = data*2%10 + carry
            carry = data * 2 // 10

        if carry:
            curr = ListNode(carry,prev)
            return curr

        return prev

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

nums = [9,9,9]
head = build_linked_list(nums)
sol = Solution()
new_head = sol.doubleIt(head)
print_linked_list(new_head)


