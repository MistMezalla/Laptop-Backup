#include <bits/stdc++.h>
using namespace std;

int binary_search(int a[], int n, int x)
{
    int b = 0;
    int e = n-1;
    int m;

    while (b<=e)
    {
        m =(b+e)/2;
        
        if (a[m]==x)
            return x;
        else
        {
            if(a[m] < x)
                b=m+1;
            else
                e=m-1;
        }
    }
    return -1;
}

int main()
{
    int arr[]={1,2,3,4,5,6,7,8,9};
 
    cout << binary_search(arr,9,10);
    return 0;
}