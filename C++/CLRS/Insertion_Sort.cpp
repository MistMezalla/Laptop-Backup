#include <bits/stdc++.h>
using namespace std;

void Insertion_Sort_incr(int A[],int n)
{
    int i,j;
    for (i = 1; i < n + 1; i++)
    {
        int key = A[i];
        j = i-1;
        while (key < A[j] && j > -1)
        {
            A[j+1] = A[j];
            j--;
        }
        A[j+1]=key;
    }
}

void Insertion_Sort_decr(int A[],int n)
{
    int i,j;
    for (i=1;i<n+1;i++)
    {
        int key=A[i];
        j=i-1;
        while (key>A[j] && j >-1)
        {
            A[j+1]=A[j];
            j--;
        }
        A[j+1]=key;
    }
}

void ADD_Bin_int(int A[], int B[], int C[],int n)
{
    A[n],B[n],C[n+1];
    int i;
    int carry = 0;
    for (i=0;i<n;i++)
    {
        int res = A[i] + B[i] + carry;
        if(res >= 2)
        {
            C[i] = res%2;
            carry = res/2;
        }
        else
        {
            C[i]=res;
        }
    }
    C[n] = carry;
}

void Ins_Sort_rec(int A[],int p, int r)
{
    int key = A[r];
    int j = r-1;
    while(j>-1 && key<A[j])
    {
        A[j+1]=A[j];
        j--;
    }
    A[j+1]=key;
}

void Insertion_Sort_rec(int A[], int p, int r)
{
    if (p>=r)
        return;
    
    int q = (p+r)/2;
    Insertion_Sort_rec(A,p,r-1);
    Ins_Sort_rec(A,p,r);
}

int main()
{
    int A[] = {5, 8, 6, 4};
    int i;

    Insertion_Sort_incr(A, 4);
    for (i=0;i<4;i++)
    {
        cout << A[i] << ' ' ;
    }

    cout <<endl;
    Insertion_Sort_decr(A,4);
    for (i=0;i<4;i++)
    {
        cout << A[i] << ' ' ;
    }

    cout << endl;
    int arr[]={3,4,1,2};
    Insertion_Sort_rec(arr, 0, 3);
    for (i=0;i<4;i++)
    {
        cout << arr[i] << ' ' ;
    }

    cout << endl;
    int b1[]={1,1,1}, b2[]={1,0,1}, b3[4];
    cout << b1[0]<<','<<b2[0]<< endl;

    int n=3;
    for (i=0;i<n/2 + 1;i++)
    {
        int temp = b1[i];
        b1[i]=b1[n-i-1];
        b1[n-i-1]=temp;
    }

    for (i=0;i<n/2 +1;i++)
    {
        int temp = b2[i];
        b2[i]=b2[n-i-1];
        b2[n-i-1]=temp;
    }
    

    cout << "b1" <<endl;
    for (i=0;i<3;i++)
    {
        cout << b1[i] << ' ' ;
    }
    cout <<endl;

    cout << "b2" <<endl;
    for (i=0;i<3;i++)
    {
        cout << b2[i] << ' ' ;
    }
    cout<<endl;

    ADD_Bin_int(b1,b2,b3,3);
    for (i=3;i>-1;i--)
    {
        cout << b3[i] << ' ' ;
    }

    return 0;
}