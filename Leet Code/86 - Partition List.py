from typing import Optional
from collections import deque
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        low_que = deque()
        higher_que = deque()

        while head:
            if head.val < x:
                low_que.append(head)
            else:
                higher_que.append(head)
            head = head.next

        if low_que:
            head = low_que[0]
        elif higher_que:
            head = higher_que[0]
        else:
            return head

        prev = None
        while low_que:
            if prev is None:
                prev = low_que.popleft()
            node = low_que.popleft() if low_que else None
            prev.next = node
            prev = node if node else prev

        while higher_que:
            if prev is None:
                prev = higher_que.popleft()
            node = higher_que.popleft() if higher_que else None
            prev.next = node
            prev = node

        if prev:
            prev.next = None


        return head

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
head = create_linked_list([6,1,4,3,2,5,2])
k = 3
print("Original list:")
print_linked_list(head)

sol = Solution()
new_head = sol.partition(head, 2)
print("Reversed list in k-groups:")
print_linked_list(new_head)





