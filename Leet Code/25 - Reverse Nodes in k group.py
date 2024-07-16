from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(start,end):
            prev,curr = None,start

            while curr!=end:
                curr.next,prev,curr = prev,curr,curr.next

            return prev

        dummy = ListNode(0)
        dummy.next = head
        prev_grp_end = dummy

        while True:
            node = prev_grp_end
            for _ in range(k):
                node = node.next
                if node is None:
                    return dummy.next

            next_group_start = node.next
            grp_start = prev_grp_end.next

            new_grp_start = reverse(grp_start,next_group_start)

            prev_grp_end.next = new_grp_start
            grp_start.next = next_group_start

            prev_grp_end = grp_start


def create_linked_list(arr):
    dummy = ListNode(0)
    current = dummy
    for value in arr:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

def print_linked_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "")
        head = head.next
    print()

# Example usage
head = create_linked_list([1, 2, 3, 4, 5,6])
k = 3
print("Original list:")
print_linked_list(head)

sol = Solution()
new_head = sol.reverseKGroup(head, k)
print("Reversed list in k-groups:")
print_linked_list(new_head)


