package MyPackage;

import java.util.Arrays;

//Showing the example of Binary Search algorithm
//Return value : return index if found
//else return -(insertionIndex+1)

public class Searching {

	public static void main(String[] args) {
		int[] array= {5, 4, 3, 2, 1, 0, -1};
		Arrays.sort(array);	//-1, 0, 1, 2, 3, 4, 5
		
		System.out.println(Arrays.binarySearch(array, 4));
		System.out.println(Arrays.binarySearch(array, -5));
		
		System.out.println("\nLets check string arrays\n");
		String[] string = {"a", "b", "c"};
		System.out.println(Arrays.binarySearch(string, "a"));


	}

}
