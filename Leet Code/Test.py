from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        ind = len(lists)
        i = 0
        while i < ind:
            l1 = lists[i]
            l2 = lists[i+1] if i+1 < ind else None

            dummy = ListNode(0)
            dummy.next = self.merge(l1,l2)
            lists.append(dummy.next)

            ind += 1
            i += 2

        return lists[-1] if lists else None

    def merge(self,l1,l2):
        res = ListNode(0)
        curr = res

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 if l1 else l2

        return res.next