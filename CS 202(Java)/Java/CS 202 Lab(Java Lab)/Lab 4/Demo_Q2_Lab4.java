import java.util.*;

public class Demo_Q2_Lab4{
	public static void main(String[] args)
	{
		Candidate student = new Candidate();
		student.enterDetails();
		student.displayRecord();
	}
}

class Candidate{
	private int rollNo;
	private String name;
	private float score;
	private String remarks;

	public void assignRem()
	{
		if (this.score >= 50)
			this.remarks = "Selected";
		else
			this.remarks = "Not Selected";
	}
	
	public void enterDetails()
	{
		Scanner sc = new Scanner(System.in);

		System.out.println("Enter the roll number: ");
		this.rollNo = sc.nextInt();	

		System.out.println("Enter the name: ");
		this.name = sc.next();

		System.out.println("Enter the score: ");
		this.score = sc.nextFloat();
		
		assignRem();
	}
	
	public void displayRecord()
	{
		System.out.println("Roll number: "+ this.rollNo);
		System.out.println("Name: "+ this.name);
		System.out.println("Score: "+ this.score);
		System.out.println("Remarks: "+ this.remarks);	
	}
}
	
		

	
		