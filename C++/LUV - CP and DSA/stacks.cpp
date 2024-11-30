#include <bits/stdc++.h>
using namespace std;

int main()
{
    stack<int> st;
    vector<int> v={7,5,6,8,3};
    
    int i;
    for(i=0;i<5;i++)
    {
        st.push(v[i]);
    }

    cout << st.top() << endl;
    cout << st.size() <<endl;


    return 0;
}