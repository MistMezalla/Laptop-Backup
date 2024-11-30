package MyPackage;

public class WrapperClassExample {
	public static void main(String[] args) {
		int num=17;
		//String ab="18";
		
		//Integer numObj=new Integer(ab)); 
				
		//int num2=numObj.intValue();
		//System.out.println(num2);		//auto unboxing
	
		
		System.out.println("\n\n......Inter class important functions....");	
		
		//System.out.println(Integer.toString(num));	
		//System.out.println(Integer.toBinaryString(num));		
		//System.out.println(Integer.toHexString(num));	
		
		System.out.println(Integer.parseInt("150"));	
		System.out.println(Integer.parseInt("150",8));	
		System.out.println(Integer.parseInt("+200",16));	
		System.out.println(Integer.parseInt("-344",12));	
		
		String ab="200";
		int val=Integer.parseInt(ab);
		
		System.out.println(ab+400);	
		System.out.println(val+400);	
		
		
	}

}
