import bisect

l = [1,3,4,4,6,6,8,9]

lb = bisect.bisect_left(l,4)
ub = bisect.bisect_right(l, 4)

print(f"lb: {l[lb]} index: {lb}")
print(f"ub: {l[ub]} index: {ub}")
