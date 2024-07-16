#include <stdio.h>
main()
{
    float num;
    num=3.5;
    printf("%f\n",num); //Will show 6 digits
    printf("%f.1\n",num);// Will show 1 digit
    printf("%f.2\n",num);//Will show 2 digit
    printf("%f.4\n",num);//Will show 4 digit
    printf("%lu",sizeof(num));

}