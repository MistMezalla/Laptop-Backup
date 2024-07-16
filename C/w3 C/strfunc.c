#include <stdio.h>
#include"String.h"
void main()
{
    char st1[]={"Hello Everyone!"};
    printf("%d\n",strlen(st1)); //1

    char st2[]={" and Good Bye"};
    printf("%s\n",strcat(st1,st2));//2

    char st3[]={"Hi"};
    
    char st4[]={};
    
    strcpy(st4,st1);
    printf("%s\n",st3);//4: If this is after strcpy() line then Hello...Bye is printed and if bef then Hi is printed.  
    printf("%s\n",st4);//3
    
    printf("%d\n",strcmp(st1,st3));//5   

    char st5[10]={};
    printf("Enter the string: ");//6
    fgets(st5,sizeof(st5),stdin);
    printf("%s\n",st5);//7

    //Using pointers.
    //Reference
    int *pt1= &st1;
    printf("%p\n",&st1);//8
    printf("%p\n",pt1);//9

    //Dereference
    printf("%s\n",* pt1);//10: not getting the desired output. With %c some int number and with %s no output.

}
