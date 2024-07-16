from typing import Optional
from random import randint
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

        node = head
        n = 0
        while node:
            n+=1
            node = node.next

        self.size = n


    def getRandom(self) -> int:
        pos = randint(1,self.size)
        node = self.head

        ind = 1
        while ind != pos:
            node = node.next
            ind += 1

        return node.val

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

nums = [1,2,3]
head = build_linked_list(nums)
sol = Solution(head)
print(sol.getRandom())
# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()