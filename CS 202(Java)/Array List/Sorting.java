package MyPackage;

import java.util.Arrays;

public class Sorting {

	public static void main(String[] args) {
		int[] numbers= {5, 2, 3, -1, 0, 4, 1};
		
		System.out.print("\nBefore sorting integer array");
		
		for(int i=0; i<numbers.length; i++) {
			System.out.print(numbers[i]+" ");
		}

		Arrays.sort(numbers);
		
		System.out.print("\nAfter sorting integer array");
		
		for(int i=0; i<numbers.length; i++) {
			System.out.print(numbers[i]+" ");
		}
	
		char[] characters= {'a', 'z', 'b', 'w', 'c', 'A', 'D', 'Z', 'C'};
		//Try making it int[]. What does it print?
		
		System.out.print("\nBefore sorting integer array -->");
		
		for(int i=0; i<characters.length; i++) {
			System.out.print(characters[i]+" ");
		}
	
		Arrays.sort(characters);
		
		System.out.print("\nAfter sorting integer array -->");
		
		for(int i=0; i<characters.length; i++) {
			System.out.print(characters[i]+" ");
		}
		
	}

}
