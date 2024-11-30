public class StaticPublic {  // Class name corrected (no static keyword in the class name)
    static int max_elem(int a, int b) {
        return a >= b ? a : b;
    }

    public int min_elem(int a, int b) {
        return a <= b ? a : b;
    }

    public static void main(String[] args) {
        System.out.println(max_elem(5, 7));

        StaticPublic my_obj = new StaticPublic();  // Object created to call the non-static method
        System.out.println(my_obj.min_elem(5, 7));

        operations obj = new operations(5, 7);  // Corrected the object creation and method call
        System.out.println(obj.add(5, 7));
        System.out.println(operations.sub(5, 7));// Calling the static method using the class name

        JavaBasics Obj = new JavaBasics();
        Obj.Print();
    }
}

class operations {
    public int add(int a, int b) {
        return a + b;
    }

    static int sub(int a, int b) {
        return a - b;
    }

    public operations(int a, int b) {
//        add(a, b);
//        sub(a, b);
    }
}
