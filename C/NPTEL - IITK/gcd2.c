#include <stdio.h>
void main()
{
    int a,b,t;
    scanf("%d%d ",&a,&b);

    printf("gcd of %d and %d is \n",a,b);
    while(!(b==0)){
        t=a;
        a=b;
        b=t%b;
    }
    printf("%d\n",a);
}