#include<stdio.h>
void main()
{
    float matrix1[3][3]={{1,2,3},{-5,7,0},{4,-2,-21}};
    float matrix2[3][3]={{-7,6,12},{0,0,-16},{61,0,49}};
    float matrix3[3][3]={{},{},{}};
    int i,j;
    float s;
    for (i=0;i<3;i++){
        for (j=0;j<3;++j){
            s=(matrix1[i][j])+(matrix2[i][j]);
            printf("%f ",s);
            matrix3[i][j]=s;
        }
    }
    int m,n;
    for (m=0;m<3;m++){
        for (n=0;n<3;++n){
            printf("%f ",matrix3[m][n]);
        }
    }
}