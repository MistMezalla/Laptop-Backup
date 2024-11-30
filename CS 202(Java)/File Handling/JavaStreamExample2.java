package MyPackage;
import java.io.*;

public class JavaStreamExample2 {
	public static void main(String[] args) {
		try {
			FileReader in=new FileReader("Input.txt");
			FileWriter out=new FileWriter("Output.txt");
			int c;
			
			while((c=in.read())!=-1)
			{
				//System.out.println((char)c);
				out.write(c);
			}
			//out.close();
			out.flush();
			
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		
	}

}
