//get() and set() methods in arraylist

package MyPackage;

import java.util.ArrayList;

public class Example3 {

	public static void main(String[] args) {
		ArrayList<Integer>arr1=new ArrayList<Integer>(2);
		arr1.add(4);
		arr1.add(5);
		arr1.add(2);
		arr1.add(9);
		arr1.add(15);
		
		System.out.println(arr1);
		arr1.set(2, 19);
		
		//System.out.println(arr1.get(3));
		
		System.out.println(arr1);
			
	
	}

}
