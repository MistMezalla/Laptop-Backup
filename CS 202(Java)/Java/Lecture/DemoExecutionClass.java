public class DemoExecutionClass {
    public static void main(String [] args){
        ConstructorsUsage res = new ConstructorsUsage(10,5);
        System.out.println("IIITG" + res.l + res.b);

//        // For 1st variant
//        // Creating an instance of the static nested class
//        Static_vs_Access_Specifiers.StaticNestedClass nested = new Static_vs_Access_Specifiers.StaticNestedClass();
//        nested.display();
        
        // For 2nd Variant
        //Create an instance of Static_vs_Access_Specifiers
        Static_vs_Access_Specifiers outer = new Static_vs_Access_Specifiers();

        // Create an instance of the static nested class, passing the outer instance
//        Static_vs_Access_Specifiers.StaticNestedClass nested = new Static_vs_Access_Specifiers.StaticNestedClass(outer);
//        nested.display();
        
        // When subclass(Nested class) is not static
        Static_vs_Access_Specifiers.StaticNestedClass nested =  outer.new StaticNestedClass();
        nested.display();

        This_return result = new This_return(100,200);
        This_return result_inst;
        result_inst = result.get_this();
        System.out.println(result_inst);
        System.out.println(result_inst.l + " " + result_inst.b);
        System.out.println(result.l+ " " + result.b);
    }
}
