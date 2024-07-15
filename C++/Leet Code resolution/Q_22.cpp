#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isValid(string s) 
    {
        unordered_map<char, int> hash = {{'(', 1}, {'{', 2}, {'[', 3}, {')', -1}, {'}', -2}, {']', -3}};   
        stack<int> st;
        int i;
        
        //for (char c : s)
        for (i=0;i<s.size();i++)
        {
            char c = s[i];
            if (hash[c] > 0)
                st.push(hash[c]);
            else {
                if (st.empty() || st.top() + hash[c] != 0)
                    return false;
                st.pop();
            }
        }
        return st.empty();
    }
};

int main()
{
   Solution sol;
   cout << sol.isValid("[)]");
   return 0;
}
