package MyPackage;
import java.util.Arrays;
  
public class fill2D
{
    public static void main(String[] args)
    {
        int [][]ar = new int [3][4];
  
        for (int i=0; i<ar.length; i++)
            Arrays.fill(ar[i], 1, 3, i+2);
     
        for(int i=0; i<ar.length;i++)
        {	System.out.print("\n");
        	for(int j=0; j<ar[i].length; j++)
        		System.out.print(ar[i][j]+" ");
        }
    }
}