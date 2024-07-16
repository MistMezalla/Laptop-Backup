#include <AFMotor.h>

AF_DCMotor motor1(1); // Motor driver for motor 1
AF_DCMotor motor2(2); // Motor driver for motor 2

// Define IR sensor pins
int leftIR = A0;    // Left IR sensor pin
int centerIR = A1;  // Center IR sensor pin
int rightIR = A2;   // Right IR sensor pin

// Maze dimensions
int mazeWidth = 8;  // Adjust to match your maze
int mazeHeight = 8; // Adjust to match your maze

// Maze grid
int maze[8][8] = {
  {0, 1, 1, 0, 0, 1, 1, 1},
  {0, 1, 0, 1, 1, 0, 1, 0},
  {0, 1, 0, 1, 1, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 1, 0},
  {0, 1, 1, 1, 0, 1, 1, 0},
  {0, 0, 0, 1, 0, 1, 1, 0},
  {1, 1, 0, 1, 0, 1, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0}
};

// Flood fill values
int floodFillValue = 1;
int goalX = 7;  // Adjust to the goal's position
int goalY = 0;  // Adjust to the goal's position

void setup() {
  // Initialize serial communication
  Serial.begin(9600);

  // Set IR sensor pins as inputs
  pinMode(leftIR, INPUT);
  pinMode(centerIR, INPUT);
  pinMode(rightIR, INPUT);
}

void loop() {
  int currentX = 0; // Starting X position
  int currentY = 7; // Starting Y position

  // Initialize the flood fill algorithm
  initializeFloodFill();

  // While the robot hasn't reached the goal
  while (currentX != goalX || currentY != goalY) {
    // Perform flood fill to find the path
    performFloodFill(currentX, currentY);

    // Determine the best direction to move
    int nextDirection = getNextMove(currentX, currentY);

    // Execute the move
    moveRobot(nextDirection);

    // Update current position
    currentX += dx[nextDirection];
    currentY += dy[nextDirection];
  }
}

void initializeFloodFill() {
  // Initialize the maze with large values
  for (int y = 0; y < mazeHeight; y++) {
    for (int x = 0; x < mazeWidth; x++) {
      maze[y][x] = 1000;
    }
  }

  // Set the goal position to 0
  maze[goalY][goalX] = 0;
}

void performFloodFill(int startX, int startY) {
  // Implement the flood fill algorithm to update maze[][] values
  // You need to determine how to mark walls and open paths in the maze
  // Update maze[y][x] with the minimum steps to reach the goal
  // Use a queue or a stack to manage the flood fill algorithm
}

int getNextMove(int currentX, int currentY) {
  // Determine the next move based on the maze[][] values
  // You need to choose the direction that leads to the lowest maze[][] value
  // Be careful to avoid obstacles
  // Return the direction (0 for forward, 1 for left, 2 for right)
}

void moveRobot(int direction) {
  // Implement motor control code to move the robot in the specified direction
  // You'll need to use the L293D motor driver to control the motors
  // Adjust motor1 and motor2 to move the robot accordingly
}


