from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def swap(Head: Optional[ListNode]):
            n1 = Head
            n2 = Head.next

            n1.next = n2.next
            n2.next = n1

            return n2

        if (head is None) or (head.next is None):
            return head

        node = head
        prev = None
        while node:
            if node == head:
                head = swap(node)
                prev = node
                node = node.next


            elif node.next is not None:
                prev.next = swap(node)
                prev = node
                node = node.next



            else:
                prev = node
                node = node.next

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

nums = [5]
head = build_linked_list(nums)
sol = Solution()
new_head = sol.swapPairs(head)
print_linked_list(new_head)



