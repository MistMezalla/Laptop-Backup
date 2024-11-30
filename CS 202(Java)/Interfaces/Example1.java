package MyPackage;
interface BiCycle{
	int wheels=2;
	void applyBrakes(int dec);
	void speedUP(int inc);
}
class BSA implements BiCycle{
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
}
public class Example1 {
	public static void main(String[] args) {
		BSA b=new BSA();
		b.applyBrakes(5);
		b.speedUP(15);
		b.showSpeed();
		
		//BiCycle.wheels=3;
		System.out.println("Showing the wheels = "+BSA.wheels);
		
	}

}
