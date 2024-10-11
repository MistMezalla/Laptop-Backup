#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:
        int Karatsuba_multiplication(int a,int b)
        {
            if (a<10 || b<10)
                return a*b;

            string a_str = to_string(a);
            string b_str = to_string(b);

            int m = max(a_str.size(),b_str.size())/2;

            int a1 = stoi(a_str.substr(0,a_str.size() - m));
            int a0 = stoi(a_str.substr(a_str.size() - m));

            int b1 = stoi(b_str.substr(0,b_str.size() - m));
            int b0 = stoi(b_str.substr(b_str.size() - m));

            int z0 = Karatsuba_multiplication(a0,b0);
            int z1 = Karatsuba_multiplication((a0+a1),(b0+b1));
            int z2 = Karatsuba_multiplication(a1,b1);

            return z2*pow(10,2*m) + (z1-z0-z2)*pow(10,m) + z0;
            
        }

};

int main()
{
    Solution sol;
    cout << sol.Karatsuba_multiplication(1234,5678);
    return 0;
}