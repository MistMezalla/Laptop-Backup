from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode(0,head)
        prev = dummy

        node = head
        flag = False
        while node.next:
            if node.val == node.next.val:
                flag = True
                node = node.next
            else:
                if flag:
                    node = node.next
                    prev.next = node
                    flag = False
                else:
                    prev = node
                    node = node.next


        if flag:
            node = node.next
            prev.next = node



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
list1 = create_linked_list([2,2,3,3,4,4,5])
new_list = sol.deleteDuplicates(list1)
print_linked_list(new_list)
