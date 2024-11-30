//Default methods in interfaces. Default methods 
//help in extending the interfaces without disturbing the 
//classes that implement the interface
package MyPackage;

interface Camera{
	void takeSnapshot();
	void recordVideo();
	private void helloWorld() {System.out.println("Hello world");}
	default void recordVideoEnhanced() {
	helloWorld();	
	System.out.println("Enhanced video recording");}}

interface Wifi{
	String [] getNetwork();
	void connectToNetwork(String network);
}

class CellPhone{
	int cell_id;
	void callNumber(int phoneNumber) {System.out.println("Calling number "+phoneNumber);}
	void pickCall() {System.out.println("Connencting"); }
}

class SmartPhone extends CellPhone implements Camera, Wifi{
	public void takeSnapshot() 
	{
		if(cell_id==0)
		{
			System.out.println("Hellooooooo");
		}
		System.out.println("Taking snapshots");
	}
	public void recordVideo() {System.out.println("Recording video");}
	public String[] getNetwork(){
		String[] nets= {"Alex", "IIITG", "CSE IIITG"};
		return nets;
	}
	public void connectToNetwork(String network) {
		System.out.println("Connecting to network "+network);}
	void smartCallreceive() {
		System.out.println("Smartphone feature : Smart call receive");
	}

}

public class Example3 {
	public static void main(String[] args) {
		SmartPhone p=new SmartPhone();
		p.recordVideoEnhanced();
		
		Camera c=new SmartPhone();
		c.takeSnapshot();
		c.recordVideo();
		c.recordVideoEnhanced();
		//c.callNumber(123);  Not allowed as you are allowed to use object c only as a camera
		
	}

}


//String[] sh=p.getNetwork();
		//for(int i=0; i<sh.length;i++)
		//System.out.print(sh[i]+" ");
		//p.helloWorld();
