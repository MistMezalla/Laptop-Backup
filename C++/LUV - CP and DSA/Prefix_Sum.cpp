#include <bits/stdc++.h>
using namespace std;

const int N = 1e5 + 7;
int arr[N];
long long int pf[N];

const int M = 1e3 + 7;
int Arr[M][M];
long long int Pre_fix[M][M];

void One_D_arr()
{
    int i,n;
    cin >> n;
    cout << endl;
    for (i=1;i<=n;i++)
    {
        cin >> arr[i];
        pf[i]=pf[i-1]+arr[i];
    }   
    cout << endl;
    int t;
    cin >> t;
    while (t--)
    {
        int l,r;
        cin >> l >> r;
        cout << pf[r] - pf[l-1];
    }
}

void Two_D_arr()
{
    int i,j;
    int n;
    cin >> n;
    cout << endl;
    for (i=1;i<=n;i++)
    {
        for (j=1;j<=n;j++)
        {
            cin >> Arr[i][j];
            Pre_fix[i][j] = Arr[i][j] + Pre_fix[i-1][j] + Pre_fix[i][j-1] - Pre_fix[i-1][j-1];
        }
    }
    cout << endl;

    int t;
    cin >> t;
    cout << endl;
    while(t--)
    {
        int a,b,c,d;
        cin >> a >> b >> c >> d;
        cout << endl;

        for (i=1;i<=n;i++)
    {
        for (j=1;j<=n;j++)
        {
            cout << Arr[i][j] << ' ';
        }
        cout << endl;
    }
        cout << endl;
        cout << Pre_fix[c][d] - Pre_fix[a-1][d] - Pre_fix[c][b-1] + Pre_fix[a-1][b-1] << endl;
    }
}

int main()
{
    //One_D_arr();
    Two_D_arr();
    return 0;
}