#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:
        pair<int,int> find_max_2nd_max(const vector<int> &arr)
        {
            int n = arr.size();

            if (n<2)
                throw invalid_argument("Both max and 2nd max can't be found");
            
            vector<pair<int,vector<int>>> tournament;
            for (int i=0;i<n;i++)
                tournament.push_back({arr[i],{}});

            while (tournament.size() > 1)
            {
                vector<pair<int,vector<int>>> next_rd;

                for (int i = 0;i<tournament.size() - 1;i+=2)
                {
                    int winner;
                    vector<int> loser;
                    if(tournament[i].first > tournament[i+1].first)
                    {
                        winner = tournament[i].first;
                        loser = tournament[i].second;
                        loser.push_back(tournament[i+1].first);
                    }
                    else
                    {
                        winner = tournament[i+1].first;
                        loser = tournament[i+1].second;
                        loser.push_back(tournament[i].first);
                    }
                    next_rd.push_back({winner,loser});
                }

                if (tournament.size() & 1)
                    next_rd.push_back(tournament.back());
                
                tournament = next_rd;
            }

            return {tournament[0].first, *max_element(tournament[0].second.begin(),tournament[0].second.end())};
        }
};

int main()
{
    Solution sol;
    auto res = sol.find_max_2nd_max({7,8,6,9,10,1,11});
    cout << res.first << " & " << res.second << endl;
    return 0;
}