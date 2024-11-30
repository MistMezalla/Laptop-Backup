package MyPackage;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;

public class Example_Stream1 {
	public static void main(String[] args) {
		try{
			FileOutputStream f=new FileOutputStream("Test.txt");
			//f.write(97);
			
			String s= "Hello World";
			byte b[]=s.getBytes();
			System.out.println(b);
			f.write(b);
			f.close();
			
		} catch (IOException e) {
			e.printStackTrace();
		}

	
	}

}
