#include <stdio.h>
#include <math.h>

void test1()
{
    int num=50;
    int r;
    int bin=0;
    int i;
    for (i=0;i<8;i++)
    {
        r=num%2;
        num/=2;
        printf("%d %d\n",r,num);
        bin+=r*pow(10,i);
        printf("\n%d\n",bin);
        //printf("%d\n",10000+10);
    }
}

void test2()
{
    int num;
    scanf(" %d",&num);

    int i,j;
    int q=num;
    int bin=0;
    int d;
    //int b=1;
    
    for (i=0;i<8;i++)
    {
        d=q%2;
        printf("%d\t",d);
        q/=2;
        printf("%d",(int)pow(10,j));
        bin+=d*((int)pow(10,j));
        printf("\t\t%d",bin);
        //b*=10;
        printf("\n");
        j++;
    }
    printf("%d\n",bin);
}

void test3()
{
    int num;
    scanf(" %d",&num);

    int i=0;
    int q=num;
    int bin=0;
    int d;
    int b=1;
    while(q!=0)
    {
        d=q%2;
        printf("%d\n",d);
        q/=2;
        
        bin+=d*b;
        printf("%d\n",bin);
        b*=10;
    }
    printf("%d\n",bin);
}

float avg(int array[],int size);
void test4()
{
    int n;
    printf("Enter the value of n: ");
    scanf(" %d",&n);

    int arr[n];
    int i;
    for(i=0;i<n;i++)
    {
        printf("Enter the number: ");
        scanf(" %d",&arr[i]);
    }

    printf("%f",avg(arr,n));
}

float avg(int array[],int size)
{
    int *p;
    p=array;

    int i,sum=0;
    for (i=0;i<size;i++)
        sum+=*(p+i);

    return ((float)sum/size);
}
/*
void test5()
{
    void Bsort_list(Node **head)
{
    Node *ptr;//*preptr;
    ptr=*head;
    //ptr=(*head)->next;
    int min=(*head)->data;

    while(ptr->next!=NULL)
    {
        while(ptr->next->next!=NULL)
        {
            if(ptr->next->data<=ptr->data)
            {
                int temp;
                temp=ptr->next->data;
                ptr->next->data=ptr->data;=
                ptr->data=temp;
            }
            ptr->next=ptr->next->next;
        }
        ptr=ptr->next;
    }
}

}
*/
#define size 10
void test_5_1(int st[size],int *Top)
{
    int i;
    for (i=*Top;i>=0;i--)
        printf("%d\n",st[i]);
}

void test_5_2(int st[size],int *Top)
{
    (*Top)++;
    st[*Top]=10;
    test_5_1(st,Top);
}

void main()
{
    int i;
    //test4();
    int st[size]={1,2,3,4,5,6,7,8,9};
    int top=-1;
    top=8;
    int *Top=&top;

    test_5_1(st,Top);
    test_5_2(st,Top);
    test_5_1(st,Top);
    /*
    for(i=0;i<8;i++)
        printf("%d ",(int) pow(10,i));
    */
}

