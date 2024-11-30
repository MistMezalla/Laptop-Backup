package MyPackage;

public class TypeCasting {
	public static void main(String[] args) {
	//.........Widening.............
		int i=25;
		double d=i;
		
		System.out.println("\n\n........Widening......");
		System.out.println("i = "+i);
		System.out.println("d = "+d);
		
	//.........Narrowing 2.............
		double k=5.6;
		int p=(int)k;
		
		System.out.println("\n\n........Narrowing......");
		System.out.println("k = "+k);
		System.out.println("p = "+p);
		

	}

}
