import java.util.Scanner;

public class Demo_Lab7_Q2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int choice;
        do {
            System.out.println("Enter the choice: ");
            System.out.println("1 = SBI\n2 = PNB\n3 = BOI\n0 = Exit the program");
            choice = sc.nextInt();
            double bal;
            Bank ac = null;

            switch (choice) {
                case 1:
                    System.out.println("Enter the balance for this a/c: ");
                    bal = sc.nextDouble();
                    ac = new SBI(bal);
                    break;
                case 2:
                    System.out.println("Enter the balance for this a/c: ");
                    bal = sc.nextDouble();
                    ac = new PNB(bal);
                    break;
                case 3:
                    System.out.println("Enter the balance for this a/c: ");
                    bal = sc.nextDouble();
                    ac = new BOI(bal);
                    break;
                case 0:
                    System.out.println("Exiting the program !!!");
                    break;
                default:
                    System.out.println("Wrong Input!!");
            }

            if (ac != null) {
                ac.addInterest();
                ac.display();
            }
        } while (choice != 0);
    }
}

class Bank {
    static double totalBalance;

    void display() {
        System.out.println("The total available balance is: " + totalBalance);
    }
    
    void addInterest() {
        System.out.println("Adding interest to the bank account (default method in Bank class)");
    }
}

class SBI extends Bank {
    double rateOfInterest = 3.5;
    double localBalance;

    SBI(double localBalance) {
        this.localBalance = localBalance;
        totalBalance += localBalance;
    }

    @Override
    void display() {
        System.out.println("Balance in SBI a/c: ");
        System.out.println("Rate of interest: " + rateOfInterest + "\nLocal balance: " + localBalance);
        super.display();
    }

    @Override
    void addInterest() {
        totalBalance -= localBalance;
        localBalance += rateOfInterest * localBalance / 100;
        totalBalance += localBalance;
    }
}

class PNB extends Bank {
    double rateOfInterest = 4;
    double localBalance;

    PNB(double localBalance) {
        this.localBalance = localBalance;
        totalBalance += localBalance;
    }

    @Override
    void display() {
        System.out.println("Balance in PNB a/c: ");
        System.out.println("Rate of interest: " + rateOfInterest + "\nLocal balance: " + localBalance);
        super.display();
    }

    @Override
    void addInterest() {
        totalBalance -= localBalance;
        localBalance += rateOfInterest * localBalance / 100;
        totalBalance += localBalance;
    }
}

class BOI extends Bank {
    double rateOfInterest = 5;
    double localBalance;

    BOI(double localBalance) {
        this.localBalance = localBalance;
        totalBalance += localBalance;
    }

    @Override
    void display() {
        System.out.println("Balance in BOI a/c: ");
        System.out.println("Rate of interest: " + rateOfInterest + "\nLocal balance: " + localBalance);
        super.display();
    }

    @Override
    void addInterest() {
        totalBalance -= localBalance;
        localBalance += rateOfInterest * localBalance / 100;
        totalBalance += localBalance;
    }
}
