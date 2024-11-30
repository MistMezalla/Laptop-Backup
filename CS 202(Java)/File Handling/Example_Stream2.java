package MyPackage;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

public class Example_Stream2 {
	public static void main(String[] args){
		
		try {
			FileInputStream fin= new FileInputStream("Test.txt");
			System.out.println((char)fin.read());
			int i=fin.read();
			while(i!=-1) {
				System.out.print((char)i);
				i=fin.read();
			
			}
			
			fin.close();
			
			
		} catch (IOException e) {
			e.printStackTrace();
		}
	
	
	}
}
