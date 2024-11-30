package MyPackage;
import java.util.*;
class finallyExample{
	public static int fun() {
		Scanner sc = new Scanner(System.in);
		try {
			int a =9;
			int b=0;
			int c=(b/a);
			System.out.println("ABCCCCC");
			
			return c;
		}
		catch(Exception e)
		{
			System.out.println("Class s2222 "+e);
			System.out.println("Hiiiii");
			try {
				String d = sc.nextLine();
				System.out.println(8+d+"Hi");
				System.out.println(10/0);
			}
			catch(Exception e1) {
				System.out.println(e1);
			}
			finally{
				System.out.println("Nested finally being executed!!");
				return 7;
			}
			//return 3;
		}
		finally {
			System.out.println("Cleaning up the resources");
			//return 4;
		}
		
	//tem.out.println("Outside finally ::: Cleaning up the resources");
		//return 2;
	}
	
	
}
public class ExampleFinally1 {
	public static void main(String[] args) {
		System.out.println(finallyExample.fun());
	}
}




