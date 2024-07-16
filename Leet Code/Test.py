from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def partition(start: ListNode, end: ListNode) -> ListNode:
            """
            Partitions the linked list around a pivot element.

            Args:
                start: The starting node of the sublist to partition.
                end: The node after the end of the sublist (exclusive).

            Returns:
                The new pivot node.
            """

            pivot = start
            current = start.next
            last_smaller = start  # Track the last smaller element

            while current != end:
                if current.val <= pivot.val:
                    # Swap values if current element is less than or equal to the pivot
                    current.val, last_smaller.next.val = last_smaller.next.val, current.val
                    last_smaller = last_smaller.next
                current = current.next

            # Swap the last smaller element (or pivot itself) with the element after the pivot
            last_smaller.next.val, pivot.val = pivot.val, last_smaller.next.val
            return last_smaller.next

        def quick_sort(start: ListNode, end: Optional[ListNode]) -> None:
            """
            Sorts a sublist of the linked list using Quick Sort recursively.

            Args:
                start: The starting node of the sublist to sort.
                end: The node after the end of the sublist (exclusive).
            """

            if start != end:
                pivot = partition(start, end)
                quick_sort(start, pivot)
                quick_sort(pivot.next, end)

        if not head or not head.next:
            return head  # Handle empty or single-node lists

        # Find the tail node (not strictly necessary, but can be useful for optimization)
        tail = head
        while tail.next:
            tail = tail.next

        quick_sort(head, tail)
        return head

def build_linked_list(nums):
    if not nums:
        return None
    head = ListNode(nums[0])

    node = head
    for i in range(1, len(nums)):
        node.next = ListNode(nums[i])
        node = node.next

    return head

def print_linked_list(head: Optional[ListNode]):
    """
    Prints the linked list values.
    """

    while head:
        print(head.val, end=' ')
        head = head.next
    print()

nums = [2, 3, 7, 1, 8, 4, 6, 5]
head = build_linked_list(nums)
sol = Solution()
new_head = sol.sortList(head)
print_linked_list(new_head)
