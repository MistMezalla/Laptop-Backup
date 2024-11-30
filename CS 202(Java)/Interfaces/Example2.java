//Implementing multiple interfaces is possible which 
//is not possible in case of abstract classes
package MyPackage;
interface BiCycle2{
	int wheels=2;
	void applyBrakes(int dec);
	void speedUP(int inc);
}
interface Horn{
	void blowHorn();
	void stopHorn();
}
class BSA2 implements BiCycle2, Horn{
	int speed=20;
	public void applyBrakes(int dec) {
		speed-=dec;
	}
	public void speedUP(int inc) {
		speed+=inc;
	}
	void showSpeed() {
		System.out.println("Speed of the cycle = "+speed);
	}
	public void blowHorn() {System.out.println("Horn started");};
	public void stopHorn() {System.out.println("Horn stopped");};
}

public class Example2 {
	public static void main(String[] args) {
		BSA2 b=new BSA2();
		b.applyBrakes(5);
		b.speedUP(15);
		b.showSpeed();
		b.blowHorn();
		b.stopHorn();
		//BiCyle.wheels=3;
		System.out.println("Showing the wheels = "+BSA2.wheels);
		
	}

}
