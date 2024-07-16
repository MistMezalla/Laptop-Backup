#include<stdio.h>
#include <stdbool.h>
void main()
{
    printf("%d\n",10>9); // Returns 1(True) as int data type
    printf("%f\n",1>9); // Returns 0.000000(False) as float data type

    // To assign a variable boolean value, bool type has to imported.
    bool t=true;
    printf("%d\n",t);
    
    int l[]={};
    bool m=false;
    printf("%d\n",m); //In C only (keyword) false and 0 have tvalue as 
                      // false. Empty data other data type hv tvalue
                      // as true(not same as python).
}                   
/*
#include <stdbool.h>
void main1()
{
    bool t=true;
    printf("%d\n",t);
}
*/
// The abv problem to be debugged after functions.


