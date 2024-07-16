'''
-> My sol mimics the iterator functionality to some extent
-> However theis approach properly makes use of 'iterators' and 'generators'
'''

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.iter = self.in_order(root)
        self.nxt = next(self.iter,None)
        '''
        -> None acts as def value of next when 'iterator' runs out of value
        -> i.e., this case arises in this case when 'StopIteration Error' is thrown
        '''

    def in_order(self,node):
        if node:
            yield from self.in_order(node.left)
            yield node.val
            yield from self.in_order(node.right)

    def next(self) -> int:
        res,self.nxt = self.nxt,next(self.iter,None)
        return res

    def hasNext(self) -> bool:
        return self.next is not None

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()