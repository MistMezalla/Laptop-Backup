public class Example {
    private String myString;

    public Example() {
        // Default constructor
    }

    public void printString() {
        System.out.println(myString);
    }

    public static void main(String[] args) {
        Example example = new Example();
        example.printString();  // This will print "null"
    }
}
