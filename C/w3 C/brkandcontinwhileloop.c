#include<stdio.h>
void main()
{
    int i=0;

    while(i<=10){
        if (i==8){
            break;
        }
        else if(i==6){
            i++; // if this statement is not added then i=6 throughout 
                 // the loop and hence loop terminates.
            continue;
        }
        printf("%d\n",i);
        i+=1;
    }
}