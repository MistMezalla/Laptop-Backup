#include <stdio.h>

#define SIZE 10
int st[SIZE];
int Me,Mo;

void push(int st[],int *t,int val)
{
    if (*t==Me || *t==Mo)
    {
        printf("Stack Overflow\n");
        return;
    }
    *t+=2;
    st[*t]=val;
}

int pop(int st[],int *t)
{
    if(*t==-2 || *t==-1)
    {
        printf("Stack Underflow\n");
    }
    else
    {
        int pos;
    pos=*t;
    *t-=2;
    return st[pos];
    }
}

void display(int st[],int *t)
{
    int i;
    if(*t%2==0)
    {
        if(*t==-2)
    {
        printf("Stack Underflow\n");
    }
        for(i=*t;i>-2;i-=2)
        {
            printf("%d\n",st[i]);
        }
    }
    else 
    {
        if(*t==-1)
    {
        printf("Stack Underflow\n");
    }
        for (i=*t;i>-1;i-=2)
        {
            printf("%d\n",st[i]);
        }
    }
}

 void main()
{
    int me,mo;
    int t1=-2,t2=-1;
    int *te=&t1,*to=&t2;
    printf("Enter the max size of the stack: ");
    scanf(" %d %d",&me,&mo);
    Me=2*(me-1);
    Mo=2*mo-1;

    int ch;
    do
    {
        printf("Enter the choice: ");
        scanf(" %d",&ch);
        switch(ch)
        {
            case 1:
            {
                int val;
                printf("Enter the val: ");
                scanf(" %d",&val);
                push(st,te,val);
                break;
            }
            case 2:
            {
                int val;
                printf("Enter the val: ");
                scanf(" %d",&val);
                push(st,to,val);
                break;
            }
            case 3:
            {
                printf("The popped value of stack 1 is %d\n",pop(st,te));
                break;
            }
            case 4:
            {
                printf("The popped value of the stack 2 is %d\n",pop(st,to));
                break;
            }
            case 5:
            {
                display(st,te);
                break;
            }
            case 6:
            {
                display(st,to);
                break;
            }
        }
    } while (ch!=0);
    
}