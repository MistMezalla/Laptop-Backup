class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        length = 1 << n - 1

        inv_cnt = 0
        while k > 1:
            if k == length // 2 + 1:
                return '1' if inv_cnt % 2 == 0 else '0'

            elif k > length // 2 +1 :
                k = length - k + 1
                inv_cnt += 1

            length //= 2

        return '0' if inv_cnt % 2 == 0 else '1'