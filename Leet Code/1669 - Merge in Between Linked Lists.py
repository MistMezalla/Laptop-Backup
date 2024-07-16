
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        cntr = 0
        node = list1

        while node and cntr != a-1:
            cntr += 1
            node = node.next

        pt_bef = node

        while cntr != b+1:
            cntr += 1
            node = node.next

        pt_after = node

        node = list2
        while node.next:
            node = node.next

        pt_last = node

        pt_bef.next = list2
        pt_last.next = pt_after

        return list1

from typing import Optional
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

arr1 = [10,1,13,6,9,5]
list1 = build_linked_list(arr1)
arr2=[1000000,1000001,1000002]
list2 = build_linked_list(arr2)

print_linked_list(list1)
print()
print_linked_list(list2)
print()

sol = Solution()
res_list = sol.mergeInBetween(list1,3,4,list2)
print_linked_list(res_list)
print()

