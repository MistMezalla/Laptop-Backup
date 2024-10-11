#include <bits/stdc++.h>
using namespace std;

int MSA(vector <int> &arr)
{
    int ms,msa = arr[0];

    int i;
    for (i=1;i<arr.size();i++)
    {   
        ms = max_element(ms,ms + arr[i]);
        msa = max_element(msa,ms);
    }
    return msa;
}

int main()
{
    vector<int> nums = {-2, 1,-3, 4,-1, 2, 1,-5, 4};
    cout << MSA(nums) << endl;
    return 0;
}