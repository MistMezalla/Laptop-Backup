package MyPackage;

import java.util.Arrays;

public class Sorting2 {

	public static void main(String[] args) {
		int[] num= {5, 4, 3, 2, 1, 0, -1};
		
		System.out.print("\nBefore sorting the array --> ");
		
		for(int i=0; i<num.length; i++) {
			System.out.print(num[i]+" ");
		}
		
		Arrays.sort(num, 3 ,7);
		
		System.out.print("\nBefore sorting the array --> ");
		
		for(int i=0; i<num.length; i++) {
			System.out.print(num[i]+" ");
		}

		
	}

}
