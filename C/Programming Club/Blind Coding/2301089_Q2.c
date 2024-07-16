#include <stdio.h>
void main()
{
	int n;
	scanf(" %d",&n);
	
	int arr[n];
	int i;
	for (i=0;i<n;i++)
		scanf(" %d",&arr[i]);
	
	for(i=0;i<n/2;i++)
	{
		arr[i]=arr[i]+arr[n-i-1];
		arr[n-i-1]=arr[i]-arr[n-i-1];
		arr[i]=arr[i]-arr[n-i-1];
	}

	for (i=0;i<n;i++)
		printf("%d",arr[i]);
}
