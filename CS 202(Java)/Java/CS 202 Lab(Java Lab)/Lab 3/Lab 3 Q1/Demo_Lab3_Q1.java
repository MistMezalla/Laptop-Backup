public class Demo_Lab3_Q1 {
	public static void main(String [] args)
	{
		StudentRecord obj1 = new StudentRecord();	
		StudentRecord obj2 = new StudentRecord(27);	
		StudentRecord obj3 = new StudentRecord(31,"Rahul");	
		StudentRecord obj4 = new StudentRecord(66,"Swapnil","CSE");	

		obj1.displayRecord();
		obj2.displayRecord();
		obj3.displayRecord();
		obj4.displayRecord();
	}
}