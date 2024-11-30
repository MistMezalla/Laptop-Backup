//abstract class can be created without abstract methods
package MyPackage;
abstract class Base{
	void func() {System.out.println("Hello");}
}

class Derived extends Base{
	void newfunc() {System.out.println("Within Derived");}
}

public class Example4 {
	public static void main(String[] args) {
		Base b=new Base();
		b.func();
		//b.newfunc();   ---> This line throws an error. Find out Why.
	}
}
