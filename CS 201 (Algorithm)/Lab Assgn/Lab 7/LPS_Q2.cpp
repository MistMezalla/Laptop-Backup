/*
     Rec Rel:-
     OPT_sol = max{dp(i+1,j-1) + 2 , dp(i,j-1), dp(i+1,j)}
*/

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
     int Longest_Palindromic_Subseq(vector<int> &nums) {
          int n = static_cast<int>(nums.size());
          if (n == 0) return 0;


          vector<vector<int>> dp(n, vector<int>(n, 0));


          for (int i = 0; i < n; ++i) {
               dp[i][i] = 1;
          }


          for (int len = 2; len <= n; ++len) {
               for (int i = 0; i <= n - len; ++i) {
                    int j = i + len - 1;

                    if (nums[i] == nums[j]) {
                         dp[i][j] = dp[i+1][j-1] + 2;
                    } else {
                         dp[i][j] = max(dp[i+1][j], dp[i][j-1]);
                    }
               }
          }

          return dp[0][n-1];
     }
};

int main() {
     Solution sol;
     vector<int> nums = {1,2,3,3,5,1};
     cout << "len of LPS: "
          << sol.Longest_Palindromic_Subseq(nums) << endl;
     return 0;
}
