#include <stdio.h>

//Q1
void Q1()
{
    int n;
    printf("Enter the size of the array: ");
    scanf(" %d",&n);

    int arr[n];
    int i,j;

    printf("Enter the data in the array: ");
    for (i=0;i<n;i++)
        scanf(" %d",&arr[i]);

    printf("\n");
    for (i=0;i<n;i++)
        printf("%d\n",arr[i]);

    for (i=0;i<n;i++)
    {
        for (j=i+1;j<n;j++)
        {
            if (arr[i]>=arr[j])
            {
                arr[i]=arr[i]+arr[j];
                arr[j]=arr[i]-arr[j];
                arr[i]=arr[i]-arr[j];
            }
        }
    }

    printf("\n");
    for (i=0;i<n;i++)
        printf("%d\n",arr[i]);
        
    int unique_arr[n];
    int k=0;
    for (i=0;i<n;i++)
    {
        for (j=i+1;j<n;j++)
        {
            if (arr[i]!=arr[j])
            {
                unique_arr[k]=arr[i];
                k++;
                i=j;
            }
        }

        if (i==n-1)
            unique_arr[k]=arr[i];
            k++;
    }


    for (i=0;i<k;i++)
        printf("%d ",unique_arr[i]);

}

//Q3
void Q3()
{
    int arr[10];

    int i,j;
    printf("Enter the elements in the array: ");
    for (i=0;i<10;i++)
        scanf(" %d",&arr[i]);

     for (i=0;i<10;i++)
    {
        for (j=i+1;j<10;j++)
        {
            if (arr[i]>=arr[j])
            {
                arr[i]=arr[i]+arr[j];
                arr[j]=arr[i]-arr[j];
                arr[i]=arr[i]-arr[j];
            }
        }
    }

    int val,pos;
    int beg,end;
    /*
    int n;
    int m;
    while (beg<=end)
    {
        pos=(beg+end)/2;
        
        if (arr[pos]==50)
        {
            n=pos;
            break;
        }
        else if (arr[pos]>50)
            end--;
        else    
            beg++;
    }

    beg=0;end=n;
    while (beg<=end)
    {
        pos=(beg+end)/2;
        
        if (arr[pos]==25)
        {
            m=pos;
            break;
        }
        else if (arr[pos]>25)
            end--;
        else    
            beg++;
    }
    */
    printf("The pairs are as follows\n: ");
    for (i=0;i<9;i++)
    {
        beg=i;end=9;
        val=50-arr[i];    
       while (beg<=end)
    {
        pos=(beg+end)/2;
        
        if (arr[pos]==val)
        {
           printf("%d %d\t",arr[i],arr[pos]);
            break;
        }
        else if (arr[pos]>val)
            end--;
        else    
            beg++;
    }
    }

}

void Q3_simple()
{
    int arr[10];

    int i,j;
    printf("Enter the elements in the array: ");
    for (i=0;i<10;i++)
        scanf(" %d",&arr[i]);

     for (i=0;i<10;i++)
    {
        for (j=i+1;j<10;j++)
        {
            if (arr[i]+arr[j]==50)
                printf("%d %d\t",arr[i],arr[j]);
        }
    }

    
}

//Q7
void Q7()
{
    int arr[10]={0,1,2,1,0,4,5,2,4,6};

    int i,j,dup=0;

    for (i=0;i<10;i++)
    {
        for (j=i+1;j<10;j++)
        {
            if (arr[i]>=arr[j])
            {
                arr[i]=arr[i]+arr[j];
                arr[j]=arr[i]-arr[j];
                arr[i]=arr[i]-arr[j];
            }
        }
    }

    for (i=0;i<10;i++)
    {
        for (j=i+1;j<10;j++)
        {
            if (arr[i]!=arr[j])
                i=j;
            else
                dup++;
        }
    }
    printf("%d",dup);
}

void Q8()
{
    int arr[10]={0,1,1,2,0,3,4,5,6,7};

    int even[10];
    int odd[10];

    int i,e=0,o=0;
    for (i=0;i<10;i++)
    {
        if (arr[i]%2==0)
        {
            even[e]=arr[i];
            e++;
        }

        else
        {
            odd[o]=arr[i];
            o++;
        }
    }

    for (i=0;i<e;i++)
        arr[i]=even[i];
    int ind=0;
    for (i=e;i<10;i++)
    {
        arr[i]=odd[ind];
        ind++;
    }

    for(i=0;i<10;i++)
        printf(" %d",arr[i]);
}

//Abv program has heavy time and space complexity.

