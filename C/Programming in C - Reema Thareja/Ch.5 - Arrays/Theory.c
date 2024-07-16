#include <stdio.h>

//Q3
void Q3()
{
	int n;
	printf("Enter the size of the arrya: ");
	scanf(" %d",&n);
		
	int arr[n];
	int i;
	for (i=0;i<n;i++)
	{
		printf("Enter the number: ");
		scanf(" %d",&arr[i]);
	}

	int min=arr[0];
	int pos=0;
	for (i=1;i<n;i++)
	{
		if (min>=arr[i])
		{
        	min=arr[i];
			pos=i;
        }
    }
	
	printf("%d,%d",min,pos);
}

//Q4
void Q4()
{
	int n;
	printf("Enter the size of the array: ");
	scanf(" %d",&n);
		
	int arr[n];
	int i;
	for (i=0;i<n;i++)
	{
		printf("Enter the number: ");
		scanf(" %d",&arr[i]);
	}
	
	int max=arr[0],pM=0,min=arr[0],pm=0;
	for(i=1;i<n;i++)
	{
		if (max<=arr[i])
		{
			max=arr[i];
			pM=i;
		}
		if (min>=arr[i])
		{
			min=arr[i];
			pm=i;
		}
	}

	max=max+min;
	min=max-min;
	max=max-min;

	printf("%d,%d\t%d,%d",max,pM,min,pm);
}
	
//Q5
void Q5()
{
	int n;
	printf("Enter the size of the array: ");
	scanf(" %d",&n);
		
	int arr[n];
	int i;
	for (i=0;i<n;i++)
	{
		printf("Enter the number: ");
		scanf(" %d",&arr[i]);
	}

	int max1=arr[0],pos=0;
	for (i=1;i<n;i++)
	{
		if (max1<=arr[i])
		{
        	max1=arr[i];
            pos=i;
        }
    }

	int max2=arr[n-pos-1];
	for(i=0;i<n;i++)
	{
		if (i!=pos && max2<=arr[i])
		    max2=arr[i];
	}
	
	printf("%d,%d",max1,max2);
}

//Q7
void Q7()
{
	int n;
	printf("Enter the size of the array: ");
	scanf(" %d",&n);
		
	int arr[n];
	int i;
	for (i=0;i<n;i++)
	{
		printf("Enter the number: ");
		scanf(" %d",&arr[i]);
	}
	/*
	int uni[n],ind=0;
	uni[ind]=arr[0];
	*/
	int j;
	for (i=0;i<n;i++)
	{
		for (j=i+1;j<n;j++)
			if (arr[i]==arr[j])
			{
				printf("Duplicate elem persists which is %d at %d",arr[j],j);
				break;
			}
	}
}

//Q8toQ9
void Q8toQ9()
{
	int n;
	printf("Enter the size of the array: ");
	scanf(" %d",&n);
		
	int arr[n],grp[n];
	int i;
    
    for (i=0;i<n;i++)
        grp[i]=0;
	for (i=0;i<n;i++)
	{
		printf("Enter the number: ");
		scanf(" %d",&arr[i]);
		grp[arr[i]/10]++;
	}
	
	for (i=0;i<n;i++)
		printf("%d\t%d\n",i,grp[i]);

    int j;
    for (i=0;i<n;i++)
    {
        for (j=0;j<grp[i];j++)
            printf("*");
        printf("\n");
    }
		
}

//Q11
int *insert(int *,int *,int ,int ); //arr,size,vnum,pos
void Q11()
{
	int n;
	printf("Enter the size of the array: ");
	scanf(" %d",&n);
		
	int Arr[n];
	int i;
	for (i=0;i<n;i++)
	{
		printf("Enter the number: ");
		scanf(" %d",&Arr[i]);
	}

	int num,pos;
	printf("Enter the number to be inserted: ");
	scanf(" %d",&num);
	printf("Enter the postion: ");
	scanf(" %d",&pos);

	int *p;
	p=insert(Arr,&n,num,pos);
	printf("%d\n",*p);
	for (i=0;i<n;i++)
		printf("%d ",*(p+i));
}

int *insert(int *a,int *n,int num, int pos)
{
    static int arr[100];
    int i;
	
    for (i=0;i<*n;i++)
	{
        arr[i]=*a+i;
		//printf("hi ");
		//printf("\n%d",arr[i]);
	}
	//printf("%d\n",*n);
	(*n)++;
	//printf("%d\n",*n);
	for (i=(*n)-1;i>pos;i--)
	{
		//printf("Hello ");
		arr[i]=arr[i-1];
		//printf("%d",arr[i]);
	}
	arr[pos]=num;

	return arr;
}		

