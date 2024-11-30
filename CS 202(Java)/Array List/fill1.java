package MyPackage;

import java.util.Arrays;

public class fill1 {

	public static void main(String[] args) {
		int[] numbers= {5, 4, 3, 2, 1, 0, -1};
		
		System.out.print("\nBefore filling integer array ");
		
		for(int i=0; i<numbers.length; i++) {
			System.out.print(numbers[i]+" ");
		}

		//Arrays.fill(numbers, 10);
		Arrays.fill (numbers, 3, 6, 91);	//fills from start to end-1
		System.out.print("\nAfter filling integer array ");
		
		for(int i=0; i<numbers.length; i++) {
			System.out.print(numbers[i]+" ");
		}
		
	}

}
