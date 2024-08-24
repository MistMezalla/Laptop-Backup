from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None

        node = head


        while node and node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next

        if head.val == val:
            head = head.next

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

list1 = create_linked_list([7,7,7,7,7])
list2 = create_linked_list([6,2,6,3,4,5,6])
list3 = create_linked_list([])

new_list = sol.removeElements(list2,6)
print_linked_list(new_list)
