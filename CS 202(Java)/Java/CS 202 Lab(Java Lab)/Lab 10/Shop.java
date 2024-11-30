import java.util.*;
public class Shop {
    public static void main(String [] args) {
        Items[] items = {
                new Items(1, "TV", 10000, 3, 2),
                new Items(2, "Mouse", 1000, 7, 3),
                new Items(3, "HeadPhone", 2000, 1, 6),
                new Items(4, "Mobile", 5000, 5, 1),
        };

        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the name of user: ");
        String user_name = sc.nextLine();
        System.out.println("Enter the budget of the user: ");
        double user_budget = sc.nextDouble();

        User user = new User(user_name, user_budget);

        while (true) {
            System.out.println("Enter your choice: ");
            System.out.println("1. Display Items\n2. Buy Items\n3. Exit");
            int choice = sc.nextInt();


            if (choice == 1) {
                for (Items item : items) {
                    System.out.println(item);
                }
            }

            else if(choice == 2) {
                System.out.println("Enter the item code to be purchased: ");
                int item_code = sc.nextInt();
                try {
                    Items item = null;
                    for (Items i : items) {
                        if (i.itemCode == item_code) {
                            item = i;
                            break;
                        }
                    }

                    if (item == null) {
                        throw new ItemNotFoundException("Item not found. Enter the value from 1 to 4.");
                    }

                    System.out.println("Enter the number of qty to be bought: ");
                    int qty = sc.nextInt();

                    if (qty > item.stockRemaining) {
                        throw new OutOfStockException("Item out of Stock currently.\n" + "You can purchase only: " + item.stockRemaining);
                    }

                    if (qty > item.itemLimit) {
                        throw new ItemLimitException("Item limit exceeded\n" + "You can purchase only: " + item.itemLimit);
                    }


                    double tot_cost = qty * item.unitPrice;
                    if (tot_cost > user.budget) {
                        throw new OverBudgetException("Budget Exceeded.\n" + "Current Bill: " + tot_cost + "\nYour Budget: " + user.budget);
                    }

                    item.stockRemaining -= qty;
                    user.budget -= tot_cost;
                    System.out.println("Purchase made successfully!!" + "Remaining budget: " + user.budget);
                } catch (ItemLimitException | ItemNotFoundException | OutOfStockException | OverBudgetException e) {
                    System.out.println("ERROR:" + e.getMessage());
                }
                break;
            }

            else if(choice  == 3){
                System.out.println("Thank You");
                break;
            }

            else{
                System.out.println("Invalid choice!!!Enter the choice bet 1 - 3.");
            }
        }
    }
}

class ItemNotFoundException extends Exception{
    public ItemNotFoundException(String message) {
        super(message);
    }
}

class OverBudgetException extends Exception {
    public OverBudgetException(String message) {
        super(message);
    }
}

class ItemLimitException extends Exception {
    public ItemLimitException(String message) {
        super(message);
    }
}

class OutOfStockException extends Exception {
    public OutOfStockException(String message) {
        super(message);
    }
}


