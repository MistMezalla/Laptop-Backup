void setup() {
  #include <AFMotor.h>

AF_DCMotor motor3(3);
AF_DCMotor motor4(4);
int SPEED = 255;
int speed_Coeff = 3;
char command = 'S';

//3 Left Motor
//4 Right Motor
void setup() {
  // put your setup code here, to run once:
  motor3.run(RELEASE);
  motor4.run(RELEASE);
  Serial.begin(250000);
}

void loop() {
  digitalWrite(LED_BUILTIN, LOW);
   while(Serial.available()) {
    char command = (char)Serial.read();
    Serial.println(command);
    executeCommand(command);
  }
}

void executeCommand(char command) {
  switch (command) {
    case 'S': Stop(); break;
    case 'F': Forward(); break;
    case 'B': Backward(); break;
    case 'R': TurnRight(); break;
    case 'L': TurnLeft(); break;
    case 'G': ForwardLeft(); break;
    case 'H': BackwardLeft(); break;
    case 'I': ForwardRight(); break;
    case 'J': BackwardRight(); break;
    case '0'...'9': SPEED = ((command - '0') * 25); break;
    case 'q': SPEED = 255; break;
    default: Stop(); break;
  }
}



void Forward() {
  motor3.setSpeed(SPEED);
  motor4.setSpeed(SPEED);
  motor3.run(FORWARD);
  motor4.run(FORWARD);
}

void Backward() {
  motor3.setSpeed(SPEED);
  motor4.setSpeed(SPEED);
  motor3.run(BACKWARD);
  motor4.run(BACKWARD);
}

void TurnLeft() {
  motor3.setSpeed(SPEED);
  motor4.setSpeed(SPEED);
  motor3.run(BACKWARD);
  motor4.run(FORWARD);
}

void TurnRight() {
  motor3.setSpeed(SPEED);
  motor4.setSpeed(SPEED);
  motor3.run(FORWARD);
  motor4.run(BACKWARD);
}

void ForwardRight() {
  motor3.setSpeed(SPEED);
  motor4.setSpeed(SPEED / speed_Coeff);
  motor3.run(FORWARD);
  motor4.run(FORWARD);
}

void ForwardLeft() {
  motor3.setSpeed(SPEED / speed_Coeff);
  motor4.setSpeed(SPEED);
  motor3.run(FORWARD);
  motor4.run(FORWARD);
}

void BackwardLeft() {
  motor3.setSpeed(SPEED / speed_Coeff);
  motor4.setSpeed(SPEED);
  motor3.run(BACKWARD);
  motor4.run(BACKWARD);
}

void BackwardRight() {
  motor3.setSpeed(SPEED);
  motor4.setSpeed(SPEED / speed_Coeff);
  motor3.run(BACKWARD);
  motor4.run(BACKWARD);
}

void Stop() {
  motor3.setSpeed(0);
  motor4.setSpeed (0);
  motor3.run(RELEASE);
  motor4.run(RELEASE);
}
