package MyPackage;

import java.util.Arrays;

public class CompareArrays {

	public static void main(String[] args) {
		int [] numbers1= {5, 4, 3, 2, 1, 0, -1};
		int [] numbers2= {5, 4, 3, 2, 1, 0, -1};
		int [] numbers3= {1, 2, 3, 7, 7, 8, 1};
		
		System.out.println(numbers1==numbers2);
		System.out.println(Arrays.equals(numbers1, numbers2));
		System.out.println(Arrays.equals(numbers1, numbers3));
		
		
		
	}

}
