//A simple example of abstract method and abstract class
package MyPackage;

abstract class Bike{
	abstract void run();
}

class Honda extends Bike{
	void run() {System.out.println("Honda bike is running");}
	void fun() {System.out.println("Have fun");}
}

public class Example1 {
	public static void main(String[] args) {
		Honda h=new Honda();
		h.run();
	}
}
