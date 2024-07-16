#include <stdio.h>
//Practice for EA3 and mid sem viva

void fibo()
{
    //0 1 1 2 3 5 8 13
    int p=0,s=1;
    int n;

    scanf(" %d",&n);
    int i;

    for (i=1;i<=n;i++)
    {
        if (i==1)
            printf("%d ",p);
        else if (i==2)
            printf("%d ",s);
        else
        {
            int num;
            num=p+s;
            p=s;
            s=num;
            printf("%d ",num);
        }
    }
}

void Sorting()
{
    int arr[10]={1,1,0,5,7,6,9,4,2,4};

    int i,j;
    //descinding
    for (i=0;i<10;i++)
    {
        for(j=i+1;j<10;j++)
        {
            if(arr[i]>=arr[j])
            {
                arr[i]=arr[i]+arr[j];
                arr[j]=arr[i]-arr[j];
                arr[i]=arr[i]-arr[j];
            }
        }
    }
    for (i=0;i<10;i++)
    {
        printf("%d ",arr[i]);
    }
}

void CW()
{
    int m;
    printf("Enter the number of students: ");
    scanf(" %d",&m);

    int n;
    printf("Enter the number of subjects: ");
    scanf(" %d",&n);

    int marks[m][n];
    int i,j;
    for (i=0;i<m;i++)
    {
        for(j=0;j<n;j++)
        {
            printf("Enter the marsk of student %d in subj %d: ",i+1,j+1);
            scanf("%d",&marks[i][j]);
        }
    }

    /*
    for (i=0;i<m;i++)
    {
        for(j=0;j<n;j++)
        {
            printf("%d ",marks[i][j]);
        }
        printf("\n");
    }
    */
    int hm[m];
    for (i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
            hm[j]=marks[i][j];
    
        for (i=0;i<m;i++)
        {
            for(j=i+1;j<m;j++)
            {
                if(hm[i]<=hm[j])
                {
                    hm[i]=hm[i]+hm[j];
                    hm[j]=hm[i]-hm[j];
                    hm[i]=hm[i]-hm[j];
                }
            }
        }
        int k;
        for (k=0;k<m;k++)
            printf("%d\n",hm[k]);
        
        printf("\n");
            
        for (k=0;k<m;k++)
        {
            if(hm[0]==marks[0][k])
                printf("%d\n",k+1);
            else if (hm[m-1]==marks[0][k])
                printf("%d",k+1);
        }
    }
}

void main()
{
    //fibo();
    //Sorting();
    CW();
}