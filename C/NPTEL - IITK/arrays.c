#include<stdio.h>
void main()
{
    float array[]={1,2,3,4};
    
    int i=0;
    for (i=0;i<4;i++){
        printf("%f ",array[i]);
    }

    array[3]=7;
    printf("%f ",array[3]);

    int j=0;
    /*int n=len(array);*/
    // Error arouse dof implict declaration of len func. this means that a diff libray has to be impoted for its usage.
    while (j<4){
        printf("%f ",array[j]);
        j++;
    }
}