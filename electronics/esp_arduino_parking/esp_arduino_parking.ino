int entrance_sensor_1 = 8;
int entrance_relay = LED_BUILTIN;
bool gate_state = false;
unsigned long previous_millis = 0;
String data;
void setup() {
  Serial.begin(115200);
  pinMode(entrance_sensor_1, INPUT);
  pinMode(entrance_relay, OUTPUT);
}

void loop() {
  //values of sensors
  if (millis() - previous_millis >= 500) {
    previous_millis = millis();
    int val_entrance_sensor_1 = digitalRead(entrance_sensor_1);
    Serial.println("val_entrance_sensor_1:" + String(val_entrance_sensor_1) + " val_entrance_sensor_2:" + String(val_entrance_sensor_1));
    if (Serial.available() != 0) {
      String data = Serial.readStringUntil('\n');
      data.trim();
      gate_management(data, val_entrance_sensor_1);
    }
  }
}

void gate_management(String data, int val_entrance_sensor_1) {
  //type:entrance:direction:up
  String gate_type = getValue(data, ':', 1);
  String gate_direction = getValue(data, ':', 3);
  Serial.println(gate_type + " " + gate_direction);
  if (gate_type == "entrance" && gate_direction == "up") {
    gate_state = true;
    Serial.println("OK");
  } else {
    Serial.println("Error Here is No Car");
  }
}

String getValue(String data, char separator, int index) {
  int strIndex[] = {0, -1};
  int found = 0;
  int maxIndex = data.length() - 1;
  for (int i = 0; i <= maxIndex && found <= index; i++) {
    if (data.charAt(i) == separator || i == maxIndex) {
      found++;
      strIndex[0] = strIndex[1] + 1;
      strIndex[1] = (i == maxIndex) ? i + 1 : i;
    }
  }
  return found > index ? data.substring(strIndex[0], strIndex[1]) : "";
}
