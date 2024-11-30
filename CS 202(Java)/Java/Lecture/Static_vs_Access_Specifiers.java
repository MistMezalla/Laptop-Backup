// 1st variant
//public class Static_vs_Access_Specifiers {
//    private static int staticVar = 10; // Static variable
//    private int instVar = 20;          // Instance variable
//
//    // Static nested class
//    public static class StaticNestedClass {
//        void display() {
//            System.out.println("Static variable: " + staticVar);  // Accessible
//            // System.out.println("Instance variable: " + instVar); // Error: Can't access
//        }
//    }
//
//    // Private static nested class
//    private static class PrivateNestedClass {
//        void display() {
//            System.out.println("This is a private nested class.");
//        }
//    }
//}

// 2nd variant
public class Static_vs_Access_Specifiers {
    private static int staticVar = 10; // Static variable
    private int instVar = 20;          // Instance variable

    // Static nested class
    class StaticNestedClass {
//        // Accept instance of Static_vs_Access_Specifiers
//        private Static_vs_Access_Specifiers outer;
//
//        StaticNestedClass(Static_vs_Access_Specifiers outer) {
//            this.outer = outer;
//        }

        void display() {
            System.out.println("Static variable: " + staticVar);  // Accessible
            System.out.println("Instance variable: " + instVar); // Now accessible
        }
    }
}
