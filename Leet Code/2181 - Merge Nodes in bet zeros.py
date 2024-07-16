from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        res = ListNode()
        current = res


        while node.next:
            data = 0
            while node.next.val:
                data += node.next.val
                node = node.next

            current.next = ListNode(data)
            current = current.next
            node = node.next


        return res.next

def build_linked_list(nums):
    head = ListNode(nums[0])

    node = head
    for i in range(1,len(nums)):
        node.next = ListNode(nums[i])
        node = node.next

    return head

def print_linked_list(head: Optional[ListNode]):
    while head:
        print(head.val,end = ' ')
        head = head.next

nums = [0,3,1,0,4,5,2,0]
head = build_linked_list(nums)
print_linked_list(head)
print()
sol = Solution()
new_head = sol.mergeNodes(head)
print_linked_list(new_head)
print()



