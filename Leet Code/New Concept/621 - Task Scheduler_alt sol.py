class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        chr_freq = [0] * 26

        for task in tasks:
            chr_freq[ord(task) - ord('A')] += 1

        chr_freq.sort()

        gap = chr_freq[25] - 1
        idles = gap * n

        for i in range(24, -1, -1):
            idles -= min(gap,chr_freq[i])

        return len(tasks) + idles if idles >= 0 else len(tasks)

sol = Solution()
print(sol.leastInterval(tasks = ["A","A","A","B","B","B"], n = 2))
print(sol.leastInterval(tasks = ["A","C","A","B","D","B"], n = 1))
print(sol.leastInterval( tasks = ["A","A","A", "B","B","B"], n = 3))
print(sol.leastInterval( tasks = ["A","A","A",'B','B','B','C','C'], n = 2))