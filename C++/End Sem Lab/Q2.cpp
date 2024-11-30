#include <bits/stdc++.h>
using namespace std;

class Solution {
    public :
        int min_cost_make_identical(string &s1,string &s2, vector<int> &cost1, vector<int> &cost2) {
        unordered_map<char,int> cost1_per_char,cost2_per_char;

        vector<int> freq(26,0);

        int i;
        for(i = 0;i< static_cast<int>(s1.size());i++) {
            //cout << s1[i] << "\t";
            freq[ int(s1[i]) - int('a')] ++;
            cost1_per_char[s1[i]] = cost1[i];
        }
        cout << endl;
        for(i = 0;i< static_cast<int>(s2.size());i++) {
            //cout << s2[i] << "\t";
            freq[ int(s2[i]) - int('a')] --;
            cost2_per_char[s2[i]] = cost2[i];
        }

        int min_cost = 0;
        for (int j = 0;j <26;j++) {
            char ch = char(int('a') + j);
            if (freq[j] > 0) {
                min_cost += cost1_per_char[ch];
            }
            else if(freq[j] < 0) {
                min_cost += cost2_per_char[ch];
            }
        }
        return min_cost;
    }
};

int main() {
    Solution sol;
    int t;
    cout << "Enter the number of test cases" << endl;
    cin >> t ;
    cout << endl;

    while (t--) {
        string s1,s2;
        int size1,size2;
        vector<int> cost1,cost2;

        cout << "Enter the size of first string" <<endl;
        cin >> size1;
        cout << endl;
        if (size1 > 0) {
            cout << "Enter the first String" << endl;
            cin >> s1;
            cout << endl;

            cout << "Enter the cost array for string 1" << endl;
            for (int i = 0; i < size1;i++) {
                int val;
                cin >> val;
                cost1.push_back(val);
            }
            cout << endl;
        }


        cout << "Enter the size of second string" << endl;
        cin >> size2;
        cout << endl;

        if (size2 > 0) {
            cout << "Enter the second string"<< endl;
            cin>> s2;
            cout << endl;




            cout << "Enter the cost array for string 2" << endl;
            for (int i = 0; i < size2;i++) {
                int val;
                cin >> val;
                cost2.push_back(val);
            }

        }

        auto res = sol.min_cost_make_identical(s1,s2,cost1,cost2);
        cout << res << endl;
    }
}