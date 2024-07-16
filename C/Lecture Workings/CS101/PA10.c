#include <stdio.h>

//Q1
int *max_ele(int *,int *,int );
void Q1()
{
    int n;
    printf("Enter the size of the array: ");
    scanf(" %d",&n);

    int arr1[n],arr2[n];
    int i;
    for (i=0;i<n;i++)
    {
        printf("Enter the number in arr1: ");
        scanf(" %d",&arr1[i]);
        printf("Enter the number in arr2: ");
        scanf(" %d",&arr2[i]);    
    }
        int *p;
        p=(max_ele(arr1,arr2,n));
        for(i=0;i<n;i++)
            printf("%d ",*(p+i));
       
}

int *max_ele(int *a1, int *a2, int m)
{
    int i;
    static int a3[100];
    for (i=0;i<m;i++)
    {
        if (*(a1+i)>=*(a2+i))
            a3[i]=*(a1+i);
        else    
            a3[i]=*(a2+i);
    }

    return a3;
}

//Q2
int *sort_array(int *,int *,int, int );
void Q2()
{
    int n1;
    printf("Enter the size of the first array: ");
    scanf(" %d",&n1);

    int n2;
    printf("Enter the size of the second array: ");
    scanf(" %d",&n2);

    int i;
    int arr1[n1],arr2[n2];
    for (i=0;i<n1;i++)
    {
        printf("Enter the number: ");
        scanf(" %d",&arr1[i]);
    }

    for (i=0;i<n2;i++)
    {
        printf("Enter the number: ");
        scanf(" %d",&arr2[i]);
    }

    int j;
    for (i=0;i<n1;i++)
    {
        for (j=i+1;j<n1;j++)
        {
            if (arr1[i]>=arr1[j])
            {
                arr1[i]=arr1[i]+arr1[j];
                arr1[j]=arr1[i]-arr1[j];
                arr1[i]=arr1[i]-arr1[j];
            }
        }
    }

    for (i=0;i<n2;i++)
    {
        for (j=i+1;j<n2;j++)
        {
            if (arr2[i]>=arr2[j])
            {
                arr2[i]=arr2[i]+arr2[j];
                arr2[j]=arr2[i]-arr2[j];
                arr2[i]=arr2[i]-arr2[j];
            }
        }
    }


    int *p;
    p=sort_array(arr1,arr2,n1,n2);
    for (i=0;i<n1+n2;i++)
        printf("%d ",*(p+i));
}

int *sort_array(int *a1,int *a2, int m,int n)
{
    static int a3[1000];
    int i;
    for (i=0;i<m;i++)
        a3[i]=*(a1+i);
    int k=0;
    for (i=m;i<m+n;i++)
    {
        a3[i]=*(a2+k);
        k++;
    }

    int j;
    for (i=0;i<m+n;i++)
    {
        for (j=i+1;j<m+n;j++)
        {
            if (a3[i]>=a3[j])
            {
                a3[i]=a3[i]+a3[j];
                a3[j]=a3[i]-a3[j];
                a3[i]=a3[i]-a3[j];
            }
        }
    }

    return a3;

}

//Q3
void countnum(int *,int);
void Q3()
{
    int n;
    printf("Enter the size of the array: ");
    scanf(" %d",&n);

    int arr[n];
    int i;
    for (i=0;i<n;i++)
    {
        printf("Enter the number: ");
        scanf(" %d",&arr[i]);
    }   

    countnum(arr,n); 
}

int isPrime(int );
void countnum(int *a, int m)
{
    int i;
    int e=0,o=0,p=0,np=0;
    for (i=0;i<m;i++)
    {
        if (*(a+i)%2==0) //even
            e++;
        if (*(a+i)%2!=0) //odd 
            o++;
        if (isPrime(*(a+i))==1) //prime 
            p++;
        if (isPrime(*(a+i))==0) //non prime
            np++;
    }

    printf("\n%d\t%d\t%d\t%d",e,o,p,np);
}

int isPrime(int x)
{
    int i;
    int flag=1;//prime
    
    if (x==1 || x<=0)
        flag=0; //non prime
    else 
        for (i=2;i<=x/2;i++)
        {
            //printf("Hi");
            if (x%i==0)
            {
                //printf("Hello");
                flag=0; //non prime
                break;
            }    
        }
    return flag;
}

//Q4
int find(int *,int );
void Q4()
{
    int m,n;
    printf("Enter the size of 2D array: ");
    scanf(" %d %d",&m,&n);

    int arr[m][n];
    int i,j;
    for (i=0;i<m;i++)
    {
        for (j=0;j<n;j++)
        {
            printf("Enter the element: ");
            scanf(" %d",&arr[i][j]);
        }
    }

    printf("The freq is %d",find(arr,m*n));
}

int find(int *a,int size)
{
    int i;
    static int c=0;
    int num;
    printf("Enter the element to be found: ");
    scanf(" %d",&num);

    for (i=0;i<size;i++)
    {
        if (*(a+i)==num)
            c++;
    }

    return c;
}


#define s_m 2
#define s_n 3
//Q5
void matrix_add(int *,int *);
void Q5()
{
    /*
    static int m,n;
    printf("Enter the size of the matrix: ");
    scanf(" %d %d",&m,&n);
    */
    int mat1[s_m][s_n],mat2[s_m][s_n];
    int i,j;

    for (i=0;i<s_m;i++)
    {
        for (j=0;j<s_n;j++)
        {
            printf("Enter the element of matrix 1: ");
            scanf(" %d",&mat1[i][j]);
        }
    }


    for (i=0;i<s_m;i++)
    {
        for (j=0;j<s_n;j++)
        {
            printf("Enter the element of matrix 2: ");
            scanf(" %d",&mat2[i][j]);
        }
    }

    for (i=0;i<s_m;i++)
    {
        for (j=0;j<s_n;j++)
        {
            //printf("Enter the element of matrix 1: ");
            printf("%d,%d",mat1[i][j],mat2[i][j]);
        }
    }
    printf("\n");
    matrix_add(mat1,mat2);
}

void matrix_add(int *a1,int *a2)
{
    int i,j;
    int c=0;
    int arr[s_m][s_n];
    for (i=0;i<s_m;i++)
    {
        for (j=0;j<s_n;j++)
        {
            printf("%d,%d\n",*(a1+c),*(a2+c));
            arr[i][j]=*(a1+c)+*(a2+c);
            
            c++;
        }
    }

    for (i=0;i<s_m;i++)
    {
        for(j=0;j<s_n;j++)
            printf("%d ",arr[i][j]);
        printf("\n");
    }
}
void main()
{
    Q5();
    //printf("%d",isPrime(-20));
}