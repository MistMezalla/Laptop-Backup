class Solution:
    def reverseBits(self, n: int) -> int:
        n_bin = bin(n)[2:]
        n_bin = "0" * (32 - len(n_bin)) + n_bin
        n_bin = n_bin[::-1]
        n_bin = "0b" + n_bin
        return int(n_bin,2)

sol = Solution()
print(sol.reverseBits(43261596))
print(43261596 <= 2**31)

class Solution:
    def reverseBits(self, n: int) -> int:
        n_bin = bin(n)[2:]
        n_bin = "0" * (32 - len(n_bin)) + n_bin

        return int("0b" + self.bin_reverse(n_bin)[1], 2)

    def bin_reverse(self, bin_str: str):
        if len(bin_str) <= 1:
            return [1,bin_str]

        mid = len(bin_str) // 2

        left_part = self.bin_reverse(bin_str[:mid])
        right_part = self.bin_reverse(bin_str[mid:])

        return self.merge(left_part,right_part) # left and right part are tuples

    def merge(self,left_part,right_part):
        #right_part[1] = right_part[1] + "0" * left_part[0]

        right_part[1] = right_part[1] + left_part[1]

        return [right_part[0] + left_part[0], right_part[1]]

sol_dnc = Solution_DnC()
print(sol_dnc.reverseBits(43261596))


