#include <bits/stdc++.h>
using namespace std;

const int N = 1e5+10;
int gc_for[N];
int gc_back[N];

int main()
{
    int n,t;
    cin >> n >> t;
    cout << endl;
    int arr[n];
    int i;
    for (i=0;i<n;i++)
    {
        cin >> arr[i];
    }
    cout << endl;
    for (i=1;i<N;i++)
    {
        gc_for[i]=__gcd(arr[i-1],gc_for[i-1]);
    }

    for (i=n-1;i>0;i--)
    {
        gc_back[i]=__gcd(arr[i],gc_back[i+1]);
    }

    while(t--)
    {
        int l,r;
        cin >> l >> r;
        cout << endl;
        cout << __gcd(gc_for[l-1],gc_back[r+1]);
    }
    return 0;
}