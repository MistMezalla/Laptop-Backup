#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int pow_of_number(int x,int n) {
        int ans = 1;

        while (n) {
            if (n & 1) {
                ans *= x;
            }
            x *= x;
            n = n >> 1;
        }
        return ans;
    }

    int pow_of_number_DnC(int x,int n) {
        if (n == 1)
            return x;

        int left_part = pow_of_number_DnC(x,ceil((double)n/2));
        int right_part = pow_of_number_DnC(x,floor((double)n/2));

        return left_part * right_part;
    }
};


int main() {
    Solution sol;
    cout << sol.pow_of_number(2,4) << endl;
    cout << sol.pow_of_number_DnC(2,5) << endl;
    return 0;
}