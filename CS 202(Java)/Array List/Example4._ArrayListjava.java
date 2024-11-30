package MyPackage;

import java.util.*;

class Student{
	int roll;
	String name;
	int age;
	
	Student(int roll, String name, int age){
		this.roll=roll;
		this.name=name;
		this.age=age;		
	}
		
	public String toString() {
		return ("Roll = "+roll+" Name = "+name+ "Age = "+age);
		
	}
}



public class Example4 {

	public static void main(String[] args) {
		Student s1=new Student(101, "John", 21);
		Student s2=new Student(121, "Ravi", 31);
		Student s3=new Student(111, "Joseph", 21);
		
		ArrayList <Student> list_s=new ArrayList<>();
		
		list_s.add(s1);
		list_s.add(s2);
		list_s.add(s3);
		
		System.out.println(list_s);
		
		
		for(Student s:list_s) {
			System.out.println(s);
		}
		
		
		
		

	}

}