void Q8_alt()
{
    int arr[10]={0,1,1,2,0,3,4,5,6,7};

    int i,j;
    for(i=0;i<10;i++)
    {
        for (j=i+1;j<10;j++)
        {
            if(arr[j]%2==0 && arr[i]%2!=0)
            {
                arr[i]=arr[i]+arr[j];
                arr[j]=arr[i]-arr[j];
                arr[i]=arr[i]-arr[j];
            }
        }
    }

    for (i=0;i<10;i++)
        printf("%d ",arr[i]);
}

//Q11
int sum_dia(int *,int ,int );
void Q11()
{
    int arr[3][3]={1,2,3,4,5,6,7,8,9};

    printf("%d",sum_dia(arr,3,3));
}

int sum_dia(int *a,int m,int n)
{
    int i,j;
    static int sm=0;
    for (i=0;i<m;i++)
    {
        for (j=0;j<n;j++)
        {
            if (i==j)
                sm += *((a + i*n) + j);
        }
    }
    return sm;
}

//Q12
void Q12()
{
    int arr[3][3]={0,1,2,3,4,0,5,6,7};

    int i,j,c=0;
    for (i=0;i<3;i++)
    {
        for (j=0;j<3;j++)
            if (arr[i][j]!=0)
                c++;
    }
    printf("%d",c);
}

//Q14
void Q14()
{
    float arr[5];

    int i;
    printf("Enter the elements of the array: ");
        
    for (i=0;i<5;i++)
        scanf(" %f",&arr[i]);

    for (i=0;i<5;i++)
        printf("%f ",arr[i]);

    if (10.000002==10.000002)
        printf("Eq");
    if(10.000001<10.000002)
        printf("Less");
    if(10.000004>=10.000007)
        printf("Greater");
}

//Q15
#define eps 0.000001
void Q15()
{
    float arr[5];
    int i;

    printf("Enter the elements of the array: ");
    for (i=0;i<5;i++)
        scanf(" %f",&arr[i]);

    float min=arr[0];
    int pos;
    for (i=1;i<5;i++)
    { 
        if(arr[i]<=min)
        {
            min=arr[i];
            pos=i;
        }
    }    
    printf("%f & %d",min,pos);
}

//Q18
void Q18()
{
    int mat[2][2][3]={1,2,3,4,5,6,7,8,9,10,11,12};
    int i,j,k;
    int mat_trans[3][2][2];

    for (i=0;i<2;i++)
        for (j=0;j<2;j++)
            for (k=0;k<3;k++)
                mat_trans[k][j][i]=mat[i][j][k];

     for (i=0;i<3;i++)
     {
        for (j=0;j<2;j++)
        {
            for (k=0;k<2;k++)
                printf("%d ",mat_trans[i][j][k]);    
            printf("\n");
        }
        printf("\n");
    }
}
                
//Q19
void Q19()
{
    int mat1[2][3]={10,20,30,40,50,60},mat2[3][3]={1,2,3,4,5,6,7,8,9};
    int i,j,k;
    int res[2][3];

    for (i=0;i<2;i++)
    {
        for (j=0;j<3;j++)
        {
            for (k=0;k<3;k++)
            {
                res[i][j]+=mat1[i][k]*mat2[k][j];
            }
        }
    }

    for (i=0;i<2;i++)
    {
        for(j=0;j<3;j++)
            printf("%d ",res[i][j]);
        printf("\n");
    }
}

//Q22_23
void Q22_23()
{
    int qn;
    int arr[2][3]={1,2,3,4,5,6};
    int i,j;

    do
    {
        int sm=0;
        printf("Enter the question number: ");
        scanf(" %d",&qn);

        if (qn==22)
        {
            for (i=0;i<2;i++)
                for (j=0;j<3;j++)
                {
                    if (i<j)
                        sm+=arr[i][j];
                }  
            printf("%d",sm);
        }
        if (qn==23)
        {
            for (i=0;i<2;i++)
                for (j=0;j<3;j++)
                {
                    if (i>j)
                        sm+=arr[i][j];
                }  
            printf("%d\n",sm);
        }
    }while(qn==22 || qn==23);
}

//Q24_26
int isUT(int *,int );
int isLT(int *,int );
int isSym(int *,int );
void Q24_26()
{
    int mat[3][3]={1,2,3,2,5,6,3,6,9};
    int i,j;

    int qn;
    do
    {
        printf("Enter the question number: ");
        scanf(" %d",&qn);

        if (qn==24)
            printf("%d\n",isUT(mat,3));
        if (qn==25)
            printf("%d\n",isLT(mat,3));
        if (qn==26)
            printf("%d\n",isSym(mat,3));
        

    }while (qn==24 || qn==25 || qn==26);
}