//Q11_alt
void Q11_alt()
{
	int n;
	printf("Enter the size of the array: ");
	scanf(" %d",&n);
	
	int i;
	int arr[n];
	for (i=0;i<n;i++)
	{
		printf("Enter the number: ");
		scanf(" %d",&arr[i]);
	}
	
	int num,pos;
	printf("enter the number to be inserted: ");
	scanf(" %d",&num);
	printf("Enter the position: ");
	scanf(" %d",&pos);

	n++;
	for (i=n-1;i>pos;i--)
		arr[i]=arr[i-1];

	arr[pos]=num;

	for(i=0;i<n;i++)
		printf("%d ",arr[i]);
}

//Q12
void Q12()
{
	int n;
	printf("Enter the size of the array: ");
	scanf(" %d",&n);
	
	int i;
	int arr[n];
	for (i=0;i<n;i++)
	{
		printf("Enter the number: ");
		scanf(" %d",&arr[i]);
	}
	
	int num,pos;
	printf("Enter the  number: ");
	scanf(" %d",&num);

	for (i=0;i<n;i++)
		if (num>=arr[i])
			pos=i+1;
	
	n++;
	for (i=n-1;i>pos;i--)
		arr[i]=arr[i-1];
		
	arr[pos]=num;

	for (i=0;i<n;i++)
		printf("%d ",arr[i]);
}	
	
//Q13
int *delete(int *,int *, int, int );
void Q13()
{
	int n;
	printf("Enter the size of the array: ");
	scanf(" %d",&n);
	
	int i;
	int arr[n];
	for (i=0;i<n;i++)
	{
		printf("Enter the number: ");
		scanf(" %d",&arr[i]);
	}
	
	int num,pos;
	//printf("Enter the  number: ");
	//scanf(" %d",&num);
	printf("Enter the postion: ");
	scanf(" %d",&pos);

	int *p;
	p=delete(arr,&n,num,pos);
	for(i=0;i<n;i++)
		printf("%d ",*(p+i));
}

int *delete(int *a,int *n,int num, int pos)
{
	static int Arr[10000];
	int i;
	for (i=0;i<*n;i++)
		Arr[i]=*(a+i);

	(*n)--;

	for (i=pos;i<*n;i++)
		Arr[i]=Arr[i+1];

	return Arr;
}
	
//Q14
int *delete(int *,int *, int, int );
void Q14()
{
	int n;
	printf("Enter the size of the array: ");
	scanf(" %d",&n);
	
	int i;
	int arr[n];
	for (i=0;i<n;i++)
	{
		printf("Enter the number: ");
		scanf(" %d",&arr[i]);
	}
	
	int num,pos;
	printf("Enter the number to be deleted: ");
	scanf(" %d",&num);

	for (i=0;i<n;i++)
		if(num==arr[i])
			pos=i;

	n--;
	for(i=pos;i<n;i++)
		arr[i]=arr[i+1];

	for(i=0;i<n;i++)
		printf("%d ",arr[i]);
}
	
//Q16
void Q16()
{
	int n1,n2;
	printf("Enter the size of 1st and 2nd arrays resp: ");
	scanf(" %d %d",&n1,&n2);

	int ind1=0,ind2=0;
	int arr1[n1],arr2[n2];

	int i;
	printf("Enter the elem fot 1st array\n");
	for(i=0;i<n1;i++)
		scanf(" %d",&arr1[i]);

	printf("Enter the elem fot 2nd array\n");
	for(i=0;i<n2;i++)
		scanf(" %d",&arr2[i]);
	
	int arr3[n1+n2];
	int j=0;
	while(ind1<n1 && ind2<n2)
	{	
		if(arr1[ind1]<=arr2[ind2])
		{
			arr3[j]=arr1[ind1];
			j++;
			ind1++;
		}
		else
		{
			arr3[j]=arr2[ind2];
			j++;
			ind2++;
		}
	}
	
	if(ind1==n1)
	{
		while(ind2<n2)
		{	
			arr3[j]=arr2[ind2];
			ind2++;
			j++;
		}
	}
	
	else
	{
		while(ind1<n1)
		{	
			arr3[j]=arr1[ind1];
			ind1++;
			j++;
		}
	}

	printf("%d\n",j);
	for (i=0;i<j;i++)
		printf("%d ",arr3[i]);

}
	
//Algo to find length of unsorted array
void Algo_1()
{
	int arr[]={3,4,2,1},len;
	len=sizeof(arr)/sizeof(arr[0]);
	printf("%d\n",len);
	printf("%d",arr[3]==1);
}

