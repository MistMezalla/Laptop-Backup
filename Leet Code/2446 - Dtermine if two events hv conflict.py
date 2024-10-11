class Solution:
    def haveConflict(self, event1: list[str], event2: list[str]) -> bool:
        st1 = self.time_converter(event1[0])
        st2 = self.time_converter(event2[0])
        # if st1 == st2:
        #     return True

        end1 = self.time_converter(event1[1])
        end2 = self.time_converter(event2[1])
        # if end1 == end2:
        #     return True

        return st1 <= st2 <= end1 or st2 <= st1 <= end2
        # if st1 < st2:
        #     if end1 < st2:
        #         return False
        #     else:
        #         return True
        #
        # if st2 < st1:
        #     if end2 < st1:
        #         return False
        #     else:
        #         return True
        #

    def time_converter(self,t1):
        time1 = int(t1[:2]) * 60 + int(t1[3:])
        return time1

sol = Solution()
print(sol.haveConflict(event1 = ["02:10","02:49"], event2 = ["02:00","03:00"]))