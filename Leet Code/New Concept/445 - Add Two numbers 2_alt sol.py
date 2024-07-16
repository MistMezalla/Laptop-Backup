'''
-> Instead of reversing the lists - same function can be mimiced by using stack
'''

from typing import Optional
from collections import deque
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1,stack2 = deque(),deque()

        node = l1
        m1 = 0
        while node:
            stack1.append(node.val)
            m1 += 1
            node= node.next

        node= l2
        m2 = 0
        while node:
            stack2.append(node.val)
            m2 += 1
            node = node.next

        head = None

        carry = 0
        while stack1 and stack2:
            data = stack1.pop() + stack2.pop() + carry
            node = ListNode(data % 10,head)
            head = node
            carry = data // 10

        while stack1:
            data = stack1.pop() + carry
            node = ListNode(data % 10, head)
            head = node
            carry = data // 10

        while stack2:
            data = stack2.pop() + carry
            node = ListNode(data%10, head)
            head = node
            carry = data // 10

        if carry:
            node = ListNode(carry, head)
            head = node


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

num1 = [1]
num2 = [9,9]

head1 = build_linked_list(num1)
head2 = build_linked_list(num2)

sol = Solution()
new_head = sol.addTwoNumbers(head1,head2)
print_linked_list(new_head)




