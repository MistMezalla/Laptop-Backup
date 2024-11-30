package MyPackage;

interface Interface1{
	void method1();
	void method2();
}

interface Interface2 extends Interface1{
	void method3();
	void method4();
}

class ABC implements Interface2{
	public void method1() {System.out.println("Method 1");}
	public void method2() {System.out.println("Method 2");}
	public void method3() {System.out.println("Method 3");}
	public void method4() {System.out.println("Method 4");}
}

public class Example4 {
	public static void main(String[] args) {
		ABC obj=new ABC();
		obj.method1();
		obj.method2();
		obj.method3();
		obj.method4();		
	}

}
