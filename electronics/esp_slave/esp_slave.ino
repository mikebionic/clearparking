#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <ESP8266HTTPClient.h>
#include <SoftwareSerial.h>

WiFiClient wifiClient;
const char* ssid = "home111";
const char* password = "d152535k";
const char* deviceName = "Hehehehe";
ESP8266WebServer server(80);

String serverUrl = "http://192.168.31.66:5000/";
String payload;
String device_key = "secret_key";
String command = "parking_sensor";

unsigned long previous_millis = 0;

String val_entrance_sensor_1 = "";
String val_entrance_sensor_2 = "";

String state = "0";

void handlePong() {
  server.send(200, "text/html", device_key);
}


void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  WiFi.disconnect();
  WiFi.hostname(deviceName);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  server.on("/ping/", handlePong);
  server.on("/check-car-presence/", check_car_presence);
  server.on("/control/", control_gates);

  server.begin();
  Serial.println(WiFi.localIP());
  Serial.println("HTTP server started");
  httpGETRequest();
  previous_millis = millis();
}


void loop() {
  if (millis() - previous_millis >= 180000) {
    httpGETRequest();
    previous_millis = millis();
  }
  if (Serial.available() != 0) {
    String data = Serial.readStringUntil('\n');
    data.trim();
    if (data.length() > 5) {
      val_entrance_sensor_1 = getValue(data, ':', 1);
      val_entrance_sensor_2 = getValue(data, ':', 3);
    }
  }
  server.handleClient();
}

void control_gates() {
  String key = server.arg("device_key");
  if (key != device_key) {
    server.send(401, "text/html", "Unauthorized");
  }

  String type = server.arg("type");
  type.trim();
  String directions = server.arg("direction");
  directions.trim();
  if (type == "entrance") {
    if (directions == "up") {
      Serial.println("type:entrance:direction:up");
    }
    else if (directions == "down") {
      Serial.println("type:entrance:direction:down");
    }
  }
  if (type == "exit") {
    if (directions == "up") {
      Serial.println("type:exit:direction:up");
    }
    else if (directions == "down") {
      Serial.println("type:exit:direction:down");
    }
  }
  server.send(200, "text/html", "OK");
}

void check_car_presence() {
  String type = server.arg("type");
  type.trim();

  String key = server.arg("device_key");
  if (key != device_key) {
    server.send(401, "text/html", state);
  }
  if (val_entrance_sensor_1 == "0") {
    Serial.println("OK");
  }
  if (val_entrance_sensor_2 == "0") {
    Serial.println("OK");
  }

  if (type == "entrance") {
    if (val_entrance_sensor_1 == "0" && val_entrance_sensor_2 == "0") {
      state = "1";
    } else {
      state = "0";
    }
  }
  if (type == "exit") {
    if (val_entrance_sensor_1 == "0" && val_entrance_sensor_2 == "0") {
      state = "1";
    } else {
      state = "0";
    }
  }
  server.send(200, "text/html", state);
}

void httpGETRequest() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    String apiGetData = serverUrl + "set-ip/?device_key=" + String(device_key);
    http.begin(wifiClient, apiGetData);
    int httpResponseCode = http.GET();
    String payload = "{}";
    if (httpResponseCode > 0) {
      Serial.print("HTTP Response code: ");
      Serial.print(httpResponseCode);
      payload = http.getString();
      Serial.println(payload);
    }
    else {
      Serial.print("Error code: ");
      Serial.println(httpResponseCode);
    }
    http.end();
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
