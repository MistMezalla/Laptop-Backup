import java.util.ArrayList;
import java.util.Scanner;

public class HMS {
    private ArrayList<Person> persons;
    private ArrayList<Medicine> medicines;

    public HMS() {
        persons = new ArrayList<>();
        medicines = new ArrayList<>();
        persons.addAll(personData());
        medicines.addAll(medicineData());
    }

    public void addDoctor(int personId, String name, String specialization, int patientsAssigned) {
        persons.add(new Doctor(personId, name, specialization, patientsAssigned));
    }

    public void addPatient(int personId, String name, String ailmentType, boolean isInsured, String medicineName, int qty) {
        persons.add(new Patient(personId, name, ailmentType, isInsured, medicineName, qty));
    }

    public void displayPersons() {
        for (Person person : persons) {
            System.out.println("ID: " + person.personId + "\tName: " + person.name);
            if (person instanceof Patient) {
                Patient pat = (Patient) person;
                System.out.println("Ailment Type: " + pat.ailmentType + "\tMedicine: " + pat.medicineName + "\tQty: " +
                        pat.quantity + "\tInsured: " + pat.isInsured);
            } else if (person instanceof Doctor) {
                Doctor doc = (Doctor) person;
                System.out.println("Specialisation: " + doc.specialization + "\tPatients Assigned: " + doc.patientsAssigned);
            }
        }
    }

    public void displayMedicines() {
        for (Medicine med : medicines) {
            System.out.println("Name: " + med.medicineName + "\tCategory: " + med.category + "\tStock Qty: " + med.stockQuantity);
        }
    }

    private ArrayList<Person> personData() {
        ArrayList<Person> data = new ArrayList<>();
        data.add(new Patient(2, "John Doe", "Fever", true, "Paracetamol", 2));
        data.add(new Patient(4, "Alice Smith", "Infection", false, "Amoxicillin", 1));
        data.add(new Patient(6, "Bob Johnson", "Diabetes", true, "Metformin", 1));
        data.add(new Patient(8, "Carol White", "Arthritis", false, "Ibuprofen", 4));
        data.add(new Patient(10, "Eve Brown", "Hypertension", true, "Aspirin", 1));
        data.add(new Doctor(1, "Dr. Brown", "Cardiology", 4));
        data.add(new Doctor(3, "Dr. Grey", "Dermatology", 1));
        data.add(new Doctor(5, "Dr. Black", "Orthopedist", 6));
        data.add(new Doctor(7, "Dr. Green", "Neurology", 2));
        data.add(new Doctor(9, "Dr. White", "General Medicine", 3));
        return data;
    }

    private ArrayList<Medicine> medicineData() {
        ArrayList<Medicine> data = new ArrayList<>();
        data.add(new Medicine("Paracetamol", "Analgesic", 10));
        data.add(new Medicine("Amoxicillin", "Antibiotic", 5));
        data.add(new Medicine("Aspirin", "Analgesic", 0));
        data.add(new Medicine("Ibuprofen", "Anti-inflammatory", 8));
        data.add(new Medicine("Metformin", "Anti-diabetic", 12));
        return data;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        HMS hms = new HMS();

        hms.displayPersons();
        hms.displayMedicines();

        System.out.println("Enter 0 for Patient and 1 for Doctor:");
        int choice = sc.nextInt();
        sc.nextLine();
        if (choice == 0) {
            System.out.println("Enter Patient details: ID, Name, Ailment, Insured (true/false), Medicine, Qty");
            int personId = sc.nextInt();
            sc.nextLine();
            String name = sc.nextLine();
            String ailmentType = sc.nextLine();
            boolean isInsured = sc.nextBoolean();
            sc.nextLine();
            String medicineName = sc.nextLine();
            int qty = sc.nextInt();
            hms.addPatient(personId, name, ailmentType, isInsured, medicineName, qty);
        } else if (choice == 1) {
            System.out.println("Enter Doctor details: ID, Name, Specialization, Patients Assigned");
            int personId = sc.nextInt();
            sc.nextLine();
            String name = sc.nextLine();
            String specialization = sc.nextLine();
            int patientsAssigned = sc.nextInt();
            hms.addDoctor(personId, name, specialization, patientsAssigned);
        }

        System.out.println("Enter days admitted:");
        int daysAdmitted = sc.nextInt();
        for (Person person : hms.persons) {
            if (person instanceof Patient) {
                ((Patient) person).calculateCharges(daysAdmitted);
            }
        }

        System.out.println("Enter days worked:");
        int daysWorked = sc.nextInt();
        for (Person person : hms.persons) {
            if (person instanceof Doctor) {
                ((Doctor) person).calculateSalary(daysWorked);
            }
        }
    }
}

class OutOfStockException extends Exception {
    public OutOfStockException(String msg) {
        super(msg);
    }
}

abstract class Person {
    int personId;
    String name;

    Person(int personId, String name) {
        this.personId = personId;
        this.name = name;
    }
}

class Patient extends Person {
    String ailmentType;
    boolean isInsured;
    String medicineName;
    int quantity;

    Patient(int personId, String name, String ailmentType, boolean isInsured, String medicineName, int qty) {
        super(personId, name);
        this.ailmentType = ailmentType;
        this.isInsured = isInsured;
        this.quantity = qty;
        this.medicineName = medicineName;
    }

    void prescribeMedicine(String medicineName, int quantity, ArrayList<Medicine> medicines) throws OutOfStockException {
        for (Medicine med : medicines) {
            if (med.medicineName.equals(medicineName)) {
                if (quantity > med.stockQuantity)
                    throw new OutOfStockException("Requested quantity of medicines is unavailable!");
                med.stockQuantity -= quantity;
            }
        }
    }

    void calculateCharges(int daysAdmitted) {
        int baseCharges = isInsured ? 450 * daysAdmitted : 500 * daysAdmitted;
        System.out.println("Total charges: " + baseCharges);
    }
}

class Doctor extends Person {
    String specialization;
    int patientsAssigned;

    Doctor(int personId, String name, String specialization, int patientsAssigned) {
        super(personId, name);
        this.specialization = specialization;
        this.patientsAssigned = patientsAssigned;
    }

    void calculateSalary(int daysWorked) {
        int baseSalary = 1000 * daysWorked + (patientsAssigned > 3 ? 2000 : 0);
        System.out.println("Total salary: " + baseSalary);
    }
}

class Medicine {
    String medicineName;
    String category;
    int stockQuantity;

    Medicine(String medicineName, String category, int stockQuantity) {
        this.medicineName = medicineName;
        this.category = category;
        this.stockQuantity = stockQuantity;
    }
}
