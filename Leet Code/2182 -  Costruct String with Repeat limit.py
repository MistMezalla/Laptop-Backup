'''
-> Note the string concatenation is expensive job wrt appending char to list of char and then finally joining them
'''
class Solution1:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq_char = [0] * 26

        for ch in s:
            freq_char[ord(ch) - ord("a")] += 1

        ind = 25
        res = ""
        while ind >= 0:
            if freq_char[ind] <= 0:
                ind -= 1
                continue

            used = min(freq_char[ind],repeatLimit)
            res += chr(ind + ord("a")) * used
            freq_char[ind] -= used

            if freq_char[ind] > 0:
                smaller_ind = ind - 1

                while smaller_ind >= 0 and freq_char[smaller_ind] <= 0:
                    smaller_ind -= 1

                if smaller_ind < 0:
                    break
                res += chr(smaller_ind + ord("a"))
                freq_char[smaller_ind] -= 1

        return res

import heapq
from collections import Counter
class Solution2:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        max_heap = [(-ord(ch),cnt) for ch,cnt in Counter(s).items()]
        heapq.heapify(max_heap)

        res = []
        while max_heap:
            elem = heapq.heappop(max_heap)
            char = chr(-elem[0])
            cnt = elem[1]

            used = min(cnt,repeatLimit)
            res.append(char * used)
            cnt -= used

            if cnt > 0 and max_heap:
                smaller_elem = heapq.heappop(max_heap)
                smaller_char = chr(-smaller_elem[0])
                smaller_cnt = smaller_elem[1]

                res.append(smaller_char)
                if smaller_cnt > 1:
                    heapq.heappush(max_heap,(-ord(smaller_char),smaller_cnt-1))
                heapq.heappush(max_heap,(-ord(char),cnt))

        return "".join(res)

sol = Solution2()
print(sol.repeatLimitedString(s = "cczazcc", repeatLimit = 3))