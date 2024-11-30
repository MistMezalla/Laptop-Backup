import java.util.*;

public class Demo_Lab3_Q2 {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Enter the first number: ");
		int a = sc.nextInt();

		System.out.println("Enter the second number: ");
		int b = sc.nextInt();

		System.out.println("Enter the operator out of these ('+','-','*','/') only");
		String oper = sc.next();

		Operation obj = new Operation(a,oper,b);
		obj.calculateValue();
		obj.displayResult();
	}
}