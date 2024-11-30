import java.util.Scanner;

public class Demo_Lab9_Q2 {
    public static void main(String [] args){
        int choice;
        Scanner sc = new Scanner(System.in);
        do{
            System.out.println("Enter the choice.");
            System.out.println("1 = To run\n0 = Exit");
            choice = sc.nextInt();
            sc.nextLine();



            if (choice != 0){
                String card_number;
                System.out.println("Enter the card number: ");
                card_number = sc.nextLine();
                String card_holder_name;
                System.out.println("Enter the card holder name: ");
                card_holder_name = sc.nextLine();
                double Bal;
                System.out.println("Enter the balance: ");
                Bal = sc.nextDouble();
                sc.nextLine();


                String upi_id;
                System.out.println("Enter the UPI ID: ");
                upi_id = sc.nextLine();
                String bank_name;
                System.out.println("Enter the bank name");
                bank_name = sc.nextLine();

                double amt;
                System.out.println("Enter the amt to be taken out: ");
                amt = sc.nextDouble();

                CreditCard cc = new CreditCard(card_number,card_holder_name,Bal);
                //mng.calculateBonus();
                if (cc.processPayment(amt)){
                    System.out.println("Successful Card Transaction");
                }
                else{
                    System.out.println("Failed Card Transaction");
                }
                cc.paymentDetails();


               UPI upi = new UPI(upi_id,bank_name,Bal);
                //dev.calculateBonus();
                if (upi.processPayment(amt)){
                    System.out.println("Successful UPI Transaction");
                }
                else{
                    System.out.println("Failed UPI Transaction");
                }
                upi.paymentDetails();
            }
            else{
                System.out.println("Wrong Input!!");
            }
        }while(choice != 0);
    }
}

interface Payment{
    boolean processPayment(double amount);
    void paymentDetails();
}

class CreditCard implements Payment{
    String cardNumber;
    String cardHolderName;
    double balance;

    CreditCard(String card_number,String card_holder_name,double bal){
        cardNumber = card_number;
        cardHolderName = card_holder_name;
        balance = bal;
    }


    public boolean processPayment(double amt){
        if (amt > 0 && amt <= balance){
            this.balance -= amt;
            return true;
        }
        return false;
    }

    public void paymentDetails(){
        System.out.println("Card Number: " + cardNumber + "\nCard Holder Name: " + cardHolderName + "\nBalance: " + balance);
    }
}

class UPI implements Payment{
    String upiId;
    String bankName;
    double balance;

    UPI(String upi_Id, String bank_name, double bal)
    {
        upiId = upi_Id;
        bankName = bank_name;
        balance = bal;
    }

    public boolean processPayment(double amt){

        if (amt > 0 && amt <= balance){
            this.balance -= amt;
            return true;
        }
        return false;
    }

    public void paymentDetails(){

        System.out.println("UPI_Id: " + upiId + "\nBank Name: " + bankName + "\nBalance: " + balance);
    }
}