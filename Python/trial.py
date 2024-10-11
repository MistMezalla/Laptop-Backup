def kmp_search(text, pattern):
    # Function to build the longest prefix suffix (lps) array
    def build_lps(pattern):
        lps = [0] * len(pattern)  # Initialize lps array to all 0s
        length = 0  # Length of the previous longest prefix suffix
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    # Lengths of text and pattern
    n = len(text)
    m = len(pattern)

    # Build the lps array for the pattern
    lps = build_lps(pattern)

    i = 0  # index for text
    j = 0  # index for pattern

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            print(f"Pattern found at index {i - j}")
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1] #shifting by j - len(longest perix) no. of places
            else:
                i += 1

# Example usage
text = "abaababaabacabaababaabaababaababaabababaababaabaababaababaabaaa"
pattern = "abaababaabaab"
kmp_search(text, pattern)
