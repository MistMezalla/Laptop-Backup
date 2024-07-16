#include<stdio.h>
void main()
{
    int a,b;
    scanf("%d%d",&a,&b);
    // Logical error due to implicit type casting
    /*printf("%f",a*b);*/ // Res is 0.000000
    /*printf("%d",(float)a*b);*/ // Res is 0 as format specifier is %d. 
                                 // First the value is coverted as float and the final res
                                 // is then the converted as int due format specifier.  
    printf("%d",a*b);
}
