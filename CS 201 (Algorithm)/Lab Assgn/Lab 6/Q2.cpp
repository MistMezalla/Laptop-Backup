#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:
        double fractional_knapsack(vector<pair<int,int>> items, int capacity)
        {
            sort(items.begin(),items.end(),[](pair<int,int> &a, pair<int,int> &b)
            {
                return static_cast<double>(a.first)/a.second > static_cast<double>(b.first)/b.second; 
            });

            double total_profit = 0;

            for(auto item: items)
            {
                if (capacity >= item.second)
                {
                    total_profit += item.first;
                    capacity -= item.second;
                }
                else
                {
                    double partial_part = item.first * ((double)(capacity)/item.second);
                    total_profit += partial_part;
                    break;
                }
            }
            return total_profit;
        }
};

int main()
{
    Solution sol;
    cout << fixed << setprecision(3);  // Set precision to 3 decimal places
    // As the cout by def prints the res as int or precision(0) for double values

    vector<pair<int,int>> items1 = {{60, 10}, {100, 20}, {120, 30}};
    cout << sol.fractional_knapsack(items1,50) << endl;

    vector<pair<int,int>> items2 = {{50, 5}, {80, 10}, {90, 15}};
    cout << sol.fractional_knapsack(items2,30) << endl;

    vector<pair<int,int>> items3 = {{50, 5}, {80, 10}, {90, 15}};
    cout << sol.fractional_knapsack(items3,0) << endl;

    vector<pair<int,int>> items4 = {{70, 10}};
    cout << sol.fractional_knapsack(items4 , 10) << endl;

    vector<pair<int,int>> items5 = {{100, 50}};
    cout << sol.fractional_knapsack(items5,10) << endl;

    vector<pair<int,int>> items6 = {};
    cout << sol.fractional_knapsack(items6,50) << endl;

    vector<pair<int,int>> items7 = {{100, 50}, {200, 60}};
    cout << sol.fractional_knapsack(items7,30) << endl;

    vector<pair<int,int>> items8 = {{5000, 50}, {10000, 70}, {20000, 70}};
    cout << sol.fractional_knapsack(items8,100) << endl;
    return 0;
};