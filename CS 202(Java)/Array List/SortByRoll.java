package MyPackage;
import java.util.*;

class Student3{
	int roll;
	String name;
	//String address;
	
	public Student3(int roll, String name)
	{
	 
	     // This keyword refers to current instance itself
	     this.roll = roll;
	     this.name = name;
	     //this.address = address;
	}
	
	public String toString()
    {
		// Returning attributes of Student
        return this.roll + " " + this.name + " ";
    }
	 
}

public class SortByRoll {
	
	public static void sortObject(Student3[] Arr) {
		int[] rollno=new int[Arr.length];
		int[] index=new int[Arr.length];
		int[] index2=new int[Arr.length];
		
		for(int i=0; i<Arr.length; i++ )
		{
			index[i]=Arr[i].roll;
		}
		
		for(int i=0; i<Arr.length; i++)
		{
			rollno[i]=Arr[i].roll;
		}
		
		for(int i=0; i<Arr.length; i++)
		{
			System.out.println(rollno[i]);
		}
		
		Arrays.sort(rollno);
		
		for(int i=0; i<Arr.length; i++)
		{
			System.out.println(rollno[i]);
		}
		
		int k=0;
		
		for(int i=0; i<Arr.length; i++)
			for(int j=0; j<Arr.length; j++)
			{
				if(rollno[i]==index[j]) {
					index2[k++]=j;
					break;
				}
					
			}
		
		System.out.print("\n\nSorted by Roll \n");
		
		for(int i=0; i<Arr.length; i++)
		{
			System.out.println(Arr[index2[i]]);
		}
		
		
		
		
	}

	public static void main(String[] args) {
		Student3[] Array= {new Student3(14,"Tom"), new Student3(17,"Alex"),  new Student3(11,"Harry")};

		sortObject(Array);
	
	
	
	}

}
