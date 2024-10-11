#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:
        int max_profit(vector<int> prices,int rent)
        {
            if (!prices.size() or prices.size() < 2)
            {
                return 0;
            }
            int min_price = prices[0];
            int min_price_day = 0;
            int max_profit = 0;

            int i;
            for (i=0;i<prices.size();i++)
            {
                int curr_profit = prices[i] - min_price - rent*(i-min_price_day);
                if (curr_profit > max_profit)
                    max_profit = curr_profit;
                else if (prices[i] - rent < min_price)
                {
                    min_price = prices[i];
                    min_price_day = i;
                }
            }
            return max_profit;
        }

};

int main()
{
    Solution sol;
    vector<int> prices = {70, 100, 140, 40, 60, 90, 120, 30, 60};
    cout << sol.max_profit({100, 90, 80, 70, 60},5) << endl;
    return 0;
}