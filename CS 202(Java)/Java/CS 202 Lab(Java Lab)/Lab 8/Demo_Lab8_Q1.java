import java.util.*;
public class Demo_Lab8_Q1{
	public static void main(String [] args){
		Scanner sc = new Scanner(System.in);
		
		int choice;
		
		Shape shp = null;
		do{
			System.out.println("Enter the choice" );
			System.out.println("1 = Circle\n2 = Rectangle\n0 = Exit");
			choice = sc.nextInt();
			switch(choice){
				case 1:
					System.out.println("Enter the radius of the circle: ");
					int rad = sc.nextInt();
					shp = new Circle(rad);
					break;
				case 2:
					System.out.println("Enter the length of the circle: ");
					int length = sc.nextInt();
					System.out.println("Enter the breadth of the circle: ");
					int breadth = sc.nextInt();
					shp = new Rectangle(length,breadth);
				
					break;
				case 0:
					System.out.println("Exiting the program !!!");
					break;
				default:
					System.out.println("Wrong Input !!");
					break;
			}

			if (shp != null)
			{
				System.out.println(shp);
				System.out.println("Area: " + shp.getArea());
				System.out.println("Perimeter:" + shp.getPerimeter());
			}
		}while(choice != 0);
	}
}

abstract class Shape{
	String name;
	int noSides;
	
	abstract double getArea();

	abstract double getPerimeter();

	public String toString(){
		return "name: " + name + "\nNumber of Sides: " + noSides;
	}
}

class Circle extends Shape{
	int radius;
	
	Circle(int r){
		radius = r;
		super.name = "Circle";
		super.noSides = 0;
	}

	@Override
	double getArea(){
		return 3.14 * radius * radius;
	}

	@Override
	double getPerimeter(){
		return 2 * 3.14 * radius;
	}
}

class Rectangle extends Shape{
	int length;
	int breadth;

	Rectangle(int l,int b){
		length = l;
		breadth = b;
		super.name = "Rectange";
		super.noSides = 4;
	}
	
	@Override
	double getArea(){
		return length * breadth;
	}

	@Override
	double getPerimeter(){
		return 2 * (length + breadth);
	}
}
	
