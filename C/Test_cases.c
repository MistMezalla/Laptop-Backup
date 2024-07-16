#include <stdio.h>
void main()
{
	int n;
	scanf(" %d",&n);
	
	int t,sum=0;
	t=n/3;
	sum=n+t;
	while(t)
	{
		sum+=t/3;
		t/=3;
	}
	
	printf("%d",sum);
}