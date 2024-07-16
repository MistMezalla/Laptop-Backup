#include <stdio.h>
//Proframming Excercise
void Q1()
{
    int num;
    printf("Enter the number: ");
    scanf("%d",&num);
    
    printf("%d %o %X",num,num,num);
}

void Q2()
{
    float num;
    printf("Enter the number: ");
    scanf("%f",&num);

    printf("%.2e\t%.4e\t%.8e",num,num,num);
}

void Q3()
{
    int l[10];
    int i,n;
    for (i=0;i<=9;i++)
    {
        printf("enter the number: ");
        scanf("%d",&n);
        l[i]=n;
    }   
    
    int c=0;
    for (i=0;i<3;i++)
    {
        printf("%d,%d,%d\n",l[i+c],l[i+c+1],l[i+c+2]);
        c+=2;
    }
    printf("%d",l[10]);
}

void Q4()
{
    int i,c=0;
    for (i=1;i<=200;i++)
    {
        if (i%2==0)
            c+=1;
    }
    printf("%d",c);
}

#include <string.h>
void Q5()
{
    int vow=0;
    char txt;
    fgets(txt,sizeof(txt),stdin);
    int n=strlen(txt);

    char str[n];
    int i;
    for (i=0;i<n;i++)
    {
        if (str[i]==(('a'||'A')||('e'||'E')||('o'||'O')||('u'||'U')||('i'||'I')))
            vow++;
    }
    printf("%d",vow);
}
#include <math.h>
void Q9()
{
    float p,r,t;
    printf("Enter the p,r&t: ");
    scanf("%f %f %f",&p,&r,&t);
    
    float ci;
    ci=(pow((1+r/100),t)-1)*p;
    printf("%f",ci);
}

void Q11()
{
    printf("Item\tQty\tPrice\tAmt\n");
    int c=1;
    while(c)
    {
        float bill[5][3];
        char bill_items[5][1];
        char item[100];
        printf("Enter the item: ");
        fgets(item,sizeof(item),stdin);
        //bill_items[1][1]=item;
        printf("%s\n",item);
        //printf("%s\n",bill_items);
        
        float qty,price,amt;
        printf("Enter the qty: ");
        scanf(" %f",&qty);
        printf("Enter the price: ");
        scanf(" %f",&price);
        amt=qty*price;
        //printf("%s\t%f\t%f\t%f\n",item,qty,price,amt);
        
        bill[1][1]=qty;
        bill[1][2]=price;
        bill[1][3]=amt;
        
        printf("%f\n",bill[1][1]);
        printf("%f\t%f\t%f\n",bill[1][1],bill[1][2],bill[1][3]);
        printf("Do u want to continue? c=0 or 1: ");
        scanf("%d",&c);
    }
}

void Q11_chatgpt()
{
    printf("Item\tQty\tPrice\tAmt\n");
    
    float bill[5][3];
    char bill_items[5][100]; // Make the item name array larger to store longer item names
    int item_count = 0; // Keep track of the current item index

    int c = 1;
    while (c) {
        char item[100];
        printf("Enter the item: ");
        fgets(item, sizeof(item), stdin);
        // Remove the trailing newline character
        if (item[strlen(item) - 1] == '\n') {
            item[strlen(item) - 1] = '\0';
        }
        // Copy the item name to the bill_items array
        strcpy(bill_items[item_count], item);

        float qty, price, amt;
        printf("Enter the qty: ");
        scanf("%f", &qty);
        printf("Enter the price: ");
        scanf("%f", &price);
        amt = qty * price;

        // Store the data in the bill array
        bill[item_count][0] = qty;
        bill[item_count][1] = price;
        bill[item_count][2] = amt;

        printf("%s\t%.2f\t%.2f\t%.2f\n", bill_items[item_count], bill[item_count][0], bill[item_count][1], bill[item_count][2]);

        item_count++; // Increment the item count for the next item

        printf("Do you want to continue? (0 to exit, 1 to continue): ");
        scanf("%d", &c);

        // Clear the input buffer to avoid issues with the next fgets
        while ((getchar()) != '\n');
    }

}
void str_input()
{
    char item[100];
    printf("Enter the item: ");
    fgets(item,sizeof(item),stdin);
    printf("%s",item);

    char bill_item[5][1];
    bill_item[1][1]=item;
    printf("%s",bill_item);
}

void Q12()
{
    printf("BBB  Y   Y EEEE\nB  B  Y Y  E\nBBB    Y   EEEE\nB  B   Y   E\nBBB    Y   EEEE");
}
void main()
{
    //Q11();
    //str_input();
    Q12();
}