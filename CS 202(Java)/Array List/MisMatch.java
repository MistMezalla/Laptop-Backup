package MyPackage;

import java.util.Arrays;

public class MisMatch {

	public static void main(String[] args)
    {
  
        // Get the Arrays
        int intArr[] = { 10, 20, 15, 22, 35 };
  
        // Get the second Arrays
        int intArr1[] = { 10, 20, 15, 22, 35 };
  
        // To compare both arrays
        System.out.println("The element mismatched at index: "
                           + Arrays.mismatch(intArr, intArr1));
    }

}
