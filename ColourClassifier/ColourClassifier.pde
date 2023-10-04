float r = random(1), g = random(1), b = random(1);
String colour;
int counter = 0;

String[] trainingData = new String[1];
String[] s2;
StringDict colourKeys;

void setup() {
  size(640, 360);
  colourKeys = new StringDict();
  colourKeys.set("r","red");
  colourKeys.set("o","orange");
  colourKeys.set("y","yellow");
  colourKeys.set("g","green");
  colourKeys.set("b","blue");
  colourKeys.set("p","purple");
  colourKeys.set("z","black");
  colourKeys.set("w","white");
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
    trainingData = removeFirstElement(trainingData);
    saveStrings("trainingData2.txt", trainingData);
    exit();
  }
  else if (colourKeys.hasKey(str(key))) colour = colourKeys.get(str(key));
  else return;
  
  println(colour);
  s2 = append(trainingData, str(r)+" "+str(g)+" "+str(b)+" "+colour);
  trainingData = s2;
  r = random(1); g = random(1); b = random(1);
  counter += 1;
}
String[] removeFirstElement(String[] inputArray) { // from ChatGPT
  if (inputArray.length <= 1) {
    return new String[0]; // Return an empty array if the original array has only one element or is empty
  }
  
  String[] result = new String[inputArray.length - 1];
  
  // Copy elements from inputArray to result, skipping the first element
  for (int i = 1; i < inputArray.length; i++) {
    result[i - 1] = inputArray[i];
  }
  
  return result;
}
