class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        intersections = []

        i = 0
        j = 0
        while i<len(firstList) and j < len(secondList):
            if firstList[i][0] <= secondList[j][0]:
                if not (firstList[i][1] < secondList[j][0]):
                    intersections.append([max(firstList[i][0],secondList[j][0]),min(firstList[i][1],secondList[j][1])])

                if firstList[i][1]<=secondList[j][1]:
                    i+=1
                else:
                    j+=1
            else:
                if not (secondList[j][1] < firstList[i][0]):
                    intersections.append([max(firstList[i][0],secondList[j][0]),min(firstList[i][1],secondList[j][1])])

                if firstList[i][1]<=secondList[j][1]:
                    i+=1
                else:
                    j+=1

        return intersections

sol = Solution()
print(sol.intervalIntersection( firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]))
print(sol.intervalIntersection( firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = []))
print(sol.intervalIntersection(firstList = [], secondList = []))
print(sol.intervalIntersection(firstList = [[0,2]], secondList = [[2,4]]))