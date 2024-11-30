import java.util.*;

public class Q2
{
	public static void main(String [] args)
	{
		System.out.println("Enter the size of the array: ");
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		int nums[] = new int[n];
		int i;

		for(i=0;i<n;i++)
		{
			System.out.println("Enter the number: ");
			nums[i] = sc.nextInt();
			
		}
		
		System.out.println("The elem in the arr are: ");
		for(i=0;i<n;i++)
		{
			System.out.println(nums[i]);	
		}

		duplicate(nums,n);
		System.out.println();
		sort(nums,n);
	}

	public static void duplicate(int []arr,int n)
	{
		int i,j;
		int Min_ind;
		
		for(i = 0; i < n;i++)
		{
			Min_ind = i;
			for(j=i;j<n;j++)
			{
				if (arr[j] <= arr[Min_ind])
				{
					Min_ind = j;
				}
			}
			int temp = arr[i];
			arr[i] = arr[Min_ind];
			arr[Min_ind] = temp;
		}	

		System.out.print("Duplicate elem are: ");
		
		int isEmpty = 1;
		int flag = 0;
		for (i=0;i<n-1;i++)
		{
			if (arr[i] == arr[i+1])
			{
				isEmpty = 0;
				if (flag == 0)
				{
					System.out.print(arr[i] + " ");
				}
				flag = 1;
			}
			else
			{
				flag = 0;
			}
		}
		if (isEmpty == 1)
		{
			System.out.println("None");
		}
	}

	public static void sort(int []arr,int n)
	{
		int i,j;
		int Min_ind;
		
		for(i = 0; i < n;i++)
		{
			Min_ind = i;
			for(j=i;j<n;j++)
			{
				if (arr[j] <= arr[Min_ind])
				{
					Min_ind = j;
				}
			}
			int temp = arr[i];
			arr[i] = arr[Min_ind];
			arr[Min_ind] = temp;
		}		

		System.out.println("The sorted array is: ");
		for(i=0;i<n;i++)
		{
			System.out.println(arr[i]);
		}
	}
		
}
	