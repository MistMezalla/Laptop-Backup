'''
Resolved = 1
Revised = 1
'''
def one_D(nums, lo=0, hi=None):
    if hi is None:
        hi = len(nums) - 1

    if not nums:
        raise ValueError("The input array is empty.")

    if lo == hi:
        return nums[lo]

    mid = (hi + lo) // 2

    if (mid == 0 or nums[mid] >= nums[mid - 1]) and (mid == len(nums) - 1 or nums[mid] >= nums[mid + 1]):
        return nums[mid]
    elif mid > 0 and nums[mid] < nums[mid - 1]:
        return one_D(nums, lo, mid - 1)
    else:
        return one_D(nums, mid + 1, hi)

print(one_D([6, 2,8]))  # Should return 6


def Two_D_greedy_ascent(arr):
    rows = len(arr)
    cols = len(arr[0])

    row = rows // 2
    col = cols // 2

    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while True:
        curr_val = arr[row][col]
        peak_found = True

        for move in moves:
            new_row = row + move[0]
            new_col = col + move[1]

            if 0 <= new_row < rows and 0 <= new_col < cols:
                if arr[new_row][new_col] > curr_val:
                    row = new_row
                    col = new_col
                    peak_found = False
                    break

        if peak_found:
            return (row, col, arr[row][col])

arr = [
    [10, 8, 10, 10],
    [14, 15, 11, 11],
    [15, 11, 11, 11],
    [16, 17, 11, 20]
]

print(Two_D_greedy_ascent(arr))  # Output: (3, 3, 20)
