#include <bits/stdc++.h>
using namespace std;

void bubble_sort(int a[],int n)
{
    int i,j;
    int swp = 1;
    for (i=0;i<n-1 && swp;i++)
    {
        for (j=n;j>i;j--)
        {
            if (a[j]<a[j-1])
                swap(a[j],a[j-1]);
        }
    }
}

int main()
{
    int arr[]={7,2,9,3,5};
    bubble_sort(arr,5);

    int i;
    for (i=0;i<5;i++)
    {
        cout << arr[i] << ' ';
    }
}