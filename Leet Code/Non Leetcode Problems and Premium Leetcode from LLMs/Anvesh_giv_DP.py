class Solution:
    def __init__(self):
        self.MOD = 998244353

    def solve_game_2048(self, max_y):
        # DP array where dp[i] means number of ways to achieve score i
        dp = [0] * (max_y + 1)
        dp[0] = 1  # There's 1 way to make score 0 (by doing nothing)

        # Process all powers of 2 (tile values)
        x = 2
        while x <= max_y:
            # Start from the back to prevent overcounting in the same iteration
            for y in range(max_y, x - 1, -1):
                dp[y] = (dp[y] + dp[y - x]) % self.MOD
            x *= 2  # Go to the next power of 2

        return dp

def main():
    sol = Solution()
    t = int(input())  # Read number of test cases
    queries = list(map(int, input().split()))  # Read all queries

    max_y = max(queries)  # Find the maximum Y in the queries
    dp = sol.solve_game_2048(max_y)  # Precompute dp up to max_y

    # Output the result for each query
    for y in queries:
        print(dp[y])

main()
