from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(0,head)
        curr = dummy

        for _ in range(n):
            head = head.next

        while head:
            head = head.next
            curr = curr.next

        curr.next = curr.next.next

        return dummy.next
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
list1 = create_linked_list([1,2,3,4,5])

new_list = sol.removeNthFromEnd(list1,4)
print_linked_list(new_list)

