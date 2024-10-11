class Solution:
    def minDeletions(self, s: str) -> int:
        hash = [0] * 26

        for chr in s:
            hash[ord(chr) - ord('a')] += 1

        hash = [x for x in hash if x != 0]

        hash_set = list(set(hash))
        hash.sort()

        del_cnt = 0
        # for _ in range(len(hash)):
        while True:
            flag_rem = False
            for i in range(len(hash)-1):
                if hash[i] == hash[i+1] and hash[i] != 0:
                    hash[i] -= 1
                    del_cnt += 1
                    flag_rem = True

            if not flag_rem:
                break

        return del_cnt

sol = Solution()
print(sol.minDeletions("aaabbbcc"))
print(sol.minDeletions("aaaaabbbbcccddddeeefffffgggggg"))
print(sol.minDeletions("aaaaceb"))


