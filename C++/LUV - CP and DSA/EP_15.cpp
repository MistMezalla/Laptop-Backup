#include <bits/stdc++.h>
using namespace std;

const int N = 1e+7 + 10;
int arr[N];
int PF[N];

int main()
{
    int n,m;
    cin >> n >> m;
    cout << endl;

    while(m--)
    {
        int a,b,k;
        cin >> a >> b >> k;
        cout << endl;
        arr[a-1]+=k;
        arr[b+1]-=k ;       
    }

    int i;
    for (i=1;i<=n;i++)
    {
        PF[i]=PF[i-1]+arr[i];
    }

    int mx=PF[0];
    for(i=1;i<=n;i++)
    {
        if (mx<=PF[i])
            mx=PF[i];
    }

    cout << mx << endl;

    return 0;
}