class Solution():
    def intersections(self,P,Q,left,right):
        P.sort()
        return self._intersections(P,Q,left,right)

    def _intersections(self,P,Q,left,right):
        if right - left <= 1:
            return 0

        mid = (left + right)//2

        left_intersections = self.intersections(P, Q, left, mid)
        right_intersections = self.intersections(P,Q,mid,right)

        return left_intersections + right_intersections + self.cross_intersections(P,Q,left,right,mid)

    def cross_intersections(self,P,Q,left,right,mid):
        temp = []
        i = left
        j = mid

        cnt = 0
        while i < mid and j < right:
            if Q[i] <= Q[j]:
                temp.append(Q[i])
                i+=1
            else:
                temp.append(Q[j])
                cnt += mid - i
                j+=1

        while i < mid:
            temp.append(Q[i])
            i += 1

        while j < right:
            temp.append(Q[j])
            j += 1

        Q[left:right] = temp

        return cnt

sol = Solution()
P = [(2,0),(1,0),(4,0),(3,0)]
Q = [(1,1),(4,1),(3,1),(2,1)]

print(sol.intersections(P, Q, 0, len(P)))

