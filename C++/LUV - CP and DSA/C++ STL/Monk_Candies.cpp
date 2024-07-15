#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    cout << endl;
    while (t--)
    {
        int n,k;
        cin >> n >> k;
        cout << endl;
        multiset<int> bags;
        int i;
        for (i=0;i<n;i++)
        {
            int candy;
            cin >> candy;
            cout << endl;
            bags.insert(candy);
        }


        int candy_cnt = 0;
        while (k--)
        {
            multiset<int> :: iterator it;
            it = --bags.end();
            int temp = *it;
            candy_cnt += *it;
            bags.erase(it);
            bags.insert(temp/2);
        }
            
        cout << candy_cnt << endl;
    }
    
   

    return 0;
}