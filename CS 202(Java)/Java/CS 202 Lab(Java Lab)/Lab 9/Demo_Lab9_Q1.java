import java.util.*;
public class Demo_Lab9_Q1 {
    public static void main(String [] args){
        int choice;
        Scanner sc = new Scanner(System.in);
        do{
            System.out.println("Enter the choice.");
            System.out.println("1 = Manager\n2 = Developer\n3 = Exit");
            choice = sc.nextInt();
            sc.nextLine();



            if (choice == 1){
                String Name;
                System.out.println("Enter the name: ");
                Name = sc.nextLine();
                float Salary;
                System.out.println("Enter the salary");
                Salary = sc.nextFloat();

                Manager mng = new Manager(Name,Salary);
                //mng.calculateBonus();
                System.out.println(mng);
            }
            else if (choice == 2){
                String Name;
                System.out.println("Enter the name: ");
                Name = sc.nextLine();
                float Salary;
                System.out.println("Enter the salary");
                Salary = sc.nextFloat();

                Developer dev = new Developer(Name,Salary);
                //dev.calculateBonus();
                System.out.println(dev);
            }
            else if (choice == 3){
                System.out.println("Exiting the program !!");
                break;
            }
            else{
                System.out.println("Wrong Input!!");
            }
        }while(choice != 0);
    }
}

abstract class Employee{
    String name;
    float salary;

    abstract double calculateBonus();

    public String toString(){
        return "Name: " + name + "\nSalary: " + salary;
    }

    Employee(String name,float salary){
        this.name = name;
        this.salary = salary;
    }
}

class Manager extends Employee{
    Manager(String name,float salary){
        super(name,salary);
        this.salary = (float)calculateBonus();
    }

    double calculateBonus(){
        return this.salary * 1.2;
    }

    public String toString(){
        return super.toString();
    }

}

class Developer extends Employee{
    Developer(String name,float salary){
        super(name,salary);
        this.salary = (float)calculateBonus();
    }

    double calculateBonus(){
        return this.salary * 1.1;
    }

    public String toString(){
        return super.toString();
    }

}


