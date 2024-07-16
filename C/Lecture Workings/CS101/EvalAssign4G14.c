#include <stdio.h>
void main()
{
    int i,j;
    int arr1[5][3]={{4,50,40}, {5,60,90},{3,20,30},{1,50,70},{2,90,70}};
    int arr2[5];    // for storing sum
    // arr1[0][0]="Roll ";
    // arr1[0][1]="S1";
    // printf("")

    for (i = 0; i < 5; i++)
    {  int sum=0;  //jb bhi next row me enter krega to sum =0 hoga
        for (j = 1; j < 3; j++)
        {
            sum += arr1[i][j];
        
        }
          arr2[i]=sum;
    }
    for (i = 0; i < 5; i++)//bubble sorting in ascending order
    {
        for (j = 0; j < 4 - i; j++)
        {
            if (arr2[j] > arr2[j + 1])
            {
                int temp = arr2[j];
                arr2[j] = arr2[j + 1];
                arr2[j + 1] = temp;
            }
        }
    }

printf("Roll No Marks\n");
for(i=0;i<5;i++)
{   //printf(" The total marks of roll %d is: ",arr1[i][0]);
    printf("%d\t%d\n",arr1[i][0],arr2[i]);}

int arr3[5];
for(i=0;i<5;i++);
    arr3[i]=arr2[i];

for (i=0;i<5;i++)
{
    for (j=i+1;j<5;j++)
    {
        arr3[i]=arr3[i]+arr3[j];
        arr3[i]=arr3[i]-arr3[j];
        arr3[j]=arr3[i]-arr3[j];
    }
}

for (i=0;i<5;i++)
{
    for(j=0;j<5;j++)
    {
        if (arr3[i]==arr2[j])
            printf("%d\t%d",arr1[j][0],arr2[j]);
        printf("\n");
    }
}

}