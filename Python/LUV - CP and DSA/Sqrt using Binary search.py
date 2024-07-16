eps = 1

def sq_root(n: int, lo = 0, hi = None):
    if n < 0:
        raise ValueError("Cannot compute square root of a negative number")
    if n == 0 or n == 1:
        return n

    if not hi:
        hi = n

    while (hi-lo)>eps:
        mid = (lo + hi) // 2
        if abs(mid*mid - n) < eps:
            return mid
        if mid*mid < n:
                lo = mid
        else:
            hi = mid

    return lo

print(sq_root(4))
print(sq_root(2))
print(sq_root(9))
print(sq_root(8))