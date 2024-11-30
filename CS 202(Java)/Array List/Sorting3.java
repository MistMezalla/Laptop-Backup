package MyPackage;

import java.util.Arrays;

public class Sorting3 {

	public static void main(String[] args) {
		String[] str= {"hij", "abc", "efg"};
		
		System.out.print("\nBefore sorting the array --> ");
		
		for(int i=0; i<str.length; i++) {
			System.out.print(str[i]+" ");
		}

		//Lexicographic sorting of the string array
		Arrays.sort(str);	
		
		System.out.print("\nAfter sorting the array --> ");
		
		for(int i=0; i<str.length; i++) {
			System.out.print(str[i]+" ");
		}

		
		
	}

}
