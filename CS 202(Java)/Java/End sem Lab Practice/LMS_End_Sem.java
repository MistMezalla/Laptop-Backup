import java.util.*;

abstract class User {
    int userId;
    String name;
    String borrowedBook;
    String bookType;
    int issueMonthNum;

    public User(int userId, String name) {
        this.userId = userId;
        this.name = name;
        this.borrowedBook = null;
        this.bookType = null;
        this.issueMonthNum = 0;
    }

    abstract int calculateFine(int returnMonthNum);

    public void issueBook(String title, String type, int issueMonthNum, ArrayList<Book> books) {
        for (Book book : books) {
            if (book.title.equals(title) && book.availableCopies > 0) {
                this.borrowedBook = title;
                this.bookType = type;
                this.issueMonthNum = issueMonthNum;
                book.availableCopies--;
                System.out.println("Book issued: " + title);
                return;
            }
        }
        System.out.println("Book not available for issue.");
    }

    public void returnBook(String title, int returnMonthNum, ArrayList<Book> books) {
        if (this.borrowedBook != null && this.borrowedBook.equals(title)) {
            for (Book book : books) {
                if (book.title.equals(title)) {
                    book.availableCopies++;
                    System.out.println("Book returned: " + title);
                    break;
                }
            }
            int fine = calculateFine(returnMonthNum);
            System.out.println("Fine for return: " + fine);
            this.borrowedBook = null;
            this.bookType = null;
            this.issueMonthNum = 0;
        } else {
            System.out.println("No book to return.");
        }
    }
}

class StudentUser extends User {
    String studentRoll;

    public StudentUser(int userId, String name, String studentRoll) throws InvalidUserIDException {
        super(userId, name);
        if (userId % 2 != 0) throw new InvalidUserIDException("Invalid UserID for Student");
        this.studentRoll = studentRoll;
    }

    @Override
    int calculateFine(int returnMonthNum) {
        int gap = returnMonthNum - this.issueMonthNum;
        if (gap > 3) {
            return 2000 * gap;
        }
        return 0;
    }
}

class FacultyUser extends User {
    String empId;

    public FacultyUser(int userId, String name, String empId) throws InvalidUserIDException {
        super(userId, name);
        if (userId % 2 == 0) throw new InvalidUserIDException("Invalid UserID for Faculty");
        this.empId = empId;
    }

    @Override
    int calculateFine(int returnMonthNum) {
        int gap = returnMonthNum - this.issueMonthNum;
        if (gap > 5) {
            return 5000 * gap;
        }
        return 0;
    }
}

class Book {
    String title;
    String type;
    int availableCopies;

    public Book(String title, String type) {
        this.title = title;
        this.type = type;
        this.availableCopies = 5;
    }
}

class InvalidUserIDException extends Exception {
    public InvalidUserIDException(String message) {
        super(message);
    }
}

public class LMS_End_Sem {
    ArrayList<User> users;
    ArrayList<Book> books;

    public LMS_End_Sem() {
        users = new ArrayList<>();
        books = new ArrayList<>();
    }

    public void addBook(String title, String type) {
        books.add(new Book(title, type));
    }

    public void addUser(User user) {
        users.add(user);
    }

    public void displayUsers() {
        for (User user : users) {
            System.out.println("User ID: " + user.userId + ", Name: " + user.name +
                    ", Borrowed Book: " + user.borrowedBook + ", Book Type: " + user.bookType +
                    ", Issue Month: " + user.issueMonthNum);
        }
    }

    public void displayBooks() {
        for (Book book : books) {
            System.out.println("Title: " + book.title + ", Type: " + book.type +
                    ", Available Copies: " + book.availableCopies);
        }
    }

    public static void main(String[] args) {
        LMS_End_Sem LMS_End_Sem_End_Sem = new LMS_End_Sem();

        // Initialize books
        LMS_End_Sem_End_Sem.addBook("Computer Organization", "Text");
        LMS_End_Sem_End_Sem.addBook("Gemba Kaizen", "Non-text");
        LMS_End_Sem_End_Sem.addBook("Let us C", "Text");
        LMS_End_Sem_End_Sem.addBook("Operating Systems", "Text");
        LMS_End_Sem_End_Sem.addBook("The Alchemist", "Non-text");

        // Initialize users
        try {
            LMS_End_Sem_End_Sem.addUser(new StudentUser(2, "Alice", "S101"));
            LMS_End_Sem_End_Sem.addUser(new StudentUser(4, "Bob", "S102"));
            LMS_End_Sem_End_Sem.addUser(new FacultyUser(1, "Dr. Smith", "F101"));
            LMS_End_Sem_End_Sem.addUser(new FacultyUser(3, "Prof. Johnson", "F102"));
        } catch (InvalidUserIDException e) {
            System.out.println(e.getMessage());
        }

        // Display all users and books
        LMS_End_Sem_End_Sem.displayUsers();
        LMS_End_Sem_End_Sem.displayBooks();

        // Issue a book
        LMS_End_Sem_End_Sem.users.get(0).issueBook("Computer Organization", "Text", 1, LMS_End_Sem_End_Sem.books);
        LMS_End_Sem_End_Sem.displayUsers();
        LMS_End_Sem_End_Sem.displayBooks();

        // Return a book
        LMS_End_Sem_End_Sem.users.get(0).returnBook("Computer Organization", 5, LMS_End_Sem_End_Sem.books);
        LMS_End_Sem_End_Sem.displayUsers();
        LMS_End_Sem_End_Sem.displayBooks();
    }
}
