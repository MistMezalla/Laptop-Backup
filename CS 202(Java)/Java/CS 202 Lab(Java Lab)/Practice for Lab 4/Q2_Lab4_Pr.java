import java.util.Scanner;

class Book {
    private int bookId;
    private String bookTitle;
    private int yearOfPublication;
    private String authorName;
    private String publisherName;
    private int numberOfAvailableCopies;
    private int totalCopies;


    public Book() {
    }

    public Book(int totalCopies) {
        this.totalCopies = totalCopies;
        this.numberOfAvailableCopies = totalCopies;
    }

    public void setDetails(int id, String title, int year, String author, String publisher, int count) {
        this.bookId = id;
        this.bookTitle = title;
        this.yearOfPublication = year;
        this.authorName = author;
        this.publisherName = publisher;
        this.totalCopies = count;
        this.numberOfAvailableCopies = count;
    }

    public void getDetails(int id) {
        if (this.bookId == id) {
            System.out.println("Book ID: " + bookId);
            System.out.println("Title: " + bookTitle);
            System.out.println("Year of Publication: " + yearOfPublication);
            System.out.println("Author: " + authorName);
            System.out.println("Publisher: " + publisherName);
            System.out.println("Total Copies: " + totalCopies);
            System.out.println("Available Copies: " + numberOfAvailableCopies);
        }
    }

    public void issue(int id) {
        if (this.bookId == id) {
            if (numberOfAvailableCopies > 0) {
                numberOfAvailableCopies--;
                System.out.println("Book issued successfully. Available copies: " + numberOfAvailableCopies);
            } else {
                System.out.println("No copies available to issue.");
            }
        }
    }

    public void returnBook(int id) {
        if (this.bookId == id) {
            if (numberOfAvailableCopies < totalCopies) {
                numberOfAvailableCopies++;
                System.out.println("Book returned successfully. Available copies: " + numberOfAvailableCopies);
            } else {
                System.out.println("All copies are already available. Cannot return more.");
            }
        }
    }
}

public class Q2_Lab4_Pr {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Create an array of 5 Book objects
        Book[] bookArray = new Book[5];
        for (int i = 0; i < 5; i++) {
            bookArray[i] = new Book();
        }

        while (true) {
            System.out.println("\nLibrary Management System");
            System.out.println("1. Set Details");
            System.out.println("2. Get Details");
            System.out.println("3. Issue");
            System.out.println("4. Return");
            System.out.println("5. Exit");
            System.out.print("Choose an option: ");
            int choice = sc.nextInt();

            if (choice == 5) {
                System.out.println("Exiting...");
                break;
            }

            System.out.print("Enter Book ID (1-5): ");
            int bookId = sc.nextInt();

            if (bookId < 1 || bookId > 5) {
                System.out.println("Invalid Book ID. Please choose between 1 and 5.");
                continue;
            }

            Book selectedBook = bookArray[bookId - 1];

            switch (choice) {
                case 1:
                    System.out.print("Enter Book Title: ");
                    sc.nextLine();
                    String title = sc.nextLine();
                    System.out.print("Enter Year of Publication: ");
                    int year = sc.nextInt();
                    System.out.print("Enter Author Name: ");
                    sc.nextLine();
                    String author = sc.nextLine();
                    System.out.print("Enter Publisher Name: ");
                    String publisher = sc.nextLine();
                    System.out.print("Enter Total Copies: ");
                    int count = sc.nextInt();
                    selectedBook.setDetails(bookId, title, year, author, publisher, count);
                    break;

                case 2:
                    selectedBook.getDetails(bookId);
                    break;

                case 3:
                    selectedBook.issue(bookId);
                    break;

                case 4:
                    selectedBook.returnBook(bookId);
                    break;

                default:
                    System.out.println("Invalid choice! Please choose a valid option.");
            }
        }

        sc.close();
    }
}

