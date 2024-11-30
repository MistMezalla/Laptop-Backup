//add, remove, removeif, contains, indexof, replaceAll
package MyPackage;

import java.util.*;

public class Example1 {
	public static void main(String[] args) {
		int n=5;
		
		ArrayList<Integer>arr1=new ArrayList<Integer>(2);
		ArrayList<Integer>arr2=new ArrayList<Integer>(n);
		
		System.out.println("\nArray 1 = "+arr1);
		//System.out.println("\nArray 2 = "+arr2);
	
		arr1.add(4);
		arr1.add(3);
		arr1.add(5);
		arr1.add(86);
	
		arr2.add(40);
		arr2.add(19);
		arr2.add(5);
		arr2.add(58);
		arr2.add(5);
		
		//arr1.remove(1);
		//System.out.println("\nArray 1 = "+arr1);
		
		
		arr2.removeIf(x->((x%5)==0));
		System.out.println("\nArray 2 = "+arr2);
		
		Collections.sort(arr1);
		
		
		System.out.println("\nArray 1 = "+arr1);
		//System.out.println("\nArray 2 = "+arr2);
		
		
		
		
		
		
		
		
	}



}
