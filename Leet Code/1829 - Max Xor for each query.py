class Solution:
    def getMaximumXor(self, nums: list[int], maximumBit: int) -> list[int]:
        # curr_xor = nums[0]
        #
        # def bits_toggler(num):
        #     i = 0
        #     # bin_num = bin(num)
        #     while i < maximumBit:
        #         num = num ^ (1 << i)
        #         i += 1
        #
        #     return num
        #
        # res = [bits_toggler(curr_xor)]
        # for i in range(1,len(nums)):
        #     curr_xor ^= nums[i]
        #     res.append(bits_toggler(curr_xor))
        #
        # # res = []
        # # for pf in pf_xor:
        # #     res.append(bits_toggler(pf))
        #
        # res.reverse()
        # return res

        #optimised code
        xor_product = 0
        for num in nums:
            xor_product ^= num

        def bits_toggler(num):
            i = 0
            # bin_num = bin(num)
            while i < maximumBit:
                num = num ^ (1 << i)
                i += 1

            return num

        res = []
        for i in range(len(nums)-1,-1,-1):
            res.append(bits_toggler(xor_product))

            xor_product ^= nums[i]

        return res



sol = Solution()
print(sol.getMaximumXor(nums = [1,2,2,3], maximumBit = 2))