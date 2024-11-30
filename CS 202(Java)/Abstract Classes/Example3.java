//abstract class can have constructors and normal methods
package MyPackage;

abstract class Bike2{
	Bike2(){System.out.println("Bike created");}
	abstract void run();
	void changeGear() {
		System.out.println("Gear changed");
	}
}

class Honda2 extends Bike2{
	Honda2(){System.out.println("Honda created");}
	void run() {System.out.println("Honda bike is running smoothly");}
}

public class Example3 {
	public static void main(String[] args) {
		Bike2 b=new Honda2();
		b.run();
		b.changeGear();
	}

}
