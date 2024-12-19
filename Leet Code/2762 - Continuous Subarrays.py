import heapq
class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        window_st = window_end = 0
        window = [(-nums[0],0)]

        cnt = 0
        for i in range(1,len(nums)):
            num = nums[i]
            curr_window_max = -window[0][0]
            if abs(num - curr_window_max) <= 2:
                window_end += 1
                heapq.heappush(window,(-num,i))

            else:
                n = window_end - window_st + 1
                cnt += n*(n+1)//2

                while True:
                    curr_window_max = -window[0][0]
                    if abs(num - curr_window_max) > 2:
                        window_st = heapq.heappop(window)[1]
                    elif window[0][1] <= window_st:
                        heapq.heappop(window)
                    else:
                        m = window_end - window_st
                        cnt -= m * (m+1) // 2
                        window_st += 1
                        window_end += 1
                        break
                heapq.heappush(window,(-num,i))

        n = window_end - window_st + 1
        cnt += n * (n + 1) // 2
        return cnt

sol = Solution()
print(sol.continuousSubarrays([5,4,2,4]))
print(sol.continuousSubarrays([5,4,3,2,4]))
print(sol.continuousSubarrays([1,2,3]))





