class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        num_str_sorted = sorted(num_str,reverse=True)

        min_ind = None
        max_num = None
        for i in range(len(num_str)):
            if num_str_sorted[i] != num_str[i]:
                min_ind = i
                max_num = num_str_sorted[i]
                break

        if min_ind == None:
            return num

        max_ind = None
        for i in range(len(num_str) - 1,-1,-1):
            if num_str[i] == max_num:
                max_ind = i
                break

        num_str[min_ind], num_str[max_ind] = num_str[max_ind], num_str[min_ind]

        return int("".join(num_str))







sol = Solution()
print(sol.maximumSwap(2736))
