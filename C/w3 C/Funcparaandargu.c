#include <stdio.h>
void myfunc(char name[],int age)
{
    printf("Hi %s. Your age is %d.\n",name,age);
}
int sumof2num(int,int);
/*void main()
{
    int c=0;
    while (c==0)
    {
        char name[10]={};
        int age;
        printf("Enter your name: ");
        fgets(name,sizeof(name),stdin);
        printf("Enter your age: ");
        scanf("%d\n",&age);
        myfunc(name,age);
        printf("Do u want ot conti: ");
        scanf("%d\n",&c);
    }   

}
*/
void main()
{
 printf("%d",sumof2num(5,3));   
}

int sumof2num(int x, int y){
return x+y;
}