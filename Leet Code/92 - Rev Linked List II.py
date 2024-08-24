from typing import Optional
from collections import deque
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return head

        stack = deque()
        prev = None
        node = head
        k = 1

        while node and k <= right:
            stack.append((prev,node))
            prev = node
            node = node.next
            k+=1


        st = stack[-1][1]

        curr = None
        while k>=left+1:
            k-=1
            prev,curr = stack.pop()
            curr.next = prev

        curr.next = node
        if prev:
            prev.next = st
        else:
            head = st

        return head

def create_linked_list(values):
    """Create a linked list from a list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    """Print values of linked list."""
    current = head
    while current:
        print(current.val, end=" -> " if current.next else " -> None\n")
        current = current.next

sol = Solution()
list1 = create_linked_list([1])
new_list = sol.reverseBetween(list1,1,1)
print_linked_list(new_list)


