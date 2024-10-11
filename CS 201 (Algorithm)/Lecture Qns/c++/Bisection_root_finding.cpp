#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:
        pair<int, bool> find_root(vector<int> coeff, int n)
        {
            int a = coeff[0], b = coeff[1], c = coeff[2];
            int D = b * b - 4 * a * c;
            int lo = -b / (2 * a);

            if (D < 0)
                return {-1, false};

            int hi = n;
            int mid;

            while (hi - lo > 1)
            {
                mid = (hi + lo) / 2;

                int eqn = a * mid * mid + b * mid + c;

                if (eqn >= 0)
                    hi = mid;
                else
                    lo = mid;
            }

            if (a * lo * lo + b * lo + c == 0)
                return {lo, true};
            else if (a * hi * hi + b * hi + c == 0)
                return {hi, true};
            else
                return {-1, false};
        }
};

int main()
{
    Solution sol;
    auto result = Solution::find_root({6, -13, 6}, 8);

    if (result.second)
        cout << "Root: " << result.first << endl;
    else
        cout << "No integer root found within the given range." << endl;

    return 0;
}
