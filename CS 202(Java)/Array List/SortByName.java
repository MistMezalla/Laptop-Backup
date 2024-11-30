package MyPackage;
import java.util.*;

class Student4{
	int roll;
	String name;
	//String address;
	
	public Student4(int roll, String name)
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

public class SortByName {
	
	public static void sortObjectName(Student4[] Arr) {
		String[] nameArray=new String[Arr.length];
		String[] index=new String[Arr.length];
		int[] index2=new int[Arr.length];
		
		for(int i=0; i<Arr.length; i++ )
		{
			index[i]=Arr[i].name;
		}
		
		for(int i=0; i<Arr.length; i++)
		{
			nameArray[i]=Arr[i].name;
		}
		
		System.out.println("....Original....\n");
		
		for(int i=0; i<Arr.length; i++)
		{
			System.out.println(nameArray[i]);
		}
		
		Arrays.sort(nameArray);
		
		System.out.println("\n....Sort 1....\n");
		
		for(int i=0; i<Arr.length; i++)
		{
			System.out.println(nameArray[i]);
		}
		
		int k=0;
		
		for(int i=0; i<Arr.length; i++)
			for(int j=0; j<Arr.length; j++)
			{
				if(nameArray[i]==index[j]) {
					index2[k++]=j;
					break;
				}
					
			}
		
		System.out.print("\n\nSorted by Name \n");
		
		for(int i=0; i<Arr.length; i++)
		{
			System.out.println(Arr[index2[i]]);
		}
		
		
		
		
	}

	public static void main(String[] args) {
		Student4[] Array= {new Student4(14,"Tom"), new Student4(15,"Alex"),  new Student4(11,"Harry")};
		
		sortObjectName(Array);
	}

}
