#define ROWS 5
#define COLS 5

int maze[ROWS][COLS] = {
  {1, 0, 1, 1, 1},
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
    return true;  // Reached the end point
  }
  if (is_valid(x, y)) {
    maze[x][y] = 2;  // Mark as visited
    int dx[4] = {1, -1, 0, 0};
    int dy[4] = {0, 0, 1, -1};
    for (int i = 0; i < 4; i++) {
      int new_x = x + dx[i];
      int new_y = y + dy[i];
      if (explore(new_x, new_y, end_x, end_y)) {
        return true;
      }
    }
    maze[x][y] = 0;  // Unmark if not part of the solution path
  }
  return false;
}

void print_maze() {
  for (int i = 0; i < ROWS; i++) {
    for (int j = 0; j < COLS; j++) {
      Serial.print(maze[i][j]);
      Serial.print(" ");
    }
    Serial.println();
  }
}

void setup() {
  Serial.begin(9600);
  int start_x = 0;
  int start_y = 1;
  int end_x = 4;
  int end_y = 3;

  if (explore(start_x, start_y, end_x, end_y)) {
    Serial.println("Maze solution found:");
    print_maze();
  } else {
    Serial.println("No solution found.");
  }
}

void loop() {
  // Your loop code here, if needed
}
