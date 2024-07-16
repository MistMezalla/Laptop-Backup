from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
        prev,curr = None,head
        p1,p2,p3 = None,None,None
        res = [-1,-1]
        ind = 0

        while curr:
            ind += 1
            if prev and curr.next:
                if (curr.val > prev.val and curr.val > curr.next.val) or (curr.val < prev.val and curr.val < curr.next.val):
                    if not p1:
                        p1 = ind
                    else:
                        p3 = p2
                        p2 = ind

                    min_dist = p2 - p3 if p2 and p3 else -1
                    max_dist = p2 - p1 if p1 and p2 else -1

                    if res[0] == -1:
                        res[0] = min_dist
                    else:
                        res[0] = min(res[0],min_dist)
                    res[1] = max(res[1],max_dist)
                    if not p3:
                        res[0] = res[1]


            prev,curr = curr,curr.next


        return res

def build_linked_list(nums):
    if not nums:
        return None
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

nums = [3,8,1,3,9,2,2,5,9]
head = build_linked_list(nums)
sol = Solution()
print(sol.nodesBetweenCriticalPoints(head))
