class Solution:
    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        st_ind = [i for i in range(len(nums))]
        end_ind = [i for i in range(len(nums))]


        for i in range(len(nums)-1):
            t1 = nums[i] & 1
            t2 = nums[i + 1] & 1

            if (t1 + t2) & 1:
                st_ind[i+1] = st_ind[i]

        for i in range(len(nums)-1,0,-1):
            t1 = nums[i] & 1
            t2 = nums[i-1] & 1

            if (t1+t2) & 1:
                end_ind[i-1] = end_ind[i]

        res = []
        for st,end in queries:
            if st >= st_ind[st] and end <= end_ind[st] and st >= st_ind[end] and end <= end_ind[end]:
                res.append(True)
            else:
                res.append(False)

        return res

sol = Solution()
print(sol.isArraySpecial([5,3,1,6,7,8,10,1,3],[[2,4],[2,6],[8,8],[5,7],[6,7]]))
