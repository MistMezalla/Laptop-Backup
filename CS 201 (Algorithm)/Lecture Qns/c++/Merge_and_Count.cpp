#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:
        pair<vector<int>, int> MnC(vector<int> A, vector<int> B)
        {
            vector<int> res;
            int cntr = 0;
            int i = 0, j = 0;

            while (i < A.size() && j < B.size())
            {
                if (A[i] > B[j])
                {
                    cntr += A.size() - i; 
                    res.push_back(B[j]);
                    j++;
                }
                else
                {
                    res.push_back(A[i]); 
                    i++;
                }
            }

            while (i < A.size())
            {
                res.push_back(A[i]);
                i++;
            }

            while (j < B.size())
            {
                res.push_back(B[j]);
                j++;
            }

            return {res, cntr};
        }
};

int main()
{
    Solution sol;
    auto result = sol.MnC({3, 6, 9, 10}, {1, 2, 4, 7, 18});

    cout << "Inversion count: " << result.second << endl;
    cout << "Merged array: ";
    for (auto num : result.first)
        cout << num << " ";
    
    cout << endl;

    return 0;
}
