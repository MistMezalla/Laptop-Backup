#include <bits/stdc++.h>
using namespace std;

void Sel_Sort(int A[],int n)
{
    int i,j;
    for (i=0;i<n-1;i++)
    {
        int min_pos=i;
        for (j=i+1;j<n;j++)
        {
            if(A[min_pos]>=A[j])
            {
                min_pos=j;
            }
        }
        int temp=A[i];
        A[i]=A[min_pos];
        A[min_pos]=temp;
    }
}

int main()
{
    int A[] = {5, 8, 6, 4};
    int i;

    Sel_Sort(A, 4);
    for (i=0;i<4;i++)
    {
        cout << A[i] << ' ' ;
    }

    return 0;
}