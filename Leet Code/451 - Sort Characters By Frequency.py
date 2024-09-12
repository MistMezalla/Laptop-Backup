class Solution:
    def frequencySort(self, s: str) -> str:
        hsh_char_freq = dict()

        for letter in s:
            if letter not in hsh_char_freq:
                hsh_char_freq[letter] = 1
            else:
                hsh_char_freq[letter] += 1

        hsh_char_freq = sorted(hsh_char_freq.items(), key = lambda item: item[1], reverse=True)

        res = ""
        for chr in hsh_char_freq:
            res += chr[0] * chr[1]

        return res

sol = Solution()
print(sol.frequencySort("tree"))
print(sol.frequencySort("ccbcabaad"))
print(sol.frequencySort("8"))
print(sol.frequencySort(s = "Aabb"))

