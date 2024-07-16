'''
-> Logic is partially correct as this method causes "memory limit exceeded".
-> Hence we have to compute the req res as a precomputation
'''
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        pattern = [[0]]
        i = 1

        def generate(row_ind,elem):
            if row_ind == n:
                return

            row = []
            for dig in elem:
                if dig == 0:
                    row.extend([0, 1])
                else:
                    row.extend([1, 0])
            pattern.pop()
            pattern.append(row)

            generate(row_ind+1,row)

        generate(i,pattern[0])

        print(pattern)
        return pattern[0][k-1] #to be adjusted wrt 1 index

sol = Solution()
print(sol.kthGrammar(4,5))
print(sol.kthGrammar(1,1))
print(sol.kthGrammar(2,1))
print(sol.kthGrammar(2,2))
