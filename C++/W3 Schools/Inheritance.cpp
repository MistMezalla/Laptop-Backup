#include <bits/stdc++.h>
using namespace std;

// Base class
class Vehicle2 {
  protected: 
    string brand = "Ford";
    void honk() {
      cout << "Tuut, tuut! \n" ;
    }
};

class Car1: public Vehicle2 {
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

void method1() {
  Car1 myCar;
  myCar.useHonk(); // Correctly accesses the protected honk method
  cout << myCar.getBrand() + " " + myCar.model; // Correctly accesses the protected brand attribute
}

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
    method1();
    cout << endl;
    method2();
    return 0;
}
