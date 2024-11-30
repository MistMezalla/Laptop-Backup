package MyPackage;

import java.util.*;

class Student{
	int roll;
	String name;
	
	Student(int r, String n){
		this.roll=r;
		this.name=n;
	}
	
}

public class CompareArrays2 {
	public static void main(String[] args) {
		
		Student s1=new Student(10,"Tom");
		Student s2=new Student(12,"Alex");
		Student s3=new Student(10,"Tom");

		Student[] objArray1 = {s1, s2, s3};
		Student[] objArray2 = {s1, s2, s3};
		Student[] objArray3= {s1, s3};
				
		System.out.println(objArray1==objArray2);
		System.out.println(Arrays.equals(objArray1, objArray2));
		System.out.println(Arrays.equals(objArray1, objArray3));
		
		System.out.println(s1.equals(s3));
		
		
	}

}


//Student[] objArray1= {new Student(10,"Tom"), new Student(12,"Alex"),  new Student(14,"Harry")};
//Student[] objArray2= {new Student(10,"Tom"), new Student(12,"Alex"),  new Student(14,"Harry")};
//Student[] objArray3= {new Student(11, "Tommy"), new Student(12, "Alex"),  new Student(14, "Harry")};
	