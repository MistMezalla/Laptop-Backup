from typing import Optional
from collections import deque
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> list[int]:
        ans = []
        ind = -1

        stack = deque()

        node = head
        while node:
            i = ind
            while stack and stack[-1].val < node.val:
                if ans[i] == 0:
                    ans[i] = node.val
                    stack.pop()
                i-=1


            ans.append(0)
            stack.append(node)
            node = node.next
            ind += 1

        return ans

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

nums = [9,7,6,7,6,9]
head = build_linked_list(nums)
sol = Solution()
print(sol.nextLargerNodes(head))


