#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:
        long long Karatsuba(long long a,long long b)
        {
            if(a<10 || b<10)
                return a*b;

            string a_str = to_string(a);
            string b_str = to_string(b);

            int m = max(a_str.size(),b_str.size())/2;

            long long a1 = stoi(a_str.substr(0,a_str.size() - m));
            long long a0 = stoi(a_str.substr(a_str.size() - m));
            long long b1 = stoi(b_str.substr(0,b_str.size() - m));
            long long b0 = stoi(b_str.substr(b_str.size() - m));

            long long z0 = Karatsuba(a0,b0);
            long long z1 = Karatsuba((a1+a0),(b1+b0));
            long long z2 = Karatsuba(a1,b1);

            return z2 * pow(10,2*m) + (z1-z0-z2) * pow(10,m) + z0;
        }

};

int main()
{
    Solution sol;
    auto res = sol.Karatsuba(123456,561389) * 1LL;
    cout << res;
    return 0;
}