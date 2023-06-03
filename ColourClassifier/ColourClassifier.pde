float r = random(1), g = random(1), b = random(1);
String colour;
int counter = 0;

String[] trainingData = new String[1];
String[] s2;

void setup() {
  size(640, 360);
}
void draw() {
  background(int(r*256), int(g*256), int(b*256));
  textSize(32);
  text("red - r", 0, 32);
  text("orange - o", 0, 64);
  text("yellow - y", 0, 96);
  text("green - g", 0, 128);
  text("blue - b", 0, 170);
  text("purple - p", 0, 202);
  text("black - z", 0, 234);
  text("white - w", 0, 266);
  text(str(counter), 550, 32);
}
void keyPressed() {
  if (key == ESC) {
    saveStrings("trainingData2.txt", trainingData);
    exit();
  }
  else if (key == 'r') {
    colour = "red";
  }
  else if (key == 'o') {
    colour = "orange";
  }
  else if (key == 'y') {
    colour = "yellow";
  }
  else if (key == 'g') {
    colour = "green";
  }
  else if (key == 'b') {
    colour = "blue";
  }
  else if (key == 'p') {
    colour = "purple";
  }
  else if (key == 'z') {
    colour = "black";
  }
  else if (key == 'w') {
    colour = "white";
  }
  else return;
  s2 = append(trainingData, str(r)+" "+str(g)+" "+str(b)+" "+colour);
  trainingData = s2;
  r = random(1); g = random(1); b = random(1);
  counter += 1;
}
