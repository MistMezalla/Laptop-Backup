#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:
        int add_large_numbers(int num1,int num2)
        {
            string num1_str = to_string(num1);
            string num2_str = to_string(num2);
            return stoi(add_strings(num1_str,num2_str));
        }

        string add_strings(string n1,string n2)
        {
            if (n1.size() == 1 && n2.size() == 1)
                return to_string(stoi(n1) + stoi(n2));

            if (n1.size() < n2.size())
                n1.insert(0,n2.size() - n1.size(),'0');
            else if (n1.size() > n2.size())
                n2.insert(0,n1.size() - n2.size(),'0');

            int m = n2.size()/2;

            string n1_left = n1.substr(0,m);
            string n1_right = n1.substr(m);
            string n2_left = n2.substr(0,m);
            string n2_right = n2.substr(m);

            string left_sum = add_strings(n1_left,n2_left);
            string right_sum = add_strings(n1_right,n2_right);

            if (right_sum.size() > n1_right.size())
            {
                    string carry =  "1";
                    string right_sum = right_sum.substr(1);
                    left_sum = add_strings(left_sum,carry); 
            }

            return left_sum + right_sum; //string concatenate and not int addition here
        }
};

int main()
{
    Solution sol;
    string number1 = "12345678901234567890";
    string number2 = "98765432109876543210";
    string result = sol.add_strings(number1, number2);
    cout << number1 << " + " << number2 << " = " << result << endl;
    return 0;
}