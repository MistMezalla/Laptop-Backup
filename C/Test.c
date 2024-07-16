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


int t1;
void test6()
{
    t1=10;
    printf("1st%d ",t1);
}

void test7()
{
    int i;
    for (i=0;i<10;i++)
    {
        ++i;
        printf("%d ",i);
    }
}

void test8()
{
    int num;

    printf("Enter integers (enter -1 to exit):\n");

    do {
        scanf("%d", &num);
        if (num != -1) {
            // Process the entered integer here if needed
            printf("You entered: %d\n", num);
        }
    } while (num != -1);

    printf("Exiting program.\n");
}

#include <string.h>
void test9(char msg[20])
{
    //char msg[20];
    //scanf(" %[^\n]s",msg);
    printf("OG msg: %s\n",msg);
    
    char ins[10]="to ";
    //scanf(" %[^\n]s",ins);
    printf("Ins: %s\n",ins);

    int l_msg=strlen(msg);
    int l_ins=strlen(ins);
    int i;
    int pos=3;
    char temp=msg[pos];

    for (i=l_msg;i>=pos;i--)
    {
        msg[i+3]=msg[i];
    } 
    printf("Shifted msg: %s\n",msg);

    for(i=0;i<l_ins;i++)
    {
        msg[pos]=ins[i];
        pos++;
    }
    printf("New msg: %s\n",msg);
}

void test10()
{
    int a[3][3][3] = {
        {1, 2, 3, 4, 5, 6, 7, 8, 9},
        {10, 11, 12, 13, 14, 15, 16, 17, 18},
        {19, 20, 21, 22, 23, 24, 25, 26, 27}
    };
    int i = 0, j = 0, k = 0;
    for (i = 0; i < 3; i++) {
        for (k = 0; k < 3; k++)
            printf("%d ", a[i][j][k]);
        printf("\n");
    }

     int b[3][3]= {
        {1, 2, 3},{ 4, 5, 6},{ 7, 8, 9}};

    i=j=0;
    for (j=0;j<3;j++)
        printf("%d ",b[i][j]);
    printf("\n%d",b[1][0]);
}


void main()
{
/* 
    int i;
    //test4();
    int st[size]={1,2,3,4,5,6,7,8,9};
    int top=-1;
    top=8;
    int *Top=&top;

    printf("%d",9%-4);
    //test_5_1(st,Top);
    //test_5_2(st,Top);
    //test_5_1(st,Top);
*/
    /*
    for(i=0;i<8;i++)
        printf("%d ",(int) pow(10,i));
    */

   //test6();
   //printf("%d ",t1);
    /*
    int t=NULL;
    printf("%d\n",t);

    printf("\n%10.2e\n%11.4e",98.7654732,98.7654732);
    */
/*
   char str[20]="GM all";
 test9(str);  
 printf("%s\n",str);
 */
    int i;
    for(i=0;i<10;i++)
    {
        ++i;
        printf("%d ",i);
        i++;
    }
    test10();
}

