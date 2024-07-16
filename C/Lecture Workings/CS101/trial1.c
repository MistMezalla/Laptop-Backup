# include <stdio.h>
void main()
{
    float b,d,h,g;
    printf("Enter the basic salary: ");
    scanf("%f",&b);
    d=20*b/100;
    h=50*b/100;
    g=b+d+h;
    printf("The gross salary is: %f",g);
}
