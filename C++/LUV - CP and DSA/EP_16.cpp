#include <bits/stdc++.h>
using namespace std;

const int n = 1e5 +7;
int arr[26][n];

int main()
{
    int t;
    cin >> t;
    cout << endl;
    while(t--)
    {
        int N,Q;
        string str;
        cin >> N >> Q;
        cout << endl;
        cin >> str;
        cout << endl;

        int i,j;
        for (i=0;i<26;i++)
        {
            for (j=0;j<=N;j++)
                arr[i][j]=0;
        }

        i=j=0;
        for (j=1;j<=N;j++)
        {
            arr[str[j-1]-'a'][j]++;
        }

        for (i=0;i<26;i++)
        {
            for(j=1;j<=N;j++)
                arr[i][j]+=arr[i][j-1];
        }

        while(Q--)
        {
            int l,r;
            cin >> l >> r;
            cout << endl;
            int oddcnt=0;
            int i;
            for(i=0;i<26;i++)
            {
                if(oddcnt>1)
                {
                    cout << "False" << endl;
                    break;
                }
                if ((arr[i][r]-arr[i][l-1])%2!=0)
                    oddcnt++;
            }
            cout << "True" <<endl;
        }
    }
    return 0;
}