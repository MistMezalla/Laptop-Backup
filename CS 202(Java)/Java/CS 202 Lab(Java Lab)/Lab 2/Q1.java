import java.util.*;

public class Q1
{
	public static void main(String []args)
	{
		System.out.println("Enter the marks: ");
		Scanner sc = new Scanner(System.in);
		int marks = sc.nextInt();
		
		if (marks > 90 && marks <= 100)
		{
			System.out.println("Grade: O");
		}
		else if (marks >= 85 && marks <= 90)
		{
			System.out.println("Grade: A");
		}
		else if (marks >= 75 && marks <= 84)
		{
			System.out.println("Grade: B");
		}
		else if (marks >= 50 && marks <= 74)
		{
			System.out.println("Grade: C");
		}
		else if (marks >= 0 && marks <= 49)
		{
			System.out.println("Grade: F");
		}
		else
		{
			System.out.println("Grade: X");
		}
		
	}
}
		
		