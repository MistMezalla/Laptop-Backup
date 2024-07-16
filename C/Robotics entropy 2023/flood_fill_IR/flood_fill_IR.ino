#define LEFT_IR_SENSOR A0
#define RIGHT_IR_SENSOR A1
#define MOTOR_LEFT 5
#define MOTOR_RIGHT 6

#define ROWS 5
#define COLS 5

int maze[ROWS][COLS] = {
  {1, 1, 1, 1, 1},
  {1, 0, 0, 0, 1},
  {1, 1, 1, 0, 1},
  {1, 0, 0, 0, 0},
  {1, 1, 1, 1, 1}
};

bool is_valid(int x, int y) {
  return (x >= 0 && x < ROWS && y >= 0 && y < COLS && maze[x][y] == 0);
}

bool explore(int x, int y, int end_x, int end_y) {
  if (x == end_x && y == end_y) {
    return true; // Reached the end point
  }
  if (is_valid(x, y)) {
    maze[x][y] = 2; // Mark as visited
    int dx[4] = {1, -1, 0, 0};
    int dy[4] = {0, 0, 1, -1};
    for (int i = 0; i < 4; i++) {
      int new_x = x + dx[i];
      int new_y = y + dy[i];
      if (explore(new_x, new_y, end_x, end_y)) {
        return true;
      }
    }
    maze[x][y] = 0; // Unmark if not part of the solution path
  }
  return false;
}

void setup() {
  Serial.begin(9600);
  pinMode(LEFT_IR_SENSOR, INPUT);
  pinMode(RIGHT_IR_SENSOR, INPUT);
  pinMode(MOTOR_LEFT, OUTPUT);
  pinMode(MOTOR_RIGHT, OUTPUT);
  
  int start_x = 1;
  int start_y = 1;
  int end_x = 3;
  int end_y = 3;

  if (explore(start_x, start_y, end_x, end_y)) {
    Serial.println("Maze solution found:");
    for (int i = 0; i < ROWS; i++) {
      for (int j = 0; j < COLS; j++) {
        Serial.print(maze[i][j]);
        Serial.print(" ");
      }
      Serial.println();
    }
  } else {
    Serial.println("No solution found.");
  }
}

void loop() {
  // Maze solving and robot movement code here, using IR sensors to follow the lines.
  int leftSensorValue = digitalRead(LEFT_IR_SENSOR);
  int rightSensorValue = digitalRead(RIGHT_IR_SENSOR);
  
  // Adjust motor control based on sensor values to follow the lines.
  if (leftSensorValue == HIGH && rightSensorValue == HIGH) {
    // Both sensors are on the line, move forward.
    digitalWrite(MOTOR_LEFT, HIGH);
    digitalWrite(MOTOR_RIGHT, HIGH);
  } else if (leftSensorValue == LOW && rightSensorValue == HIGH) {
    // Only right sensor is on the line, turn right.
    digitalWrite(MOTOR_LEFT, HIGH);
    digitalWrite(MOTOR_RIGHT, LOW);
  } else if (leftSensorValue == HIGH && rightSensorValue == LOW) {
    // Only left sensor is on the line, turn left.
    digitalWrite(MOTOR_LEFT, LOW);
    digitalWrite(MOTOR_RIGHT, HIGH);
  }
  // You may need additional logic to handle turns and intersections.
}

/*
Make sure to connect your robot's motors to the specified motor control pins 
(e.g., MOTOR_LEFT and MOTOR_RIGHT) and adapt the code as needed for your specific robot and maze layout.
/*