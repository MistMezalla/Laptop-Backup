#include <stdio.h>
#include <string.h>
void constant()
{
    double a=0.007;
    printf("%lu\n",sizeof(a));
    printf("%lu\n",sizeof(0.007f)); 
    /*Therefore defualt data type of real numc=bers is double.*/
}

void strlength()
{
    char str1[]="Hello";
    char str2[]={'H','e','l','l','o','\0'};
    printf("%s\n",str1);
    printf("%s\n",str2);
    printf("%d\t%d\n",strlen(str1),strlen(str2));
}

void printf_prototype()
{
    printf("%11.4e\t%010.2e\n",98.7654,98.7654);
    printf("%06d\n",123);
    printf("%-6dHi\n",123);    
    printf("%-+3.4f\n",1.234567);

    char str[]="Good Morning";
    printf("%20.10s\n",str);
}

void printf_return()
{
    printf("%d\n",printf("Hi"));
 printf("%d\n",printf("%d\t",102));
 printf("%d",printf("%f\t",1.039));
}

void scanf_prototype()
{
    int a;
    char ch;
    float b;
    scanf("%d %c ",&a,&ch);
    scanf("%f",&b);
    printf("%010d\t%c\t%f",a,ch,b);
}

void scanf_return()
{
    
}

void SE_11()
{
    int i,num,l[3];
    for(i=1;i<=3;i++)
    {
        printf("Enter number %d: ",i);
        scanf("%d",&num);
        l[i-1]=num; 
        printf("%d\t",l[i-1]);       
    }
    printf("%d",l[0]>l[1]? (l[0]>l[2]? l[0]:l[2]):(l[1]>l[2]? l[1]:l[2]));
}

void main()
{
    
    //constant();
    //strlength();
    //printf_prototype();
    //scanf_prototype();
    //SE_11();
    
   /*
    int count;
    printf("Hello%nWorld\n",&count);
    printf("%d",count);
    */
   /*
   int count;
    printf("Hello%nWorld\n", count);
    printf("Number of characters written: %d\n", count);
    */
   /*
   int x,y;
   x=y=2,4;
   printf("% d\t %d\n",x,y);
    */
   /*
   printf("%40.27s Welcome to C Programming\n");
   printf("%-40.27s Welcome to C Programming\n");
   */
  /*
  int x;
  ++x;
  printf("%d",x);
  */

}

