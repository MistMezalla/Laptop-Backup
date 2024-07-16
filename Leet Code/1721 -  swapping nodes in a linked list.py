'''
-> Though O(n) but my solution is two pass
-> Faster is possible in one pass
'''
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        ptr = None
        node = head
        while node:
            n+=1
            if n == k:
                ptr = node
            node = node.next

        node = head
        pos = n-k+1
        n = 1
        while n != pos:
            n+=1
            node = node.next

        node.val, ptr.val = ptr.val, node.val

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

nums = [7,9,6,6,7,8,3,0,9,5]
head = build_linked_list(nums)
sol = Solution()
new_head = sol.swapNodes(head,8)
print_linked_list(new_head)