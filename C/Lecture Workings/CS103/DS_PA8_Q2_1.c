#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

int st[10];
int Me,Mo;

void push(int st[],int *top,int val)
{
    if(*top==Me || *top==Mo)
    {
        printf("Stack Overflow\n");
        return;
    }
    *top+=2;
    st[*top]=val;
}

int pop(int st[],int *top)
{
    if(*top==-2 || *top==-1)
    {
        printf("Stack Underflow\n");
    }
    else
    {
        int data=st[*top];
    *top-=2;
    return data;
    }
}

void display(int st[],int *top)
{
    int i;
    if(*top%2==0)
    {
        for (i=*top;i>-2;i-=2)
        {
            printf("%d ",st[i]);
        }
        printf("\n");
    }
    else
    {
        for(i=*top;i>-1;i-=2)
        {
            printf("%d ",st[i]);
        }
        printf("\n");
    }
}

void main()
{
    int me,mo;
    printf("Enter the max size of the stacks: ");
    scanf(" %d %d",&me,&mo);

    Me=2*(me-1);
    Mo=2*mo-1;

    int t1=-2,t2=-1;
    int *te=&t1,*to=&t2;
    int ch;
    do
    {
        printf("Enter the choice: ");
        scanf(" %d",&ch);
        switch (ch)
        {
            case 1:
            {
                int val;
                printf("Enter the data to be pushed into stack 1: ");
                scanf(" %d",&val);
                push(st,te,val);
                break;
            }
            case 2:
            {
                int val;
                printf("Enter the data to be pushed into stack 2: ");
                scanf(" %d",&val);
                push(st,to,val);
                break;
            }
            case 3:
            {
                printf("The elem popped out of stack 1 %d: ",pop(st,te));
                break;
            }
            case 4:
            {
                printf("The elem popped out of stack 2 %d: ",pop(st,to));
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