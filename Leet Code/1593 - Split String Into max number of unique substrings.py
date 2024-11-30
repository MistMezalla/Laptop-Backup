'''
-> The below sol was just extension of typical backtracking template
-> For the crux of
'''
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen_substr = set()

        def gen_substrings(st):
            max_cnt = 0
            if st == len(s):
                return 0

            for end in range(st + 1, len(s) + 1):
                sub_str = s[st:end]

                if sub_str not in seen_substr:
                    seen_substr.add(sub_str)
                    max_cnt = max(max_cnt, 1 + gen_substrings(end))
                    seen_substr.remove(sub_str)

            return max_cnt

        return gen_substrings(0)


sol = Solution()

print(sol.maxUniqueSplit("wwwzfvedwfvhsww"))
print(sol.maxUniqueSplit("ababccc"))