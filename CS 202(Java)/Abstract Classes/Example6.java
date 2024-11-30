//If a sub-class can not provide implementation of 
//all the abstract class, then the sub-class should be declared as abstract class.
package MyPackage;
abstract class Demo{
	abstract void m1();
	abstract void m2();
	abstract void m3();
}
abstract class FirstChild extends Demo{
	void m1() {System.out.println("Within m1()");}
}
abstract class SecondChild extends FirstChild{
	void m2() {System.out.println("Within m2()");}
}
class ThirdChild extends SecondChild{
	void m3() {System.out.println("Within m3()");}
}

public class Example6 {
	public static void main(String[] args) {
		Demo d=new ThirdChild();
		d.m1();
		d.m2();
		d.m3();
	}
}
