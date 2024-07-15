#include <iostream>
#include <string>
using namespace std;
/*
// Base class
class Vehicle1 {
  protected: 
    string brand = "Ford";
    void honk() {
      cout << "Tuut, tuut! \n" ;
    }
};

// Derived class
class Car1: public Vehicle1 {
  public: 
    string model = "Mustang";
};

void method1() {
  Car1 myCar;
  myCar.honk();
  cout << myCar.brand + " " + myCar.model;
}
*/
/*
The error in your code arises from the fact that the Vehicle class is inherited by the Car class using protected 
inheritance. This means that the public and protected members of the Vehicle class become protected members of the Car 
class. As a result, they are not accessible directly from an instance of Car.
*/

// Base class
class Vehicle2 {
  protected: 
    string brand = "Ford";
    void honk() {
      cout << "Tuut, tuut! \n" ;
    }
};

// Derived class
class Car2: protected Vehicle2 {
  public: 
    string model = "Mustang";
    
    // Public member function to access the base class's honk method
    void useHonk() {
      honk();
    }
    
    // Public member function to get the brand
    string getBrand() {
      return brand;
    }
};

void method2() {
  Car2 myCar;
  myCar.useHonk(); // Correctly accesses the protected honk method
  cout << myCar.getBrand() + " " + myCar.model; // Correctly accesses the protected brand attribute
}


int main()
{
    //method1();
    method2();

}

