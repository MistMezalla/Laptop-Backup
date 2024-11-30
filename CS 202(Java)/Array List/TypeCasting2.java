package MyPackage;

public class TypeCasting2 {
	
	
	static void func(double a, int b) { 
		System.out.print("\nSecond func: a = "+a+ " b = "+b);}
	
	 
	public static void main(String[] args) {
		//func(2, 2);
		//func(2.5, 2);
		func(2, (int)3.5);
		// func(2.5, 3.5);
		//func(2,2);
	}
}