void Algo_2()
{
    // Example unsorted array
    int unsortedArray[] = {5, 2, 8, 1, 7, 3};

    // Calculate the length of the array
    int length = 0;
    while (unsortedArray[length] != '\0') {
        length++;
    }

    // Print the length
    printf("Length of the array: %d\n", length);

    return;
}

//Q18
void Q18()
{
	int i,n;
	printf("Enter the size of the array: ");
	scanf(" %d",&n);
	int arr[n];

	printf("Enter the elments of the array: ");
	for (i=0;i<n;i++)
		scanf(" %d",&arr[i]);

	int j;
	for(i=0;i<n;i++)
		for(j=i+1;j<n;j++)
		{
			if (arr[i]>=arr[j])
			{
				arr[i]=arr[i]+arr[j];
				arr[j]=arr[i]-arr[j];
				arr[i]=arr[i]-arr[j];
			}
		}


	int end,beg,val,pos;
	end=n;beg=0;
	printf("Enter the value to be searched: ");
	scanf(" %d",&val);

	while(beg<=end)
	{
		pos=(end+beg)/2;

		if (arr[pos]==val)
		{
			printf("The value is found at %d",pos);
			break;
		}
		else if (arr[pos]<val)
			beg=++pos;
		else
			end=--pos;
	}

	if (beg>end)
		printf("The value is not found.");
}

//Q20
void read(int a[],int );
void display(int a[],int );
void merge(int a[],int b[],int c[],int ,int );
void reverse(int a[],int );
void Q20()
{
	int n1,n2;
	printf("Enter the size of the arrays: ");
	scanf(" %d %d",&n1,&n2);

	int arr1[n1],arr2[n2],arr3[n1+n2];
	int choice;
	int ch_arr;
	do 
	{
		printf("\nEnter the 'choice': ");
		scanf(" %d",&choice);
		printf("\nEnter the 'ch_arr': ");
		scanf(" %d",&ch_arr);
		if (choice==1)
		{
			if (ch_arr==1)
				read(arr1,n1);
			else if(ch_arr==2)
				read(arr2,n2);
		}
		else if (choice==2)
		{
			if (ch_arr==1)
				display(arr1,n1);
			else if (ch_arr==2) 
				display(arr2,n2);
			else 
				display(arr3,n1+n2);
		}
		else if (choice==3)
			merge(arr1,arr2,arr3,n1,n2);
		else if (choice==4)
		{
			if (ch_arr==1)
				reverse(arr1,n1);
			else if(ch_arr==2) 
				reverse(arr2,n2);
			else	
				reverse(arr3,n1+n2);
		}
	}while(choice!=0);
	
}

void read(int a[],int m)
{
	int i;
	for (i=0;i<m;i++)
		scanf(" %d",&a[i]);
}

void display(int a[],int m)
{
	int i;
	for (i=0;i<m;i++)
		printf("%d ",a[i]);
}

void merge(int a[],int b[],int c[],int m1,int m2)
{
	int i;
	int ind=0;
	for (i=0;i<m1;i++)
	{
		c[ind]=a[i];
		ind++;
	}
	for(i=0;i<m2;i++)
	{
		c[ind]=b[i];
		ind++;
	}
}

void reverse(int a[],int m)
{
	int i;
	for(i=m-1;i>=0;i--)
		printf("%d ",a[i]);
}

//Q21
int min(int a[],int );
int max(int a[],int );
void interchange(int a[],int ,int );

void Q21()
{
	int n;
	printf("Enter the size of the array: ");
	scanf(" %d",&n);

	int arr[n],i;
	printf("Enter the elements of the array: ");
	for (i=0;i<n;i++)
		scanf(" %d",&arr[i]);
	
	interchange(arr,min(arr,n),max(arr,n));
	for (i=0;i<n;i++)
		printf("%d ",arr[i]);
}

int min(int a[],int l)
{
	int i;
	int m=a[0];
	int pos_m;
	for (i=1;i<l;i++)
		if (m>=a[i])
		{
			m=a[i];
			pos_m=i;
		}
	printf("Mn=%d\n",pos_m);
	return pos_m;
}

int max(int a[],int l)
{
	int i;
	int M=a[0];
	int pos_M;
	for (i=1;i<l;i++)
		if (M<=a[i])
		{
			M=a[i];
			pos_M=i;
		}
	printf("Mx=%d\n",pos_M);
	return pos_M;
}

void interchange(int a[],int x,int y)
{
	a[x]=a[x]+a[y];
	a[y]=a[x]-a[y];
	a[x]=a[x]-a[y];
}

