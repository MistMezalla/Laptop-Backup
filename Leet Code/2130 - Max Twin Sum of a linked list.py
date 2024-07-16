from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        list = []
        node = head
        n = 0
        while node:
            list.append(node.val)
            node = node.next
            n+=1

        max_sum = 0
        # for i in range(n//2,n):
        #     twin_sum = list[i] + list[i%(n//2)]
        #     if twin_sum >= max_sum:
        #         max_sum = twin_sum

        for i in range(n//2):
            twin_sum = list[i] + list[n-1-i]
            if twin_sum >= max_sum:
                max_sum = twin_sum

        return max_sum

from typing import Optional
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




