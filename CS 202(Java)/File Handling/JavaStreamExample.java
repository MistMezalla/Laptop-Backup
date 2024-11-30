//Write a program to copy the content of one file to the other
package MyPackage;
import java.io.*;

public class JavaStreamExample {
	public static void main(String[] args) {
		try {
			FileInputStream in =new FileInputStream("Input.txt");
			FileOutputStream out =new FileOutputStream("Output.txt");
			
			int b;
			try {
				while((b=in.read())!=-1)
				{
					System.out.println(b);
					out.write(b);
				}
			} catch (IOException e) {
				e.printStackTrace();
			}
			finally
			{
				try {
					in.close();
					out.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
				
			}
			
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
			
			
	
		
	
	
	
	
	}

}
