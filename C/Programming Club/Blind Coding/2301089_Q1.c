#include <stdio.h>
void main()
{
	int n;
	scanf(" %d",&n);
	
	int i,j,k;
	for (i=0;i<n;i++)
	{
		for (k=0;k<i;k++)
			printf("#");
		for (j=0;j<n-i;j++)
			printf("%d",j);
		printf("\n");
	}
}
	