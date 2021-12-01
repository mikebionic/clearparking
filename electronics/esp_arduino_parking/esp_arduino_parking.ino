int entrance_sensor_1 = 8;
int entrance_relay = 13;
int val_entrance_sensor_1;
int val_entrance_sensor_3 = 1;

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
    val_entrance_sensor_1 = digitalRead(entrance_sensor_1);
    Serial.println("val_ent_1:" + String(val_entrance_sensor_1) + ":val_ent_2:" + String(val_entrance_sensor_1));
  }
  if (Serial.available() != 0) {
    String data = Serial.readStringUntil('\n');
    data.trim();
    if (data.length() > 15) {
      gate_management(data);
    }
  }
//  if (gate_state == true and val_entrance_sensor_1 == 0  and val_entrance_sensor_3 == 0) {
//    Serial.println("Close Door");
//    gate_state = false;
//  }
}

void gate_management(String data) {
  //type:entrance:direction:up
  String gate_type = getValue(data, ':', 1);
  String gate_direction = getValue(data, ':', 3);
  Serial.println(gate_type + " " + gate_direction);
  if (gate_type == "entrance" && gate_direction == "up") {
    gate_state = true;
    Serial.println("OK");
    pinMode(entrance_relay, LOW);
  } else {
    Serial.println("Error Here is No Car");
    pinMode(entrance_relay, HIGH);
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
