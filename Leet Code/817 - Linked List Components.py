from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def numComponents(self, head: Optional[ListNode], nums: list[int]) -> int:
        num_set = set(nums)

        flag = False
        res = 0
        while head:
            if head.val not in num_set and flag:
                res+=1
                flag = False
            elif head.val in num_set:
                flag = True
            head = head.next

        if flag:
            res += 1
        return res
