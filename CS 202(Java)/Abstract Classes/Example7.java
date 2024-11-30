//We can use top-level (outer class) and inner classes as abstract
package MyPackage;

abstract class A{
	abstract class B{
		abstract void fun();
	}
}

class A1 extends A{
	class B1 extends B{
		void fun() {System.out.println("Have fun");}
	}
}

public class Example7 {
	public static void main(String[] args) {
		A1 a=new A1();
		A1.B1 b=a.new B1();
		b.fun();
	}
}
