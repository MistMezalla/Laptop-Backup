#include <stdio.h>
#include <stdlib.h>

void display(int arr[],int n)
{
    int i;
    for(i=0;i<n;i++)
    {
        printf("%d ",arr[i]);
    }

}
int sum(int arr[],int n)
{

    int i;
    int sum=0;
    for(i=0;i<n;i++)
    {
        sum=sum+arr[i];


    }
    //printf("%d \n",sum);
    return sum;
}
void avg(int arr[],int n)
{
    float av;
    av=sum(arr,n)/n;
    printf("%f\n",av);

}
void address(int arr[],int n)
{
    int i;
    for(i=0;i<n;i++)
    {

        printf("%d ",&arr[i]);
    }
}
int search_element(int arr[],int n)
{
    int flag;
    printf("Enter the element to search ");
    scanf(" %d",&flag);
    for(int i=0;i<n;i++)
    {
        if(arr[i]==flag)
            return i+1;
    }
    return -1;
}

int *findMinMax(int a[],int n)
{
    int i;
    int pos_min=0,pos_max=n-1;
    int min=a[0];
    int max=a[n-1];
   
    for(i=1;i<n;i++)
    {
        if(min>=a[i])
        {    
            min=a[i];
            pos_min=i;
        }
    }
    for(i=n-1;i>=0;i--)
    {
        if(max<=a[i])
        {    
            max=a[i];
            pos_max=i;
        }
    }
   
   /* for (i=0;i<n;i++)
    {
        for (j=i+1;j<n;j++)
        {
            if(a[i]>=a[j])
            {
                a[i]=a[i]+a[j];
                a[j]=a[i]-a[j];
                a[i]=a[i]+a[j];
            }*/
   int *brr=(int*)calloc(2,sizeof(int));
    brr[0]=pos_min;
    brr[1]=pos_max;
   
    return brr;
}
int * swapMinMax(int arr[],int n)
{
    int *ind=findMinMax(arr,n);
    printf("The Maximum element is %d\n",arr[ind[0]-1]);
    printf("The Minimum element is %d\n",arr[ind[1]-1]);
}

void Q1()
{
    int n;
    printf("enter array size: ");
    scanf(" %d",&n);
    int *arr=(int*)calloc(n,sizeof(int));
     int i;

    printf("enter array element: ");

    for(i=0;i<n;i++)
    {
        scanf(" %d",&arr[i]);

    }
     display( arr,n);
     printf("%d\n",sum(arr,n));
     avg(arr,n);
     address(arr,n);
     int *ptr=findMinMax(arr,n);
     for(i=0;i<2;i++)
     {
         printf("%d ",*(ptr+i));
     }
     printf("\n");
     swapMinMax(arr,findMinMax(arr,n));

    int val=search_element(arr,n);
    printf("The element is present at %d\n",val);
    
     for(i=0;i<n;i++){
         printf("%d  ",*(swapMinMax(arr,findMinMax(arr,n))+i));
     }
     
}

int **allocate_UT(int m)
{
    int i;
    int**p=(int **)calloc(m,sizeof(int *));

    for (i=0;i<m;i++)
        p[i]=(int *)calloc(i+1,sizeof(int ));

    return p;
}

int **allocate(int m,int n)
{
    int i;
    int**p=(int **)calloc(m,sizeof(int *));

    for (i=0;i<n;i++)
        p[i]=(int *)calloc(n,sizeof(int ));

    return p;
}

void free_mem(int **arr, int m)
{
    int i;
    for (i = 0; i < m; i++)
        free(arr[i]);

    free(arr);
}

void Q2()
{
    int m;
    printf("Enter the size of the array: ");
    scanf(" %d %d",&m);

    int **mat=allocate_UT(m);
    int i,j;
    printf("Enter the values in the matrix: ");
    for (i=0;i<m;i++)
        for (j=0;j<i+1;j++)
            scanf(" %d",&mat[i][j]);

    for (i=0;i<m;i++)
    {
        for (j=0;j<i+1;j++)
            printf(" %d",mat[i][j]);
        printf("\n");
    }

    free_mem(mat,m);
    if (mat==NULL)
        printf("Mem freed");
    else
        printf("not Freed");

}

int **mat_mul(int **A,int **B,int m,int p)
{
    int i,j,k;
    int **res=allocate(m,p);
    for (i=0;i<m;i++)
    {
        for (j=0;j<p;j++)
        {
            for (k=0;k<p;k++)
                res[i][j]+=A[i][k]*B[k][j];
        }
    }

    return res;
}
void Q3()
{
    int m,n,p;
    printf("Enter the values of m,n,p: ");
    scanf(" %d %d %d",&m,&n,&p);

    int **mat1=allocate(m,n);
    int **mat2=allocate(n,p);

    int i,j;
    printf("Enter the values in the matrix1: ");
    for (i=0;i<m;i++)
        for (j=0;j<n;j++)
            scanf(" %d",&mat1[i][j]);

    for (i=0;i<m;i++)
    {
        for (j=0;j<n;j++)
            printf(" %d",mat1[i][j]);
        printf("\n");
    }

    printf("Enter the values in the matrix2: ");
    for (i=0;i<n;i++)
        for (j=0;j<p;j++)
            scanf(" %d",&mat2[i][j]);

    for (i=0;i<n;i++)
    {
        for (j=0;j<p;j++)
            printf(" %d",mat2[i][j]);
        printf("\n");
    }

    int **res=mat_mul(mat1,mat2,m,p);
    for (i=0;i<m;i++)
    {
        for (j=0;j<p;j++)
            printf("%d ",res[i][j]);
        printf("\n");
    }

    free_mem(mat1,m);
    if (mat1==NULL)
        printf("Mem freed");
    else
        printf("not Freed");

    free_mem(mat2,n);
    if (mat2==NULL)
        printf("Mem freed");
    else
        printf("not Freed");

    free_mem(res,m);
    if (mat1==NULL)
        printf("Mem freed");
    else
        printf("not Freed");
}


void main()
{
    Q2();
}