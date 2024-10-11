'''
-> Question condition:-
    -> Find max and 2nd max in O(n-1 + logn)
-> Intuition:-
    -> Find max and track the 2nd max from the branch of the bin tree of max elem in the 'tournament method'
'''

class Solution():
    def find_max_2nd_max(self,arr: list[int]):
        n = len(arr)

        if n < 2:
            raise Exception ("Both max and 2nd max can't be found")

        tournament = [(arr[i],[]) for i in range(n)]

        while len(tournament) > 1:
            next_rd = []
            for i in range(0,len(tournament)-1,2):
                if tournament[i][0] > tournament[i+1][0]:
                    winner = tournament[i][0]
                    # loser = tournament[i][1].extend([tournament[i+1][0]])
                    loser = tournament[i][1]
                    loser.append(tournament[i + 1][0])
                else:
                    winner = tournament[i+1][0]
                    # loser = tournament[i+1][1].extend([tournament[i][0]])
                    loser = tournament[i + 1][1]
                    loser.append(tournament[i][0])
                next_rd.append((winner,loser))

            if len(tournament) & 1:
                next_rd.append(tournament[-1])

            tournament = next_rd

        return tournament[0][0], max(tournament[0][1])

sol = Solution()
print(sol.find_max_2nd_max([10,7,8,9,13,4,11]))


