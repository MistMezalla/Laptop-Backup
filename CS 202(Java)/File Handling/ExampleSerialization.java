package MyPackage;
import java.io.*;

class Employee implements Serializable{
	String name;
	int emp_id;
}
public class ExampleSerialization {
	public static void main(String[] args) {
		Employee e=new Employee();
		e.name="Arijit";
		e.emp_id=231;
		
		
		
		try {
			FileOutputStream fin = new FileOutputStream("Serial.txt");
			ObjectOutputStream oin=new ObjectOutputStream(fin);
			oin.writeObject(e);
			oin.close();
			fin.close();
		} catch (FileNotFoundException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		} catch (IOException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
		
	}

}
