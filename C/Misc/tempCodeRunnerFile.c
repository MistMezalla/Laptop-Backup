//Q1
void Q1()
{
    int n;
    printf("Enter the size of the array: ");
    scanf(" %d",&n);

    int *arr=(int *)calloc(n,sizeof(int));

    int i;
    printf("Enter the elements of the array: \n");
    for (i=0;i<n;i++)
        scanf(" %d",&arr[i]);

    for (i=0;i<n;i++)
        printf("%d ",arr[i]);
    printf("\n");

    int min=arr[0],pos=0;
    for (i=1;i<n;i++)
    {
        if (arr[i]<=min)
        {
            min=arr[i];
            pos=i;
        }
    }

    arr[0]=arr[0]+arr[pos];
    arr[pos]=arr[0]-arr[pos];
    arr[0]=arr[0]-arr[pos];

    int j;
    for (i=0;i<n;i++)
    {
        for(j=i-1;j>=0;j--)
        {
            if(arr[i]>=arr[j])
            {
                pos=j+1;
                break;
            }
        }

        int temp;
        temp=arr[i];
        for (j=i;j>=pos+1;j--)
            arr[j]=arr[j-1];
        arr[pos]=temp;
    }

    for (i=0;i<n;i++)
        printf("%d ",arr[i]);
    printf("\n");
}
