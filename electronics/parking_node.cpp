#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <ESP8266HTTPClient.h>
#include <SoftwareSerial.h>

//Static IP address configuration
IPAddress staticIP(192, 168, 1, 145); //ESP static ip
IPAddress gateway(192, 168, 1, 1);   //IP Address of your WiFi Router (Gateway)
IPAddress subnet(255, 255, 255, 0);  //Subnet mask
IPAddress dns(8, 8, 8, 8);  //DNS
 
const char* ssid = "dkWork";
const char* password = "d152535k";
const char* deviceName = "Hehehehe";
ESP8266WebServer server(80);

String serverUrl = "192.168.1.100:5000";
String payload;
String device_key = "parking_secret";
String command = "parking_sensor";

int entrance_laser1 = 4;
int entrance_laser2 = 5;
int exit_laser1 = 6;
int exit_laser2 = 7;

int entrance_laser1_state = 0;
int entrance_laser2_state = 0;
int exit_laser1_state = 0;
int exit_laser2_state = 0;

int entrance_relay_down = 8
int entrance_relay_up = 9
int exit_relay_down = 10
int exit_relay_up = 11


void handlePong() {
  server.send(200, "text/html", device_key);
}


void check_car_presence() {
  String state = "0";
  String type = server.arg("type");
  type.trim();
  if (type == "entrance"){
    if (entrance_laser1_state == 1 && entrance_laser2_state == 1){
      state = "1";
    }
  }
  else if (type == "exit"){
    if (exit_laser1_state == 1 && exit_laser2_state == 1){
      state = "1";
    }
  }

  server.send(200, "text/html", state);
}


void manage_gate_relays(String type, String direction){

  if (type == "entrance"){
    // do we need to do this?
    digitalWrite(entrance_relay_down, 0);
    digitalWrite(entrance_relay_up, 0);

    if (direction == "up"){
      // !!! TODO: Add a clicking signal function, for press simulation
      digitalWrite(entrance_relay_up, 1);
    }
    else if (direction == "down"){
      digitalWrite(entrance_relay_down, 1);
    }      
  }

  if (type == "exit"){

    digitalWrite(exit_relay_down, 0);
    digitalWrite(exit_relay_up, 0);

    if (direction == "up"){
      digitalWrite(exit_relay_up, 1);
    }
    else if (direction == "down"){
      digitalWrite(exit_relay_down, 1);
    }      
  }
}

void control_gates(){
  String key = server.arg("device_key");
  if (key != device_key){
    server.send(401, "text/html", "Unauthorized");
  }

  String type = server.arg("type");
  type.trim();
  String direction = server.arg("direction");
  direction.trim();
  manage_gate_relays(type, direction);

  server.send(200, "text/html", "OK");
}


void setup(){
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  WiFi.disconnect();
  WiFi.hostname(deviceName);
  WiFi.config(staticIP, subnet, gateway, dns);
  WiFi.begin(ssid, password);
  WiFi.mode(WIFI_STA);
  delay(500);

  pinMode(entrance_laser1, INPUT);
  pinMode(entrance_laser2, INPUT);
  pinMode(exit_laser1, INPUT);
  pinMode(exit_laser2, INPUT);

  pinMode(entrance_relay_down, OUTPUT);
  pinMode(entrance_relay_up, OUTPUT);
  pinMode(exit_relay_down0, OUTPUT);
  pinMode(exit_relay_up1, OUTPUT);

  server.on("/ping/", handlePong);  
  server.on("/check-car-presence/", check_car_presence);
  server.on("/control/", control_gates);
 
  server.begin();
  Serial.println("HTTP server started");
}


void loop(){
  server.handleClient();

  entrance_laser1_state = digitalRead(entrance_laser1);
  entrance_laser2_state = digitalRead(entrance_laser2);
  exit_laser1_state = digitalRead(exit_laser1);
  exit_laser2_state = digitalRead(exit_laser2);
}