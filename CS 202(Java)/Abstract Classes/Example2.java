package MyPackage;

abstract class Bank{
	abstract int getRateofInterest();
}

class SBI extends Bank{
	int getRateofInterest() {
		return 7;}
}

class Canara extends Bank{
	int getRateofInterest() {
		return 8;}
}

public class Example2 {

	public static void main(String[] args) {
		Bank b=new SBI();
		System.out.println("Rate of SBI = "+b.getRateofInterest());
		
		b=new Canara();
		System.out.println("Rate of Canara = "+b.getRateofInterest());		
	}

}
