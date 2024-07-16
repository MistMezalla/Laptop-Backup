'''
-> Basic Logic of solving the qn was right but in time constraint cldn't come up with spiral traversal algo
'''

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> list[list[int]]:
        res = [[-1]*n for _ in range(m)]

        top = 0
        bottom = m-1
        left = 0
        right = n-1

        while top<= bottom and left <= right:
            for i in range(left,right+1):
                if head:
                    res[top][i] = head.val
                    head = head.next
                else:
                    return res
            top += 1

            for i in range(top,bottom+1):
                if head:
                    res[i][right] = head.val
                    head = head.next
                else:
                    return res
            right -= 1

            if top<=bottom:
                for i in range(right,left-1,-1):
                    if head is None:
                        return res
                    res[bottom][i] = head.val
                    head = head.next
            bottom -= 1

            if left<=right:
                for i in range(bottom, top-1,-1):
                    if head is None:
                        return res
                    res[i][left] = head.val
                    head = head.next
            left += 1


        return res


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

nums = [5,4,2,1,15,8,9,6,4,0,2,12,27]
head = build_linked_list(nums)
sol = Solution()
print(sol.spiralMatrix(3,5,head))




