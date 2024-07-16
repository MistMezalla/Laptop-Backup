'''
-> The code of my solution was of O(n) in terms of space
-> Better approach lies in using
    -> fast and slow ptrs
    -> reversing 2nd half to find res
'''
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        curr, prev = slow,None
        while curr:
            curr.next,prev,curr = prev,curr,curr.next

        max_sum = 0
        while prev:
            max_sum = max(max_sum,head.val + prev.val)
            head = head.next
            prev = prev.next

        return max_sum

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

nums = [5,4,2,1]
head = build_linked_list(nums)
sol = Solution()
print(sol.pairSum(head))