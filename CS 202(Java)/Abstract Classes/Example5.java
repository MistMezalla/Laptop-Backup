//Static methods can be put inside the abstract class
package MyPackage;

abstract class Base3{
	static void func() {System.out.println("Static function called");}
}

class Derived3 extends Base3{
	void fun() {System.out.println("Have fun");}
}
public class Example5 {
	public static void main(String[] args) {
		Base3.func();
		Derived3.func();
	}

}
