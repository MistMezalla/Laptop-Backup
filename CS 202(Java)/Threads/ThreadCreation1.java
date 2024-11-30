//Thread created by extending the Thread class
package MyPackage;

class MyThread11 extends Thread{
	@Override
	public void run() {
		int i=0;
		while(i<2) {
		System.out.println("Thread 11 is running "+i);
		i++;}
	}
}

class MyThread22 extends Thread{
	@Override
	public void run() {
		int i=0;
		while(i<2) {
		System.out.println("Thread 22 is running "+i);
		i++;}
	}
}

public class ThreadCreation1 {
	public static void main(String[] args) {
		MyThread11 t1=new MyThread11();
		MyThread22 t2=new MyThread22();
			
		t1.start();
		t2.start();
		
		for (int i=0; i<2; i++)
		System.out.println("Main thread is running "+i);
			
		//while(true)
		
		//t1.run();
		//t2.run();
	}

}