//Q25to26
void Q25to26()
{
	int db[3][4];
	int i,j;
	
	for (i=0;i<3;i++)
		for (j=0;j<3;j++)
		{
			printf("Enter the marks of the student %d in subj %d: ",i+1,j+1);
			scanf(" %d",&db[i][j]);
		}
	
	for (i=0;i<3;i++)
		for (j=0;j<3;j++)
			db[i][3]+=db[i][j];

	float avg[5];
	for (i=0;i<3;i++)
		avg[i]=db[i][3]/3;
	
	for (i=0;i<3;i++)
	{
		printf("Student %d\nsubj 1 subj 2 subj 3 total avg\n",i+1);
		for (j=0;j<4;j++)
			printf("%d\t",db[i][j]);
		printf("%f",avg[i]);
		printf("\n");
	}
	
	float sum;
	for (i=0;i<3;i++)
		sum+=avg[i];

	printf("The average of the class is: %f",sum/3);


}

//Q30
void Q30()
{
	int m1,n1,m2,n2;
	printf("Enter the size of matrix 1: ");
	scanf(" %d %d",&m1,&n1);
	printf("Enter the size of matrix 2: ");
	scanf(" %d %d",&m2,&n2);

	int mat1[m1][n1],mat2[m2][n2];
	if (n1!=m2)
		printf("Matrix multiplication not possible.");

	int i,j;
	
	printf("Enter the values of the matirx 1: ");
	for(i=0;i<m1;i++)
		for (j=0;j<n1;j++)
			scanf(" %d",&mat1[i][j]);
	
	printf("Enter the values of the matirx 2: ");
	for(i=0;i<m2;i++)
		for (j=0;j<n2;j++)
			scanf(" %d",&mat2[i][j]);

	int res[m1][n2],k;
	for (i=0;i<m1;i++)
	{
		for (k=0;k<n2;k++)
			for (j=0;j<n2;j++)
				res[i][k]+=mat1[i][j]*mat2[j][k];
	}

	for (i=0;i<m1;i++)
	{
		for (j=0;j<n2;j++)
			printf("%d ",res[i][j]);
		printf("\n");
	}
}

//Q32
void Q32()
{
	int mat[2][3];
	int i,j;

	for (i=0;i<2;i++)
	{
		for (j=0;j<3;j++)
		{
			if (i>j)
				mat[i][j]=-1;
			else if (i==j)
				mat[i][j]=0;
			else	
				mat[i][j]=1;
		}
	}

	for (i=0;i<2;i++)
	{
		for (j=0;j<3;j++)
			printf("%d",mat[i][j]);
		printf("\n");
	}
}

//Q33
void Q33()
{
	int mat[][2][2]={1,2,3,4,5,6,7,8};
	int i,j,k;
	/*
	printf("Enter the data in the 3D matrix: ");
	for (i=0;i<2;i++)
		for (j=0;j<2;j++)
			for (k=0;k<2;k++)
				scanf(" %d",&mat[i][j][k]);
	*/
	for (i=0;i<2;i++)
	{
		for(j=0;j<2;j++)
		{
			for (k=0;k<2;k++)
				printf("%d\t",mat[i][j][k]);
			printf("\n");
		}
		printf("\n");
	}
}

//Sparse matirx
void Sp_mat()
{
	int mat[3][3]={0,2,0,1,0,4,0,1,0};
	int i,j;

	int r,c;
	r=c=3;

	int  non_zero=0;
	for (i=0;i<3;i++)
		for (j=0;j<3;j++)
			if(mat[i][j]!=0)
				non_zero++;

	int sp_mat[non_zero][c];
	int x,y,val,ind=0;
	for (i=0;i<non_zero;i++)
	{
		sp_mat[0][0]=r;
		sp_mat[0][1]=c;
		sp_mat[0][2]=non_zero;
		for(j=0;j<3;j++)
		{
			if(mat[i][j]!=0 && i<r)
			{
				val=mat[i][j];
				x=i;
				y=j;
			}
		
			if (ind==0)
			{
				sp_mat[i+1][ind]=x;
				ind++;
			}
			else if (ind==1)
			{
				sp_mat[i+1][ind]=y;
				ind++;
			}
			else 
			{
				sp_mat[i+1][ind]=val;
				ind==0;
			}
		}
	}

	for (i=0;i<non_zero;i++)
	{
		for (j=0;j<c;j++)
			printf("%d ",sp_mat[i][j]);
		printf("\n");
	}
}

void main()
{
    Sp_mat();
}