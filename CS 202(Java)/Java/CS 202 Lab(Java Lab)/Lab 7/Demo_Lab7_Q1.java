import java.util.*;
public class Demo_Lab7_Q1{
	public static void main(String []args)
	{
		Scanner sc = new Scanner(System.in);
		int choice;
		do{
			System.out.println("Enter the choice: ");
			System.out.println("1 = SBI\n2 = PNB\n3 = BOI\n0 = Exit the program");
			choice = sc.nextInt();
			double bal;

			switch(choice)
			{
				case 1:
					System.out.println("Enter the bal for this a/c: ");
					bal = sc.nextDouble();
					SBI SBI_ac = new SBI(bal);
					SBI_ac.addInterest();
					SBI_ac.display();
					break;
				case 2:
					System.out.println("Enter the bal for this a/c: ");
					bal = sc.nextDouble();
					PNB PNB_ac = new PNB(bal);
					PNB_ac.addInterest();
					PNB_ac.display();
					break;
				case 3:
					System.out.println("Enter the bal for this a/c: ");
					bal = sc.nextDouble();
					BOI BOI_ac = new BOI(bal);
					BOI_ac.addInterest();
					BOI_ac.display();
					break;
				case 0:
					System.out.println("Exiting the program !!!");
					break;
				default:
					System.out.println("Wrong Input!!");
			}
		}while(choice != 0);

	}
}

class Bank{
	static double totalBalance;

	void display()
	{
		System.out.println("The total avl bal is: " + totalBalance);
	}
}

class SBI extends Bank{
	double rateOfinterest = 3.5;
	double localBalance;

	void display()
	{
		System.out.println("Balance in SBI a/c: ");
		System.out.println("Rate of interest: " + rateOfinterest + "\nLocal bal: " + localBalance);
		super.display();
	}

	void addInterest()
	{
		totalBalance -= localBalance;
		localBalance += rateOfinterest * localBalance / 100;
		totalBalance += localBalance;
		//System.out.println("Total bal upon adding the interest to this a/c: ");
		//super.display();
	}

	SBI(double localBalance)
	{
		this.localBalance = localBalance;
		totalBalance += localBalance;
		//System.out.println("Total bal upon opening the a/c: ");
		//super.display();
	}
}

class PNB extends Bank{
	double rateOfinterest = 4;
	double localBalance;

	void display()
	{
		System.out.println("Balance in PNB a/c: ");
		System.out.println("Rate of interest: " + rateOfinterest + "\nLocal bal: " + localBalance);
		super.display();
	}

	void addInterest()
	{
		totalBalance -= localBalance;
		localBalance += rateOfinterest * localBalance / 100;
		totalBalance += localBalance;
		//System.out.println("Total bal upon adding the interest to this a/c: ");
		//super.display();
	}

	PNB(double localBalance)
	{
		this.localBalance = localBalance;
		totalBalance += localBalance;
		//System.out.println("Total bal upon opening the a/c: ");
		//super.display();
	}
}

class BOI extends Bank{
	double rateOfinterest = 5;
	double localBalance;

	void display()
	{
		System.out.println("Balance in BOI a/c: ");
		System.out.println("Rate of interest: " + rateOfinterest + "\nLocal bal: " + localBalance);
		super.display();
	}

	void addInterest()
	{
		totalBalance -= localBalance;
		localBalance += rateOfinterest * localBalance / 100;
		totalBalance += localBalance;
		//System.out.println("Total bal upon adding the interest to this a/c: ");
		//super.display();
	}

	BOI(double localBalance)
	{
		this.localBalance = localBalance;
		totalBalance += localBalance;
		//System.out.println("Total bal upon opening the a/c: ");
		//super.display();
	}
}