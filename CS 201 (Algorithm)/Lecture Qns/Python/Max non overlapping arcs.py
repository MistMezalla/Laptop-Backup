class Solution:
    def max_non_overlapping_arcs(self, arcs):
        arcs.sort(key=lambda x: x[1])
        selected_arcs = []
        last_end = -float('inf')

        for arc in arcs:
            if arc[0] >= last_end:
                selected_arcs.append(arc)
                last_end = arc[1]

        return selected_arcs


arcs = [(30, 60), (45, 90), (90, 180), (170, 270), (200, 240)]
sol = Solution()
print(sol.max_non_overlapping_arcs(arcs))
