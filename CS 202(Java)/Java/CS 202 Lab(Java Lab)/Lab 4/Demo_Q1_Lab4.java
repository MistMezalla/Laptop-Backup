import java.util.*;

public class Demo_Q1_Lab4{
	public static void main(String[] args)
	{
		Scanner sc = new Scanner(System.in);

		System.out.println("Enter the Car ID: ");
		int carId = sc.nextInt();
		sc.nextLine();

		System.out.println("Enter the Car Type: ");
		String car_type = sc.nextLine();
		CarRental cr = new CarRental();
		cr.constructCar(carId,car_type);
		cr.computeRent();
		cr.showCar();
	}
}

class CarRental{
	private int carID;
	private String carType;
	private float rent;
	
	public void constructCar (int carID, String carType)
	{
		this.carID = carID;
		this.carType = carType;
	}
	
	public void computeRent()
	{
		if(this.carType.equals("Small Car"))
			this.rent = 1000;
		else if (this.carType.equals("Van"))
			this.rent = 800;
		else if (this.carType.equals("SUV"))
			this.rent = 2500;
	}

	public void showCar()
	{
		System.out.println("CarId :" + this.carID);
		System.out.println("Car Type :" + this.carType);
		System.out.println("Rent :" + this.rent);
	}
}
		

	
		