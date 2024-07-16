#include <stdio.h>
void EA2_Q1a()
{
    int num;
    printf("Enter the number: ");
    scanf("%d",&num);

    int nd=0,q;
    q=num;
    while(q!=0)
    {
        q/=10;
        nd+=1;
    }
    
    int i,d;
    q=num;
    while(q!=0)
    {
        int b=1;
        for (i=1;i<=nd-1;i++)
            b*=10;
        d=q/b;
        q%=b;
        nd--;
    
        switch (d)
        {
            case 0:
                printf("Zero");
                break;
            case 1:
                printf("One");
                break;
            case 2:
                printf("Two");
                break;
            case 3:
                printf("Three");
                break;
            case 4:
                printf("Four");
                break;
            case 5:
                printf("Five");
                break;
            case 6:
                printf("Six");
                break;
            case 7:
                printf("Seven");
                break;
            case 8:
                printf("Eight");
                break;
            case 9:
                printf("Nine");
                break;
        }
    
    }
}

void EA2_Q1b()
{
    int num;
    printf("Enter the number: ");
    scanf("%d",&num);

    int nd=0,q;
    q=num;
    while(q!=0)
    {
        q/=10;
        nd+=1;
    }

    int i,d,l[nd];
    q=num;
    for (i=0;i<nd;i++)
    {
        d=q%10;
        q/=10;
        l[i]=d;
    }

    for (i=nd-1;i>=0;i--)
    {
        switch (l[i])
        {
           case 0:
                printf("Zero");
                break;
            case 1:
                printf("One");
                break;
            case 2:
                printf("Two");
                break;
            case 3:
                printf("Three");
                break;
            case 4:
                printf("Four");
                break;
            case 5:
                printf("Five");
                break;
            case 6:
                printf("Six");
                break;
            case 7:
                printf("Seven");
                break;
            case 8:
                printf("Eight");
                break;
            case 9:
                printf("Nine");
                break; 
        }
    }
}

void EA2_Q2()
{
    
}
void main()
{
    EA2_Q1b();
}

