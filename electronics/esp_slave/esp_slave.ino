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

  server.begin();
  Serial.println(WiFi.localIP());
  Serial.println("HTTP server started");
  httpGETRequest();
}


void loop() {
  if (millis() - previous_millis >= 180000) {
    httpGETRequest();
  }
  server.handleClient();

}
void httpGETRequest() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    String apiGetData = serverUrl + "set-ip/?device-key=" + String(device_key);
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
