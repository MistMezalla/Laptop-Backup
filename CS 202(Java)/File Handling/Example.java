package MyPackage;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Example {
	public static void main(String[] args) throws IOException{
		//Creating a file
		
		
		 //File f=new File("CS202.txt"); 
		 //f.createNewFile();
		 
		   
		
		
		/*
		 * System.out.println(f.exists()); System.out.println(f.getName());
		 * System.out.println(f.getAbsolutePath());
		 * System.out.println("Can we write? "+f.canWrite());
		 * System.out.println("Can we read? "+f.canRead());
		 * System.out.println("Length of the file "+f.length());
		 */	 
		  
		  
			 		
		
		//Writing some lines to the created file
		
		
//		try 
//		{ 
//		FileWriter f = new FileWriter("CS202.txt");
//		f.write("Writing the first line\nSecond line\nThird line"); 
//		f.close(); 
//		}
//		  
//		catch (IOException e) { // TODO Auto-generated catch block
//		 e.printStackTrace(); }
//		 
		 
		 
		//Reading lines from the created file
		
		
		
		
//		  File f=new File("CS202.txt");
//		  
//		  Scanner sc = new Scanner(f);
//		  while(sc.hasNextLine()) {
//		  System.out.println(sc.nextLine()); }
//		 
		 
		
		
		  File f=new File("CS202.txt"); 
		  //f.createNewFile();
		  
		 if(f.delete()) 
		  {
		  System.out.println("The file with name CS202.txt is successfully deleted"); }
		  else {
		  System.out.println("Some problem occurred while trying to delete the file");
		  }
		  
		
		}
		 
			
	}


