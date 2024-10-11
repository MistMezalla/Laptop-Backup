#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:
        int multiply_number_single_digit(int num,int d)
        {
            string num_str = to_string(num);
            return stoi(multiply_strings(num_str,d));
        }

        string multiply_strings(string num_str,int d)
        {
            if (num_str.size() == 1)
                return to_string(stoi(num_str) * d);

            int m = num_str.size()/2;

            string left_part = num_str.substr(0,m);
            string right_part = num_str.substr(m);
            
            string left_product = multiply_strings(left_part,d);
            string right_product = multiply_strings(right_part,d);

            left_product.append(num_str.size() - m, '0');
            string res = add_strings(left_product, right_product);

            return res;
        }

        string add_strings(string left,string right)
        {
            int i = left.size() - 1;
            int j = right.size()- 1;
            int carry = 0;
            string res;

            while (i >= 0 || j >= 0 || carry)
            {
                int dig1 = i>=0 ? left[i] - '0' : 0;
                int dig2 = j>=0 ? right[j] - '0' : 0;

                int total = dig1 + dig2 + carry;
                int carry = total/10;
                res.push_back((total % 10) + '0');

                i--;
                j--;
            }

            reverse(res.begin(),res.end());
            return res;
        }

};

int main()
{
    Solution sol;
    int number = 1234;
    int digit = 5;
    auto result = sol.multiply_number_single_digit(number, digit);
    cout << number << " * " << digit << " = " << result << endl;
    return 0;
}