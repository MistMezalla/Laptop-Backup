def power(A: int, B: int, M: int) -> int:
    ans = 1
    while B:
        if B & 1:
            ans = (ans * A) % M
        A = (A * A) % M
        B >>= 1

    return ans



# Example usage:
print(power(2, 5, 13))  # Output: 6
print(power(3, 200, 50))  # Output: 1
print(power(2,11,1140))
