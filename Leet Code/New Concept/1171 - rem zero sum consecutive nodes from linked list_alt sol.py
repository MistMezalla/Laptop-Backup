'''
-> This approach makes use of
    -> prefix sum
    -> hashing to store the location of starting pt of seq to be del
-> Complexity same as mine,i.e, O(n) and O(n)
-> However my stack base approach has too much of complications in terms of huge number of edge cases to be handled
due to the framework of my stack based logic
'''
#My incomplete code based on stack based logic
'''
from typing import Optional
from collections import deque
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = deque()
        curr_sum = 0
        node = head

        while node:
            if node.val == 0:
                node = node.next
                continue
            while stack:
                if node.val * stack[-1].val < 0:
                    TBD_node = stack.pop()
                    curr_sum = node.val + TBD_node.val
                    if curr_sum * TBD_node.val < -1:

'''

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hash_nodes = {}
        pf_sum = 0
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        while curr:
            pf_sum += curr.val
            if pf_sum in hash_nodes:
                prev = hash_nodes[pf_sum]
                to_rem = prev.next
                p = pf_sum + to_rem.val if to_rem else 0
                while p != pf_sum:
                    del hash_nodes[p]
                    to_rem = to_rem.next
                    p += to_rem.val if to_rem else 0
                prev.next = curr.next

            else:
                hash_nodes[pf_sum] = curr
            curr = curr.next

        return dummy.next

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
head = create_linked_list([-1,-2,7,-4,8,-2,5,-9,12,-6,-2,3])
k = 3
print("Original list:")
print_linked_list(head)

sol = Solution()
new_head = sol.removeZeroSumSublists(head)
print("Reversed list in k-groups:")
print_linked_list(new_head)
