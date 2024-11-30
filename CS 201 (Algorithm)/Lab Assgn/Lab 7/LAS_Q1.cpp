#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int Longest_alternating_subseq(vector<int>& nums) {
        int n = static_cast<int>(nums.size());
        if (n == 0) return 0;


        vector<int> up(n, 1), down(n, 1);


        for (int i = 1; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                if (nums[i] > nums[j]) {
                    up[i] = max(up[i], down[j] + 1);
                } else if (nums[i] < nums[j]) {
                    down[i] = max(down[i], up[j] + 1);
                }
            }
        }


        int las_length = max(*max_element(up.begin(), up.end()),
                             *max_element(down.begin(), down.end()));

        return las_length;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1,5,6,0,8,7};
    cout << "Length of LAS: "
         << sol.Longest_alternating_subseq(nums) << endl;

    return 0;
}
