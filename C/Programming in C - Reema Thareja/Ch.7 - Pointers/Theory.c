#include <stdio.h>
#include <ctype.h>

//Q7
void Q7()
{
    char *pch,ch;
    printf("Enter the character: \n");
    scanf(" %c",&ch);

    pch=&ch;
    printf("%c\t%c",*pch,toupper(*pch));    
}

//Q8
void Q8()
{
    char *pch,ch;
    scanf(" %c",&ch);
    pch=&ch;

    switch(isalnum(*pch))
    {
        case 2:
            printf("LC");
            break;
        case 1:
            printf("Uc");
            break;
        case 4:
            printf("Dig");
            break;
    }
    printf("\n%d",isalnum(*pch));
    //printf("Hi");
}

//Q13
int isPrime(int n)
{
    int i,flag=1;
    
    if (n==2 || n==1)
        return 1;
    else if(n>2)
    {
        for (i=2;i<=(n/2);i++)
        {
            if(n%i==0)
            {
                flag=0;
                break;
            }
        }
    }
    if (flag)
        return 1;
    else 
        return 0;
}

void Q13()
{
    int *pnum,num; 
    pnum=&num;
    
    printf("Enter the number : ");
    scanf( " %d",pnum);
    while (*pnum!=-1)
    {
        if(isPrime(*pnum))
            printf("%d is prime\n",*pnum);
        else 
            printf("%d is not prime\n",*pnum);

        printf("Enter the number : ");
        scanf( " %d",pnum);
    }
}

//Q14
void Q14()
{
    int *a,*b,n1,n2;
    
    a=&n1,b=&n2;
    printf("Enter the two numbers: ");
    scanf(" %d %d",a,b);

    printf("%d\n",add(a,b));
    printf("%d",n1);
}
int add(int *a,int *b)
{
    *a+=*b;
    return 0;
}

//Q20
void insertion_sort_asc(int a[],int n)
{
    int i,pos=0,min=a[0];
    for (i=1;i<n;i++)
    {
        if(a[i]<=min) 
            pos=i;
    }

    a[pos]=a[pos]+a[0];
    a[0]=a[pos]-a[0];
    a[pos]=a[pos]-a[0];

    int j;
    for (i=1;i<n;i++)
    {
        for(j=i-1;j>=0;j--)
        {
            if (a[i]>=a[j])
            {
                pos=j+1;
                break;
            }
        }
        int temp=a[i];
        int k;
        for(k=i;k>=pos+1;k--)
            a[k]=a[k-1];
        a[pos]=temp;
    }
}
void Q20()
{
    int n;
    printf("Enter the size of the array: ");
    scanf(" %d",&n);

    int arr[n];
    int *parr=arr;
    
    int i;
    printf("Enter the elem of the arry: ");
    for(i=0;i<n;i++)
        scanf(" %d",(parr+i));

    insertion_sort_asc(parr,n);
    printf("The sorted elements of the array are: ");
    for(i=0;i<n;i++)
        printf("%d ",*(parr+i));
}

//Q22
void print_str(char *pstr)
{
    printf("%s\n",pstr);
}

int n_char_str(char *pstr)
{
    int i=0;
    while(pstr[i]!='\0')
        i++;

    return i;
}

int n_word_str(char *pstr)
{
    int word=0,i;
    int n=n_char_str(pstr);

    for (i=0;i<n;i++)
    {
        if (ispunct(pstr[i]) || isspace(pstr[i]) && i!=0)
           // if ((ispunct(pstr[i])!=0 && isspace(pstr[i+1])==0) || (ispunct(pstr[i])==0 && isspace(pstr[i+1])!=0))
                    word++;
    }
    return word;
}

int n_lines_str(char *pstr)
{
    int n=n_char_str(pstr);
    int lines=0,i;
    
    for (i=0;i<n;i++)
    {
        if (pstr[i]=='.' && i!=0)
            lines++;
    }

    return lines;
}

void Q22()
{
    char str[100];
    printf("Enter the string: ");
    gets(str);

    char *pstr=str;
    
    //printf("%d",n_char_str(pstr));
    
    print_str(pstr);
    printf("%d\t%d\t%d",n_char_str(pstr),n_word_str(pstr),n_lines_str(pstr));
    
}


//Q26
void read_str(char *pstr)
{
    printf("Enter the string: ");
    gets(pstr);
}

void del_semicol(char *pstr)
{
    int n=n_char_str(pstr);
    int i,j;
    for (i=0;i<n;i++)
    {
        if (pstr[i]==';')
        {
            for (j=i;j<n;j++)
                pstr[j]=pstr[j+1];
            n--;
        }
    }

    print_str(pstr);
    printf("\n");
}

void edit_str(char *pstr)
{
    int n=n_char_str(pstr);
    int i;
    for(i=0;i<n;i++)
    {
        if (pstr[i]=='.')
            pstr[i]=',';
    }

    print_str(pstr);
    printf("\n");
}

void Q26()
{
    char str[100];
    char *pstr=str;

    read_str(pstr);
    print_str(pstr);
    printf("\n");
    del_semicol(pstr);
    edit_str(pstr);
}

//Pointer and 2D array
void ptr_2Darray()
{
    int arr[3][2]={1,2,3,4,5,6};
    int (*a)[3]=arr;

    int i,j;
    /*
    for (i=0;i<2;i++)
        for (j=0;j<3;j++)
            scanf(" %d",&a[i][j]);
    */
    printf("%d\n",a[0][0]);
    for (i=0;i<2;i++)
    {
        for (j=0;j<3;j++)
            printf("%d ",a[i][j]);
    }
}

//Q30
typedef int (*fp)(int ,int );

int sum(int a,int b)
{
    return a+b;
}

int sub(int a,int b)
{
    return a-b;
}

int mul(int a,int b)
{
    return a*b;
}

int div(int a,int b)
{
    return a/b;
}

void Q30()
{
    int ch;
    do
    {
        int m,n;
        fp op[4];
        op[0]=sum;
        op[1]=sub;
        op[2]=mul;
        op[3]=div;
        printf("Enter your choice: ");
        scanf(" %d",&ch);

        printf("Enter the numbers: ");
        scanf(" %d %d",&m,&n);

        printf("%d\n",op[ch](m,n));
    }while(ch>=0);
    
}

void main()
{
    Q30();
    //ptr_2Darray();
    /*
    int *ptr;
    printf("%u\n",ptr);
    ptr=NULL;
    printf("%u ",ptr);
    if (ptr==NULL)
    {   
        printf("NULL");
    }
    else 
        printf("Not NULL");
    */
}