int isUT(int *a,int m)
{
    int i,j,flag;
    for (i=0;i<m;i++)
                for(j=0;j<m;j++)
                {
                    if (i>j)
                        if (*((a+i*m)+j)!=0)
                            return 0;
                        else 
                            flag=1;
                }
    if (flag)
        return 1;
}

int isLT(int *a,int m)
{
    int i,j,flag;
    for (i=0;i<m;i++)
                for(j=0;j<m;j++)
                {
                    if (i<j)
                        if (*((a+i*m)+j)!=0)
                            return 0;
                        else 
                            flag=1;
                }
    if (flag)
        return 1;
}

int isSym(int *a,int m)
{
    int i,j,flag;
    for (i=0;i<m;i++)
                for(j=0;j<m;j++)
                {
                    if ((*(a+i*m)+j)==(*(a+j*m)+i))
                        flag=1;
                    else
                        return 0;
                }
    if (flag)
        return 1;
}

//Q28
void Q28()
{
    float arr[5]={12.34,5456.123,4.0122,6789.0,0.3224};

    float max1=arr[0];
    int i;
    for (i=1;i<5;i++)
    {
        if (arr[i]>=max1)
            max1=arr[i];
    }

    float max2;
    int pos;
    if (max1!=arr[4])
        max2=arr[4];
    else 
        max2=arr[3];
    for(i=4;i>-1;i--)
    {
        if (arr[i]>=max2 && arr[i]!=max1)
        {
            max2=arr[i];
            pos=i;
        }
    }
    printf("%f,%d",max2,pos);
}

//Q30
void Q30()
{
    int arr[10]={1,2,3,4,5,6,7,8,9,10};

    int end=9,beg=0,val=3,pos;
    while(beg<=end)
    {
        pos=(end+beg)/2;
        
        if (arr[pos]==val)
        {
            printf("Found");
            break;
        }
        else if(arr[pos]>val)
            end--;
        else 
            beg++;
    }
    

}

//Q31
void Q31()
{
    int n;
    printf("Enter the size of the array: ");
    scanf("%d",&n);
    float arr[n];

    int i,j;
    printf("Enter the elements of the array: ");
    for (i=0;i<n;i++)
        scanf(" %f",&arr[i]);

    for (i=0;i<n;i++)
    {
        for(j=i+1;j<n;j++)
        {
            if (arr[i]>=arr[j])
            {
                arr[i]=arr[i]+arr[j];
                arr[j]=arr[i]-arr[j];
                arr[i]=arr[i]-arr[j];
            }
        }
    }

    for (i=0;i<n;i++)
        printf("%f ",arr[i]);
    printf("\n");

    float val=15.031;
    int pos;
    for (i=0;i<n;i++)
		if (val>=arr[i])
			pos=i+1;
	
	n++;
	for (i=n-1;i>pos;i--)
		arr[i]=arr[i-1];
		
	arr[pos]=val;

	for (i=0;i<n;i++)
		printf("%f ",arr[i]);
}

//Q32
void Q32()
{
    int n;
    printf("Enter the size of the array: ");
    scanf("%d",&n);
    float arr[n];

    int i,j;
    printf("Enter the elements of the array: ");
    for (i=0;i<n;i++)
        scanf(" %f",&arr[i]);

    int pos;
    float val=30;
    
    for (i=0;i<n;i++)
    {
        if (val==arr[i])
            pos=i;
    }
    for (i=pos;i<n-1;i++)
    {
        arr[i]=arr[i+1];
    }
    n--;

    for(i=0;i<n;i++)
        printf("%f ",arr[i]);

}

//Q36
void Q36()
{
    float arr1[4]={1.1,2.1,3.1,4.1};
    float arr2[3]={1.10,2.11,3.};
    float res[7];

    int n1,n2,n;
    n1=n2=n=0;

    while(n1<4 && n2<3)
    {
        if(arr1[n1]<=arr2[n2])
        {
            res[n]=arr1[n1];
            n++;
            n1++;
        }
        else if(arr1[n1]>=arr2[n2])
        {
            res[n]=arr2[n2];
            n++;
            n2++;
        }
    }

    int i;
    if (n1==4)
    {
        for (i=n2;i<3;i++)
        {
            res[n]=arr2[i];
            n++;
        }
    }
    if (n2==3)
    {
        for (i=n1;i<4;i++)
        {
            res[n]=arr1[i];
            n++;
        }
    }

    for (i=0;i<n;i++)
        printf("%f ",res[i]);
}
void main()
{
    Q36();   
}