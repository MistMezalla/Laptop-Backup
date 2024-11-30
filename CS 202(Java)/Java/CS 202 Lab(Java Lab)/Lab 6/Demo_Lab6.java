import java.util.*;

public class Demo_Lab6{
	public static void main(String []args)
	{
		int choice;
		Scanner sc = new Scanner(System.in);

		do{
			System.out.println("Enter the key number of the operation to be performed: ");
			System.out.println("1 = Addition/n2 = Subtraction/n3 = Multiplication/n0 = Exit the program");
			choice = sc.nextInt();

			switch(choice){
			case 1:
				Addition add = new Addition();
				add.input();
				add.operation();
				add.display();
				break;
			case 2:
				Subtraction sub = new Subtraction();
				sub.input();
				sub.operation();
				sub.display();
				break;
			case 3:
				Multiplication mult = new Multiplication();
				mult.input();
				mult.operation();
				mult.display();
				break;
			case 0:
				System.out.println("Exiting from the program !!!");
				break;
			default:
				System.out.println("Wrong Input !!!");
				break;
			}
		}while(choice != 0);			
	}
}

class Maths{
	protected int number1;
	protected int number2;

	public void display(){
		System.out.println("Number 1: " + number1 + "\t Number 2: " + number2);
	}

	public void input(){
		Scanner sc = new Scanner(System.in);

		System.out.println("Enter the first number: ");
		number1 = sc.nextInt();

		System.out.println("Enter the second nmumber: ");
		number2 = sc.nextInt();
	}
}

class Addition extends Maths{
	protected double result;

	public void display(){
		super.display();
		System.out.println("The result is: " + result);
	}
	
	public void operation(){
		result = number1 + number2;
	}
}

class Subtraction extends Maths{
	protected double result;

	public void display(){
		super.display();
		System.out.println("The result is: " + result);
	}
	
	public void operation(){
		result = number1 - number2;
	}
}

class Multiplication extends Maths{
	protected double result;

	public void display(){
		super.display();
		System.out.println("The result is: " + result);
	}
	
	public void operation(){
		result = number1 * number2;
	}
}
	