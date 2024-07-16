#define s_m 2
#define s_n 3
//Q5
void matrix_add(int *,int *);
void Q5()
{
    /*
    static int m,n;
    printf("Enter the size of the matrix: ");
    scanf(" %d %d",&m,&n);
    */
    int mat1[s_m][s_n],mat2[s_m][s_n];
    int i,j;

    for (i=0;i<s_m;i++)
    {
        for (j=0;j<s_n;j++)
        {
            printf("Enter the element of matrix 1: ");
            scanf(" %d",&mat1[i][j]);
        }
    }

    for (i=0;i<s_m;i++)
    {
        for (j=0;j<s_n;j++)
        {
            printf("Enter the element of matrix 2: ");
            scanf(" %d",&mat2[i][j]);
        }
    }

    matrix_add(mat1,mat2);
}

void matrix_add(int *a1,int *a2)
{
    int i,j;
    int arr[s_m][s_n];
    for (i=0;i<s_m;i++)
    {
        for (j=0;j<s_n;j++)
            arr[i][j]=*(a1+i+j)+*(a2+i+j);
    }

    for (i=0;i<s_m;i++)
    {
        for(j=0;j<s_n;j++)
            printf("%d ",arr[i][j]);
        printf("\n");
    }
}
void main()
{
    Q5();
    //printf("%d",isPrime(-20));
}