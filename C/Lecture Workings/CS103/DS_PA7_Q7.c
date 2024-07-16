#include <stdio.h>

void Merge(int a[],int p,int q, int r)
{
    int nl,nr;
    nl=q-p+1;
    nr=r-q;
    int L[nl],R[nr];
    int i,j;
    for (i=0;i<nl;i++)
    {
        L[i]=a[p+i];
    }
    for (j=0;j<nr;j++)
    {
        R[j]=a[q+j+1];
    }

    i=0;j=0;
    int k=p;
    while(i<nl && j<nr)
    {
        if(L[i]<=R[j])
        {
            a[k]=L[i];
            k++;
            i++;
        }
        else 
        {
            a[k]=R[j];
            k++;
            j++;
        }
    }

    while(i<nl)
    {
        a[k]=L[i];
        i++;
        k++;
    }

    while(j<nr)
    {
        a[k]=R[j];
        j++;
        k++;
    }
}

void Merge_Sort(int a[],int p,int r)
{
    if (p>=r)
        return;
    int q=(p+r)/2;
    Merge_Sort(a,p,q);
    Merge_Sort(a,q+1,r);
    Merge(a,p,q,r);
}

void main()
{
    int n;
    printf("Enter the size of the array: ");
    scanf(" %d",&n);
    int arr[n];
    int i;
    for (i=0;i<n;i++)
    {
        scanf(" %d",&arr[i]);
    }

    Merge_Sort(arr,0,n-1);
    
    for (i=0;i<n;i++)
    {
        printf("%d ",arr[i]);
    }
    printf("\n");
}