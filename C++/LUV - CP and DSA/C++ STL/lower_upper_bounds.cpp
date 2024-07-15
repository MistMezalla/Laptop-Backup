# include <bits/stdc++.h>
using namespace std;

int main()
{
    vector<int> v = {1,2,4,4,6,7,8,9};

    auto lower = lower_bound(v.begin(),v.end(),4);
    auto upper = upper_bound(v.begin(),v.end(),4);
    cout << "lb: " << *lower << " index: "<<lower - v.begin() << endl;
    cout << "ub: " << *upper << " index: "<< upper - v.begin() << endl;

    return 0;
}