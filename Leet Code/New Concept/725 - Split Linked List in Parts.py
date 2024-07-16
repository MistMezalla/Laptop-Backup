from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> list[Optional[ListNode]]:
        n = 0
        node = head
        while node:
            n+=1
            node = node.next

        parts = [n//k]*k

        bal = n%k
        ind = 0
        while bal:
            parts[ind] += 1
            bal -= 1
            ind += 1

        node = head
        prev = None
        res = []
        for part in parts:
            if not head:
                res.append(head)
            else:
                for i in range(part):
                    prev = node
                    node = node.next
                prev.next = None
                res.append(head)
                head = node

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

nums = []
head = build_linked_list(nums)
sol = Solution()
res = sol.splitListToParts(head,7)
print(res)

for elem in res:
    print_linked_list(elem)
    print()








