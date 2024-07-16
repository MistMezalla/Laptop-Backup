from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(start,end):
            curr,prev = start,None

            while curr != end:
                curr.next,prev,curr = prev,curr,curr.next

            return prev

        dummy = ListNode(0)
        dummy.next = head
        prev_grp_end = dummy

        grp_len = 1
        ind = 0
        node = head
        grp_start = next_grp_start = None
        while node:
            node = prev_grp_end

            for _ in range(grp_len):
                node = node.next
                ind += 1
                if node.next is None:
                    if not ind & 1:
                        next_grp_start = node.next
                        grp_start = prev_grp_end.next

                        new_grp_start = reverse(grp_start, next_grp_start)
                        prev_grp_end.next = new_grp_start
                        grp_start.next = next_grp_start

                        prev_grp_end = grp_start

                    return dummy.next

            next_grp_start = node.next
            grp_start = prev_grp_end.next
            if grp_len % 2 == 0:
                new_grp_start = reverse(grp_start,next_grp_start)

                prev_grp_end.next = new_grp_start
                grp_start.next = next_grp_start
                prev_grp_end = grp_start
            else:
                prev_grp_end = node


            grp_len += 1

            ind = 0

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
head = create_linked_list([1,2,3,4,5,6,7,8,9,10])
k = 3
print("Original list:")
print_linked_list(head)

sol = Solution()
new_head = sol.reverseEvenLengthGroups(head)
print("Reversed list in k-groups:")
print_linked_list(new_head)
