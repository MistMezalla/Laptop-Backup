#include <stdio.h>

void main()
{
    int n;
    input_n:
    printf("Enter the number of wires: ");
    scanf(" %d",&n);
    //printf("%d",n);
    
    if (n<1)
    {
        printf("Wrong input. Please enter a integral value greater than 1.\n");
        goto input_n;
    }
    
    int wire[n];
    int i;
    for (i=0;i<n;i++)
    {
        printf("Enter the length of the wire %d: ",i+1);
        scanf(" %d",&wire[i]);
    }

    int k;
    input_k:
    printf("Enter the number 'k' in range [2,5]: ");
    scanf(" %d",&k);

    if (k<2 || k>5)
    {
        printf("Wrong input. Please enter a integral value in range [2,5].\n");
        goto input_k;
    }
    
    int steps[n];
    int t;
    switch (k)
    {
        case 2:
        case 3:
        case 5:
        {
            for (i=0;i<n;i++)
            {
                if (wire[i]%k)
                    steps[i]=k-(wire[i]%k);
                else    
                    steps[i]=wire[i]%k;
            }
            /*
            for (i=0;i<n;i++)
                printf("%d\t",steps[i]);
            */
            int min;
            min=steps[0];
            for (i=1;i<n;i++)
            {
                if(steps[i]<=min)
                    min=steps[i];
            }

            printf("%d",min);

            break;
        }
        case 4:
        {
            if(n==1)
            {
                for (i=0;i<n;i++)
                {
                if (wire[i]%k)
                    steps[i]=k-(wire[i]%k);
                else    
                    steps[i]=wire[i]%k;
                }

                int min;
                min=steps[0];
                for (i=1;i<n;i++)
                {
                    if(steps[i]<=min)
                        min=steps[i];
                }

                printf("%d",min);
            }
            else
            {
                for (i=0;i<n;i++)
                {
                    if (wire[i]%2)
                        steps[i]=2-(wire[i]%2);
                    else    
                        steps[i]=wire[i]%2;
                }
                /*
                for(i=0;i<n;i++)
                    printf("%d\t",steps[i]);
                */
                int j;
                for (i=0;i<n;i++)
                {
                    for(j=i+1;j<n;j++)
                    {
                        if (steps[i]>=steps[j])
                        {
                            steps[i]=steps[i]+steps[j];
                            steps[j]=steps[i]-steps[j];
                            steps[i]=steps[i]-steps[j];
                        }
                    }
                }
                printf("%d",steps[0]+steps[1]);
            }
        }
    }
}
