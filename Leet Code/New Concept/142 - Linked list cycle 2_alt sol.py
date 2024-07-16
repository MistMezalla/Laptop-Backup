'''
-> Usage of "Floyd's Cycle" Algo
-> wrt Qn 141
    -> reset slow head and move both by one unit(same pace) when meet first time
'''
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast = head,head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow==fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow

        return None

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to create a cycle in the linked list
def create_cycle(head, pos):
    if pos == -1:
        return head
    cycle_start = None
    current = head
    index = 0
    while current.next:
        if index == pos:
            cycle_start = current
        current = current.next
        index += 1
    current.next = cycle_start
    return head

# Helper function to find the start of the cycle
def find_cycle_start(head):
    solution = Solution()
    cycle_start = solution.detectCycle(head)
    if cycle_start:
        return cycle_start.val
    else:
        return None

# Example usage and testing
if __name__ == "__main__":
    # Create a linked list with a cycle
    values = [3, 2, 0, -4]
    head = create_linked_list(values)
    head = create_cycle(head, 1)  # Create a cycle starting at index 1

    # Find the start of the cycle
    cycle_start_val = find_cycle_start(head)
    print("Cycle starts at node with value:", cycle_start_val)

    # Create a linked list without a cycle
    values_no_cycle = [1, 2, 3, 4, 5]
    head_no_cycle = create_linked_list(values_no_cycle)

    # Find the start of the cycle (should return None)
    cycle_start_val_no_cycle = find_cycle_start(head_no_cycle)
    print("Cycle starts at node with value:", cycle_start_val_no_cycle)

