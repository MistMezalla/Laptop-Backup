#include <stdio.h>
//Q2 
void Q2() 
{
    int arr[10]={15,20,67,34,07,55,98,12,05,41};

    int i,min=arr[0],pos;
    for (i=1;i<10;i++)
    {
        if (min>=arr[i])
        {
            min=arr[i];
            pos=i;
        }
    }

    arr[pos]=arr[pos]+arr[0];
    arr[0]=arr[pos]-arr[0];
    arr[pos]=arr[pos]-arr[0];

    int j,p;
    for (i=1;i<10;i++)
    {
        for (j=i-1;j>-1;j--)
        {
            if (arr[i]>=arr[j])
            {
                p=j+1;
                break;
            }
        }
            int k,temp;
            temp=arr[i];
            for (k=i;k>=p+1;k--)
                arr[k]=arr[k-1];
            arr[p]=temp;
    }

    for(i=0;i<10;i++)
        printf("%d ",arr[i]);
}

//Q3
int smallest(int a[], int m, int n);
void Q3()
{
    int arr[10] = {15, 20, 67, 34, 7, 55, 98, 12, 5, 41};

    int i;
    for (i = 0; i < 10; i++)
    {
        int pos = smallest(arr, i, 10);
      //  printf("%d,%d\n",arr[i],arr[pos]);
        if(arr[i]!=arr[pos])
        {
            arr[i] = arr[pos] + arr[i];
            arr[pos] = arr[i] - arr[pos];
            arr[i] = arr[i] - arr[pos];
        }
    }

    for (i = 0; i < 10; i++)
        printf("%d ", arr[i]);
}

int smallest(int a[], int m, int n)
{
    int i, min = a[m];
    int pos = m;
    for (i = m + 1; i < n; i++)
    {
        if (a[i] <= min)
        {
            min = a[i];
            pos = i;
        }
    }

    //printf("%d\t",pos);
    return pos;
}

int main()
{
    Q2();
    return 0;
}