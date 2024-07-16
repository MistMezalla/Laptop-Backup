#include <stdio.h>

void even_odd(int n)
{
        int q,nd=0;
        q=n;
        while(q!=0) //Counting no of digits
        {
                q/=10;
                nd+=1;
        }

        int l[n];
        int i,d;
        q=n;
        for (i=0;i<nd;i++) //Adding digits into array.
        {
                d=q%10;
                q/=10;

                l[i]=d; //Reverse addition of digits.
        }

        int a=(nd+1)/2,b=(nd-1)/2;
        int lo[a],le[b];

	  for (i=0;i<nd;i++)
        {
                if (i%2==0)
                {
                        lo[a-1]=l[i];
                        a--;
                }
                else
                {
                        le[b-1]=l[i];
                        b--;
                }
        }

        printf("The digits at odd places of n are: \n");
        for (i=0;i<(nd+1)/2;i++)
                printf("%d\t",lo[i]);
        printf("\n");

        printf("The digits at even places of n are: \n");
        for (i=0;i<(nd-1)/2;i++)
                printf("%d\t",le[i]);
}

void factorial(int n)
{
        int q,nd=0;
        q=n;
        while(q!=0) //Counting no of digits
        {
                q/=10;
                nd+=1;
        }

        int l[n];
        int i,d;
        q=n;
        for (i=0;i<nd;i++) //Adding digits into array.
        {
                d=q%10;
                q/=10;

                l[i]=d; //Reverse addition of digits.
		    }

        int a=(nd+1)/2,b=(nd-1)/2;
        int lo[a],le[b];
        for (i=0;i<nd;i++)
        {
                if (i%2==0)
                {
                        lo[a-1]=l[i];
                        a--;
                }
                else
                {
                        le[b-1]=l[i];
                        b--;
                }
        }

        int sum=0;
        for (i=0;i<(nd-1)/2;i++)
                sum+=fact(l[i]);
        printf("%d",sum);
}


void new_num(int n)
{
        int q,nd=0;
        q=n;
        while(q!=0) //Counting no of digits
        {
                q/=10;
                nd+=1;
        }

        int l[n];
        int i,d;
        q=n;
        for (i=0;i<nd;i++) //Adding digits into array.
        {
                d=q%10;
                q/=10;

                l[i]=d; //Reverse addition of digits.
        }

        int a=(nd+1)/2,b=(nd-1)/2;
        int lo[a],le[b];
	  for (i=0;i<nd;i++)
        {
                if (i%2==0)
                {
                        lo[a-1]=l[i];
                        a--;
                }
                else
                {
                        le[b-1]=l[i];
                        b--;
                }
        }

        int num=0,j;
        for (i=0;i<(nd+1)/2;i++)
        {
                int b=1;
                for (j=(nd-1)/2;j>i;j--)
                        b*=10;
                num+=lo[i]*b;
        }

        printf("Number formed with digits at odd palces (m) %d\n",num);

        printf("The factors of %d are: \n",num);
	  for (i=1;i<num;i++)
        {
                if(num%i==0)
                        printf("%d\t",i);
        }


}

int isPrime(int n)
{
        int q,nd=0;
        q=n;
        while(q!=0) //Counting no of digits
        {
                q/=10;
                nd+=1;
        }

        int l[n];
        int i,d;
        q=n;
	  for (i=0;i<nd;i++) //Adding digits into array.
        {
                d=q%10;
                q/=10;

                l[i]=d; //Reverse addition of digits.
        }
        for (i=0;i<nd;i++)
        {
                if (i%2==0)
                {
                        lo[a-1]=l[i];
                        a--;
                }
                else
                {
                        le[b-1]=l[i];
                        b--;
                }
        }

        int num=0,j;
        for (i=0;i<(nd+1)/2;i++)
        {
                int b=1;
		     for (j=(nd-1)/2;j>i;j--)
                        b*=10;
                num+=lo[i]*b;
        }


        int a=(nd+1)/2,b=(nd-1)/2;
        int lo[a],le[b];

        int j,flag;
        int prime[];
        int non_prime[];
        for (i=1;i<num;i++)
        {
                if(num%i==0)

                                for (j=2;j<i;j++)
                                {
                                        if (i%j==0)
                                                flag=1; //not prime
                                        else
                                                flag=0; //prime
                                }
        }
}
void main()
{
        int num;
        printf("Enter the number: ");
        scanf("%d",&num);

        even_odd(num);
        //factorial(num);
        //new_num(num);

}

	