'''
-> The Greedy approach is right but has to be improved to get an optimal sol
-> The Greedy approach:-
    -> Consider the example nums = [2, 6, 8, 3, 4, 5, 1], let's try to build the increasing subsequences starting with
    an empty one: sub1 = [].
    ->Let pick the first element, sub1 = [2].
    ->6 is greater than previous number, sub1 = [2, 6]
    ->8 is greater than previous number, sub1 = [2, 6, 8]
    ->3 is less than previous number, we can't extend the subsequence sub1, but we must keep 3 because in the future
    there may have the longest subsequence start with [2, 3], sub1 = [2, 6, 8], sub2 = [2, 3].
    ->With 4, we can't extend sub1, but we can extend sub2, so sub1 = [2, 6, 8], sub2 = [2, 3, 4].
    ->With 5, we can't extend sub1, but we can extend sub2, so sub1 = [2, 6, 8], sub2 = [2, 3, 4, 5].
    ->With 1, we can't extend neighter sub1 nor sub2, but we need to keep 1, so sub1 = [2, 6, 8], sub2 = [2, 3, 4, 5],
    sub3 = [1].
    ->Finally, length of longest increase subsequence = len(sub2) = 4.
    In the above steps, we need to keep different sub arrays (sub1, sub2..., subk) which causes poor performance.
-> Bin Search on Greedy approach:-
    ->But we notice that we can just keep one sub array, when new number x is not greater than the last element of the
    subsequence sub, we do binary search to find the smallest element >= x in sub, and replace with number x.
    ->Let's run that example nums = [2, 6, 8, 3, 4, 5, 1] again:
    Let pick the first element, sub = [2].
    ->6 is greater than previous number, sub = [2, 6]
    ->8 is greater than previous number, sub = [2, 6, 8]
    ->3 is less than previous number, so we can't extend the subsequence sub. We need to find the smallest number >= 3 in
    sub, it's 6. Then we overwrite it, now sub = [2, 3, 8].

-> Note: though the subseq changes but we are to return only the len and not the subseq itself. Hence correct.
'''
'''
Revise = 2
Resolve = 1
'''
from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        seq = [nums[0]]

        def bin_search(x: int):
            left = 0
            right = len(seq)- 1

            while right - left > 1:
                mid = (left+right) // 2

                if seq[mid] == x:
                    return mid
                if seq[mid] > x:
                    right = mid - 1
                else:
                    left = mid + 1

            if seq[left] >= x:
                return left
            else:
                return right


        for i in range(1,len(nums)):
            if nums[i] > seq[-1]:
                seq.append(nums[i])
            # else:
            #     seq[bin_search(nums[i])] = nums[i]
            else:
                ind = bisect_left(seq,nums[i])
                seq[ind] = nums[i]

        return len(seq)

sol = Solution()
print(sol.lengthOfLIS([10,9,2,5,3,7,101,18]))
print(sol.lengthOfLIS([2,6,8,3]))
print(sol.lengthOfLIS([2,1,3,9,7,8]))
print(sol.lengthOfLIS([7]))
print(sol.lengthOfLIS([7,7,7,7,7,7,7]))
print(sol.lengthOfLIS([0,1,0,3,2,3]))

