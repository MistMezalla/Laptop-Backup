class Solution():
    def root_QE(self, coeff: list[int], n: int):
        a, b, c = coeff[0], coeff[1], coeff[2]

        D = b**2 - 4*a*c
        x_min = -b / (2*a)

        if D < 0:  # No real roots if discriminant is negative
            return None

        lo = int(-b / (2*a))
        hi = n

        while hi - lo > 1:
            mid = (hi + lo) // 2

            eqn = a * mid**2 + b * mid + c

            if eqn >= 0:
                hi = mid
            else:
                lo = mid

        if a * lo**2 + b * lo + c == 0:
            return lo
        elif a * hi**2 + b * hi + c == 0:
            return hi
        else:
            return None

sol = Solution()
print(sol.root_QE([6, -13, 6], 8))  # This should output None as there is no integer root ≤ 8
