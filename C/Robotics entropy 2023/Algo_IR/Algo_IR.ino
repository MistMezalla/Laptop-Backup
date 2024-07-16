// Define the pins for your two IR sensors
#define LEFT_IR_SENSOR A0
#define RIGHT_IR_SENSOR A1

// Define motor control pins
#define LEFT_MOTOR 9
#define RIGHT_MOTOR 10

void setup() {
  // Initialize serial communication for debugging
  Serial.begin(9600);

  // Configure IR sensor pins as inputs
  pinMode(LEFT_IR_SENSOR, INPUT);
  pinMode(RIGHT_IR_SENSOR, INPUT);

  // Configure motor control pins as outputs
  pinMode(LEFT_MOTOR, OUTPUT);
  pinMode(RIGHT_MOTOR, OUTPUT);
}

void loop() {
  // Read sensor values
  int leftValue = digitalRead(LEFT_IR_SENSOR);
  int rightValue = digitalRead(RIGHT_IR_SENSOR);

  // Debugging: Print sensor values
  Serial.print("Left IR: ");
  Serial.print(leftValue);
  Serial.print("  Right IR: ");
  Serial.println(rightValue);

  // Implement the wall-following algorithm
  if (leftValue == LOW && rightValue == LOW) {
    // Both sensors detect no wall: Move forward
    moveForward();
  } else if (leftValue == LOW && rightValue == HIGH) {
    // Left sensor detects no wall, right sensor detects a wall: Turn left
    turnLeft();
  } else if (leftValue == HIGH && rightValue == LOW) {
    // Left sensor detects a wall, right sensor detects no wall: Turn right
    turnRight();
  } else {
    // Both sensors detect walls: Possible options to handle intersections
    // You may need to add more logic for intersection handling.
  }
}

void moveForward() {
  // Implement your motor control code to move the robot forward
  digitalWrite(LEFT_MOTOR, HIGH);
  digitalWrite(RIGHT_MOTOR, HIGH);
}

void turnLeft() {
  // Implement your motor control code to turn the robot left
  digitalWrite(LEFT_MOTOR, LOW);
  digitalWrite(RIGHT_MOTOR, HIGH);
}

void turnRight() {
  // Implement your motor control code to turn the robot right
  digitalWrite(LEFT_MOTOR, HIGH);
  digitalWrite(RIGHT_MOTOR, LOW);
}

