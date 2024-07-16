#include <stdio.h>
int main()
{
	int n;
	scanf(" %d",&n);
	
	int arr[n];
	int i,j;
	for (i=0;i<n;i++)
		scanf(" %d",&arr[i]);
	
	int max,diff;
	if (arr[0]>=arr[1])
		max=arr[0]-arr[1];
	else
		max=arr[1]-arr[0];
	if (n<=1)
		return 0;
	else
	{
		for(i=0;i<n;i++)
		{
			for(j=i+1;j<n;j++)
			{
				if (arr[i]>=arr[j])
					diff=arr[i]-arr[j];
				else
					diff=arr[j]-arr[i];
			
				if (diff>=max)
					max=diff;
			}
		}
	}
	
	printf("%d",max);
}
		
	