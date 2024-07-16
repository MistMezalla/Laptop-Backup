from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        m1 = 0
        m2 = 0

        node = l1
        while node:
            m1+=1
            node = node.next

        node = l2
        while node:
            m2 += 1
            node = node.next

        diff = m1 - m2

        node = None
        st = None
        if diff>=0:
            st = l1
            c1 = l1
            c2 = l2
        else:
            st = l2
            c1 = l2
            c2 = l1

        ind = 0
        rem = []
        while ind != abs(diff):
            rem.append(c1)
            node, c1 = c1,c1.next
            ind += 1

        carry_over = 0
        carry = 0

        while c2:
            data = c1.val + c2.val
            c1.val = data % 10
            carry = data // 10
            if node:
                node.val += carry
            node = c1
            c1,c2 = c1.next,c2.next

        for i in range(len(rem) - 1,-1,-1):
            data = rem[i].val + carry_over
            rem[i].val = data % 10
            carry_over = data // 10

        if carry_over != 0:
            node = ListNode(carry_over,st)
            st = node

        return st

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

num1 = [0]
num2 = [0]

head1 = build_linked_list(num1)
head2 = build_linked_list(num2)

sol = Solution()
new_head = sol.addTwoNumbers(head1,head2)
print_linked_list(new_head)