class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'

        length = (1 << n)

        if k == length // 2:
            return '1'
        elif k < length // 2:
            return self.findKthBit(n-1,k)
        else:
            return '1' if self.findKthBit(n-1,length - k) == '0' else '0'
        