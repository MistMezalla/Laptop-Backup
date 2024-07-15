#include <bits/stdc++.h>
using namespace std;

const int N = 1e5+10;
int n,cows;
int pos[N];

bool can_place(int min_dist)
{
    int last_pos = -1;
    int cows_ct = cows;
    int i;
    for (i=0;i<n;i++)
    {
        if (pos[i] - last_pos >= min_dist || last_pos == -1)
        {
            last_pos = pos[i];
            cows_ct--;
        }
    }
    return cows_ct == 0;
}


int main()
{
    cin >> n >> cows;
    cout << endl;


    int i;
    for (i=0;i<n;i++)
    {
        cin >> pos[i];
    }
    cout << endl;

    sort(pos,pos+n);
    int lo=0, hi = 1e9 ,mid;

    while(hi-lo>1)
    {
        mid = (hi+lo)/2;

        if (can_place(mid))
            lo = mid;
        else
            hi = mid - 1;
    }

    if (can_place(hi))
        cout<< hi;
    else
        cout << lo;


    return 0;
}