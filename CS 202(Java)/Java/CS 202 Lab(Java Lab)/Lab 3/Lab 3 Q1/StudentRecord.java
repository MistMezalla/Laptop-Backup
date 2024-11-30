public class StudentRecord{
	private int rollNo;
	private String name;
	private String department;

	StudentRecord(){
		this.rollNo = -1;
		this.name = "000";
		this.department = "000";
	}

	StudentRecord(int rollNo){
		this.rollNo = rollNo;
		this.name = "000";
		this.department = "000";
	}

	StudentRecord(int rollNo, String name){
		this.rollNo = rollNo;
		this.name = name;
		this.department = "000";
	}

	StudentRecord(int rollNo, String name, String department){
		this.rollNo = rollNo;
		this.name = name;
		this.department = department;
	}

	public void displayRecord(){
		System.out.printf("Roll number: %d, Name: %s, Dep: %s\n", rollNo,name,department); 
	}

}
	