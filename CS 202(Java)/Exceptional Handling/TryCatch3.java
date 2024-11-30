package MyPackage;

import java.util.Scanner;

public class TryCatch3 {
	public static void main(String[] args) {
		int[] array=new int[3];
		array[0]=18;
		array[1]=8;
		array[2]=22;
	
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter index value ");
		int ind=sc.nextInt();
		
		try {
			System.out.println("Checking index value");
			//System.out.println(array[0]/0);

			/*
			-> Note that since the abv 'div by zero' is caught by outer catch block the subseq or inside try catch
			block won't run by def of try catch blocks even if there is an error that can trigger the inside try
			block.
			 */

			try {
				System.out.println("Element at index inx "+array[ind]);
			}

			catch(ArrayIndexOutOfBoundsException e) {
				System.out.println("Hii...Array out of bound Exception "+e);
			}

			catch(Exception e)
			{
				System.out.println("Otherrrrrrrr exception "+e);
			}

			System.out.println(array[ind]);
		}
		catch(Exception e)
		{
			System.out.println("Other exception "+e);
		}
	
	
	}

}
