#include <bits/stdc++.h>
using namespace std;

void Merge(int A[], int p, int q, int r)
{
    int n_l=q-p+1;
    int n_r=r-q;

    int L[n_l],R[n_r];

    int i,j;
    for (i=0;i<n_l;i++)
        L[i]=A[p+i];
    for(j=0;j<n_r;j++)
        R[j]=A[q+1+j];

    i=j=0;
    int k=p;

    while(i<n_l && j<n_r)
    {
        if(L[i]<=R[j])
        {
            A[k]=L[i];
            i++;
            k++;
        }
        else
        {
            A[k]=R[j];
            j++;
            k++;
        }
    }

    while (i<n_l)
    {
        A[k]=L[i];
        k++;
        i++;
    }

    while (j<n_r)
    {
        A[k]=R[j];
        k++;
        j++;
    }
}

void Merge_sort(int A[],int p, int r)
{
    if (p>=r)
        return; 
    
    int q=(p+r)/2;
    Merge_sort(A,p,q);
    Merge_sort(A,q+1,r);
    Merge(A,p,q,r);
}

int main()
{
    int arr[]={3,1,2,4};
    Merge_sort(arr,0,3);

    int i;
    for (i=0;i<4;i++)
        cout << arr[i] << ' ';

    return 0;
}