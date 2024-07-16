class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        hash = {}

        for i in range(len(arr)):
            if arr[i] in hash:
                hash[arr[i]] += 1
            else:
                hash[arr[i]] = 1

        n = 1
        for i in range(len(arr)):
            if hash[arr[i]] == 1:
                if n==k:
                    return arr[i]
                n+=1

        return ""
