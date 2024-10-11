class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        max_ind = None
        max_num = float('-inf')
        min_ind = None
        min_num = float('inf')

        for ind,elem in enumerate(nums):
            if elem > max_num:
                max_num = elem
                max_ind = ind

            if elem < min_num:
                min_num = elem
                min_ind = ind

        st = 0
        end = len(nums)-1
        op = 0

        max_dist_st = max_ind - st + 1
        max_dist_end = end - max_ind + 1
        min_dist_st = min_ind - st + 1
        min_dist_end = end - min_ind + 1

        min_op = min(max_dist_end,min_dist_end,max_dist_st,min_dist_st)
        op += min_op
        if max_num == min_num:
            return op

        if max_dist_st == min_op:
            st += max_dist_st
            op += min(min_ind - st,end - min_ind) + 1

        elif max_dist_end == min_op:
            end -= max_dist_end
            op += min(min_ind - st,end - min_ind) + 1

        elif min_dist_st == min_op:
            st += min_dist_st
            op += min(max_ind - st, end - max_ind) + 1

        else:
            end -= min_dist_end
            op += min(max_ind - st, end - max_ind) + 1

        return op

sol = Solution()
print(sol.minimumDeletions(nums = [2,10,7,5,4,1,8,6]))
print(sol.minimumDeletions(nums = [0,-4,19,1,8,-2,-3,5]))
print(sol.minimumDeletions(nums = [101]))
print(sol.minimumDeletions([9,1,2,3,4]))






